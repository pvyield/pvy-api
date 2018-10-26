from flask_restplus import Resource, reqparse
from flask_jwt import jwt_required
from models.plantspec import PlantSpecModel

import sqlite3


class PlantSpec(Resource):
    TABLE_NAME = 'items'

    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    @jwt_required()
    def get(self, uid):
        """Read a plant configuration specification by unique identifier."""
        plantspec = PlantSpecModel.find_by_uid(uid)
        if plantspec:
            return plantspec.json()
        return {'message': 'Item not found'}, 404

    @jwt_required()
    def delete(self, uid):
        """Delete a plant configuration specification from the database by unique identifier."""
        plantspec = PlantSpecModel.find_by_uid(uid)
        if plantspec:
            plantspec.delete_from_db()

        return {'message': 'Item deleted'}


class PostPlantSpecSam(Resource):

    @jwt_required()
    def post(self):
        """Create a plant configuration specification in SAM definition format. Returns a unique identifier."""


class PostPlantSpecPvy(Resource):

    @jwt_required()
    def post(self):
        """Create a plant configuration specification in simplified pvyield format. This will translate to SAM format internally. Returns a unique identifier."""

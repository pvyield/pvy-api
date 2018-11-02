from flask_restplus import Resource, reqparse
from flask_jwt import jwt_required

from ..model.plantspec import PlantSpecModel
from ..util.dto import PlantSpecDto

api = PlantSpecDto.api
_plantSpecPvy = PlantSpecDto.plantSpecPvy
_plantSpecSam = PlantSpecDto.plantSpecSam

@api.route('/pvy/<puid>')
@api.param('puid', 'The plant specification unique identifier')
@api.response(404, 'User not found.')
class PlantSpec(Resource):
    TABLE_NAME = 'items'

    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    @jwt_required()
    @api.doc('get a plant specification')
    @api.marshal_with(_plantSpecPvy)
    def get(self, uid):
        """Read a plant configuration specification by unique identifier."""
        plantspec = PlantSpecModel.find_by_uid(uid)
        if plantspec:
            return plantspec.json()
        return {'message': 'Item not found'}, 404

    @jwt_required()
    def delete(self, uid):
        """Delete a plant configuration specification from the database by unique identifier."""
        plantSpecPvy = PlantSpecModel.find_by_uid(uid)
        if plantSpecPvy:
            plantSpecPvy.delete_from_db()

        return {'message': 'Item deleted'}


@api.route('/pvy/')
class PostPlantSpecPvy(Resource):

    @jwt_required()
    def post(self):
        """Create a plant configuration specification in simplified pvyield format. This will translate to SAM format internally. Returns a unique identifier."""


@api.route('/sam/')
class PostPlantSpecSam(Resource):

    @jwt_required()
    def post(self):
        """Create a plant configuration specification in SAM definition format. Returns a unique identifier."""


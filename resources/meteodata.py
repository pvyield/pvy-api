from flask_restplus import Resource, reqparse
from flask_jwt import jwt_required


class MeteoData(Resource):

    @jwt_required()
    def get(self, muid):
        """Check if the meteo dataset with 'muid' exists."""

    @jwt_required()
    def delete(self, muid):
        """Delete dataset defined by 'muid'."""


class PostMeteoData(Resource):

    @jwt_required()
    def post(self):
        """Create a meteorological dataset by providing hourly data."""


class CreateMeteoData(Resource):

    @jwt_required()
    def post(self):
        """Create a meteorological dataset by accessing weather data vendor APIs ."""

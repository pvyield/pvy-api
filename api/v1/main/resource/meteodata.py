from flask_restplus import Resource #, reqparse
from flask_jwt import jwt_required

from ..util.dto import MeteoDataDto

api = MeteoDataDto.api


@api.route('/<muid>')
@api.param('muid', 'The meteo dataset unique identifier')
@api.response(404, 'Entry not found.')
class MeteoData(Resource):

    @jwt_required()
    def get(self, muid):
        """Check if the meteo dataset with 'muid' exists."""

    @jwt_required()
    def delete(self, muid):
        """Delete dataset defined by 'muid'."""


@api.route('/upload/<string:format>')
class PostMeteoData(Resource):

    @jwt_required()
    def post(self):
        """Create a meteorological dataset by providing hourly data."""


@api.route('/create/<string:type>/<float:latitude>/<float:longitude>')
class CreateMeteoData(Resource):

    @jwt_required()
    def post(self):
        """Create a meteorological dataset by accessing weather data vendor APIs ."""

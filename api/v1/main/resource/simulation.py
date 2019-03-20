from flask_restplus import Resource #, reqparse
from flask_jwt import jwt_required

from ..util.dto import SimulationDto

api = SimulationDto.api


@api.route('/<string:puid>/<string:muid>/<string:fuid>')
class Simulate(Resource):

    @jwt_required()
    def get(self, puid, muid):
        """Simulate a configuration ('puid') with a meteo dataset ('muid'). Returns a simulation run id ('suid')"""

    @jwt_required()
    def delete(self, suid):
        """Delete simulation run defined by 'suid'."""


@api.route('/parametrize/<string:puid>/<string:muid>/<string:fuid>')
class Parametrize(Resource):

    @jwt_required()
    def get(self, puid, muid):
        """Run parametric analysis based on a baseline plant specification"""

    @jwt_required()
    def delete(self, suid):
        """Delete simulation run defined by 'suid'."""


@api.route('/optimize/<string:puid>/<string:muid>/<string:fuid>')
class Optimize(Resource):

    @jwt_required()
    def get(self, puid, muid, parameters, settings):
        """Optimize parameters of a configuration with a given meteo dataset based on optimization settings. Returns a plant configuration id of the optimized configuration."""


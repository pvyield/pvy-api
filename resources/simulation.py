from flask_restplus import Resource, reqparse
from flask_jwt import jwt_required


class Simulate(Resource):

    @jwt_required()
    def get(self, puid, muid):
        """Simulate a configuration ('puid') with a meteo dataset ('muid'). Returns a simulation run id ('suid')"""

    @jwt_required()
    def delete(self, suid):
        """Delete simulation run defined by 'suid'."""


class Optimize(Resource):

    @jwt_required()
    def get(self, puid, muid):
        """Optimize a configuration ('puid') with a meteo dataset ('muid'). Returns a simulation run id ('suid') of the optimized configuration."""


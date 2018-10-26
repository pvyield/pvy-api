from flask_restplus import Resource, reqparse
from flask_jwt import jwt_required


class Analyze(Resource):

    @jwt_required()
    def get(self, dataset, aggregation, metric):
        """Run a statistical analysis of a simulation run ('suid')"""

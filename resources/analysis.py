from flask_restplus import Resource, reqparse
from flask_jwt import jwt_required


class Analyze(Resource):

    @jwt_required()
    def get(self, suid, dataset, aggregation, metric):
        """Returns a single statistical metric value for a simulation run"""


class AnalyzePost(Resource):

    @jwt_required()
    def post(self, suid):
        """Runs a set of statistical analyses for a simulation run based on a json-file input"""

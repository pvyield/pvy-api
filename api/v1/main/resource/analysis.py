from flask_restplus import Resource, reqparse
from flask_jwt import jwt_required

from ..util.dto import AnalysisDto

api = AnalysisDto.api


@api.route('/<suid>/<dataset>/<aggregation>/<metric>')
@api.param('puid', 'The plant specification unique identifier')
class Analyze(Resource):

    @jwt_required()
    def get(self, suid, dataset, aggregation, metric):
        """Returns a single statistical metric value for a simulation run"""

@api.route('/<suid>/')
class AnalyzePost(Resource):

    @jwt_required()
    def post(self, suid):
        """Runs a set of statistical analyses for a simulation run based on a json-file input"""

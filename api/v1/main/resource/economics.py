from flask_restplus import Resource #, reqparse
from flask_jwt import jwt_required

from ..util.dto import economicsDto

api = economicsDto.api


@api.route('/financial/<string:fuid>')
@api.param('fuid', 'The financial dataset unique identifier')
@api.response(404, 'Entry not found.')
class Financial(Resource):

    @jwt_required()
    def get(self, fuid):
        """Check if the financial inputs with 'fuid' exists."""

    @jwt_required()
    def delete(self, fuid):
        """Delete dataset defined by 'fuid'."""


@api.route('/financial')
class PostFinancial(Resource):

    @jwt_required()
    def post(self):
        """Define a set of inputs to the financial model."""


@api.route('/lcoe/<string:fuid>')
@api.param('fuid', 'The LCOE dataset unique identifier')
class Lcoe(Resource):

    @jwt_required()
    def get(self, fuid):
        """Check if the LCOE inputs with 'fuid' exists."""

    @jwt_required()
    def delete(self, fuid):
        """Delete dataset defined by 'fuid'."""


@api.route('/lcoe')
class PostLcoe(Resource):

    @jwt_required()
    def post(self):
        """Define a set of inputs to the LCOE model."""

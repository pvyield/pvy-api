from flask_restplus import Resource, reqparse
from flask_jwt import jwt_required


class Financials(Resource):

    @jwt_required()
    def get(self, fuid):
        """Check if the financial inputs with 'fuid' exists."""

    @jwt_required()
    def delete(self, fuid):
        """Delete dataset defined by 'fuid'."""


class PostFinancials(Resource):

    @jwt_required()
    def post(self):
        """Define a set of inputs to the LCOE model or financial model."""

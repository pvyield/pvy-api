#import sqlite3
from flask_restplus import Resource, reqparse


#class UserRegister(Resource):
    # parser makes sure that only the given pars AND NO LESS are present
    #parser = reqparse.RequestParser()
    #parser.add_argument('username',
    #                 type=str,
    #                 required=True,
    #                 help='This field cannot be blank.'
    #)
    #parser.add_argument('password',
    #                 type=str,
    #                 required=True,
    #                 help='This field cannot be blank.'
    #)

    #def post(self):
    #    data = UserRegister.parser.parse_args()
#
    #    if User.find_by_username(data['username']):
    #        return {"message": "User with that username already exists."}, 400
#
    #    user = UserModel(**data) # parser ensures integrity of data, so can be passed as one
    #    user.save_to_db()

    #    return {"message": "User created successfully."}, 201

from flask import Flask, url_for, request
from flask_restplus import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from database import Database


application = Flask(__name__)
# SQLAlchemy has its own tracker, so deactivate Flask tracker
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.secret_key = 'asdaru347qcnz4r7r8527nftve8'
api = Api(application)

jwt = JWT(application, authenticate, identity)

# ADD RESOURCES
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    application.run()

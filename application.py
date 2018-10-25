from flask import Flask, url_for, request
from flask_restplus import Api
from flask_jwt import JWT
from werkzeug.contrib.fixers import ProxyFix

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from database import Database


application = Flask(__name__)
application.wsgi_app = ProxyFix(application.wsgi_app)

# SQLAlchemy has its own tracker, so deactivate Flask tracker
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.secret_key = 'asdaru347qcnz4r7r8527nftve8'

api = Api(application,
          version='0.1',
          title='pvyield API',
          description='Development prototype of the pvyield RESTful API service.',
          contact='info@pvyield.com',
          contact_url='https://pvyield.com')
jwt = JWT(application, authenticate, identity)


# ADD RESOURCES
ns_items = api.namespace('Items', description='Operations related to items.')
ns_items.add_resource(Item, '/item/<string:name>')
ns_items.add_resource(ItemList, '/items')
ns_users = api.namespace('Users', description='Operations related to users.')
ns_users.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    application.run(ssl_context='adhoc')

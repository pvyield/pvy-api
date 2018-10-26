from flask import Flask, url_for, request
from flask_restplus import Api
from flask_jwt import JWT
from werkzeug.contrib.fixers import ProxyFix

from security import authenticate, identity
from resources.user import UserRegister
from resources.plantspec import PlantSpec, PostPlantSpec
from resources.meteodata import MeteoData, CreateMeteoData, PostMeteoData
from resources.simulation import Simulate, Optimize

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
ns_spec = api.namespace('PlantSpec', description='Operations related to specifying the configuration of a power plant')
ns_spec.add_resource(PlantSpec, '/<string:puid>')
ns_spec.add_resource(PostPlantSpec, '/')

ns_meteo = api.namespace('MeteoData', description='Operations related to creating meteorological and irradiance datatsets')
ns_meteo.add_resource(MeteoData, '/<string:muid>')
ns_meteo.add_resource(CreateMeteoData, '/create/<string:type>/<float:latitude>/<float:longitude>')
ns_meteo.add_resource(PostMeteoData, '/post/')

ns_sim = api.namespace('Simulation', description='Operations related to simulations based on PlantSpec and MeteoData datasets')
ns_sim.add_resource(Simulate, '/simulate/<string:puid>/<string:muid>')
ns_sim.add_resource(Optimize, '/optimize/<string:puid>/<string:muid>')

ns_users = api.namespace('Users', description='Operations related to users')
ns_users.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    application.run()  # application.run(ssl_context='adhoc')

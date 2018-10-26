from flask import Flask, url_for, request
from flask_restplus import Api
from flask_jwt import JWT
from werkzeug.contrib.fixers import ProxyFix

from security import authenticate, identity
from resources.user import UserRegister
from resources.plantspec import PlantSpec, PostPlantSpecSam, PostPlantSpecPvy
from resources.meteodata import MeteoData, CreateMeteoData, PostMeteoData
from resources.financials import Financials, PostFinancials
from resources.simulation import Simulate, Optimize
from resources.analysis import Analyze, AnalyzePost

application = Flask(__name__)
application.wsgi_app = ProxyFix(application.wsgi_app)

# SQLAlchemy has its own tracker, so deactivate Flask tracker
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.secret_key = 'asdaru347qcnz4r7r8527nftve8'

api = Api(application,
          version='0.1',
          title='pvyield API',
          description='<table><tr>'
                      '<td>'
                      'Development <i><u>prototype</u></i> of the <b>pvyield RESTful API service</b>.<br />'
                      'This API provides a complete cloud-based toolchain for the performance analysis of large-scale, '
                      'solar photovoltaic power plants and allows to:'
                      '<ul><li>Define a <b>plant configuration</b> including main components,</li>'
                      '<li>Create and use <b>irradiance datasets</b> based on used-specified hourly data or datasets from commercial vendors,</li>' 
                      '<li>Optionally set <b>financial boundary conditions</b> for the overall analysis,</li>'
                      '<li><b>Run performance simulations</b> (based on <a href="https://www.nrel.gov/">NREL</a>-driven, open-source <a href="https://github.com/NREL/ssc">SAM</a>),</li>'
                      '<li><b>Optimize</b> for <a href="https://www.nrel.gov/analysis/tech-lcoe.html">LCOE</a>, <a href="https://en.wikipedia.org/wiki/Internal_rate_of_return">IRR</a>, or <a href="https://en.wikipedia.org/wiki/Net_present_value">NPV</a> with <a href="https://en.wikipedia.org/wiki/Genetic_algorithm">genetic optimization</a>, and finally to</li>'
                      '<li><b>Analyze results</b> via technical and economic statistical analysis (P90, P50, P10, etc.)</li></ul>'
                      'Feel free to <a href="mailto:info@pvyield.com">get in touch</a> if you are interested in this project.'
                      '</td>'
                      '<td style="text-align:right"><img src="http://external.pvyield.com/logo_02_darkblue_large.svg" alt="logo" style="width:250px;height:130px" /></td>'
                      '</tr></table>',
          contact='info@pvyield.com',
          contact_url='https://pvyield.com')
jwt = JWT(application, authenticate, identity)


# ADD RESOURCES
ns_spec = api.namespace('PlantSpec', description='Operations related to specifying the configuration of a power plant')
ns_spec.add_resource(PlantSpec, '/<string:puid>')
ns_spec.add_resource(PostPlantSpecSam, '/sam/')
ns_spec.add_resource(PostPlantSpecPvy, '/pvy/')

ns_meteo = api.namespace('MeteoData', description='Operations related to creating meteorological and irradiance datatsets')
ns_meteo.add_resource(MeteoData, '/<string:muid>')
ns_meteo.add_resource(CreateMeteoData, '/create/<string:type>/<float:latitude>/<float:longitude>')
ns_meteo.add_resource(PostMeteoData, '/upload/<string:format>')

ns_sim = api.namespace('Financials', description='Operations related to the setting the inputs for the economic analysis of simulation results')
ns_sim.add_resource(Financials, '/<string:fuid>')
ns_sim.add_resource(PostFinancials, '/')

ns_finance = api.namespace('Simulation', description='Operations related to simulations based on the PlantSpec, MeteoData, and Financials datasets')
ns_finance.add_resource(Simulate, '/simulate/<string:puid>/<string:muid>/<string:fuid>')
ns_finance.add_resource(Optimize, '/optimize/<string:puid>/<string:muid>/<string:fuid>/<string:parameters>/<string:settings>')

ns_analysis = api.namespace('Analysis', description='Operations related to analyzing simulation results')
ns_analysis.add_resource(Analyze, '/<string:suid>/<string:dataset>/<string:aggregation>/<string:metric>')
ns_analysis.add_resource(AnalyzePost, '/<string:suid>')

ns_users = api.namespace('Users', description='Operations related to users')
ns_users.add_resource(UserRegister, '/register')

# RUN APPLICATION
if __name__ == '__main__':
    application.run()  # application.run(ssl_context='adhoc')

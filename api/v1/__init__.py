from flask_restplus import Api
from flask import Blueprint

from .main.resource import user, plantspec, meteodata, economics, simulation, analysis

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          version='0.1(prototype)',
          title='pvyield API',
          description='<table><tr>'
                      '<td>'
                      'A development <i><u>prototype</u></i> of the <b>pvyield RESTful API service</b>.<br />'
                      'This API provides a complete cloud-based toolchain for the performance analysis of large-scale, '
                      'solar photovoltaic power plants and allows to:'
                      '<ul><li>Define a <b>plant configuration</b> including main components,</li>'
                      '<li>Create and use <b>irradiance datasets</b> based on user-specified hourly data or datasets from commercial vendors,</li>' 
                      '<li>Optionally set <b>financial boundary conditions</b> for the overall analysis,</li>'
                      '<li><b>Run performance simulations</b> (based on <a href="https://www.nrel.gov/">NREL</a>-driven, open-source <a href="https://github.com/NREL/ssc">SAM</a>),</li>'
                      '<li><b>Optimize</b> for LCOE, IRR, or NPV with <a href="https://en.wikipedia.org/wiki/Genetic_algorithm">genetic optimization</a>, and finally to</li>'
                      '<li><b>Analyze results</b> via technical and economic statistical analysis (P90, P50, P10, and other)</li></ul>'
                      'Feel free to <a href="mailto:info@pvyield.com">get in touch</a> if you are interested in this project.'
                      '</td>'
                      '<td style="text-align:right"><img src="http://external.pvyield.com/logo_02_darkblue_large.svg" alt="logo" style="width:250px;height:130px" /></td>'
                      '</tr><tr>'
                      '<td><img src="https://circleci.com/gh/pvyield/pvy-api/tree/master.svg?style=shield" /></td>'
                      '</tr></table>',
          contact='pvyield GmbH',
          contact_url='https://pvyield.com')

api.add_namespace(plantspec.api, path='/plantspec')
api.add_namespace(meteodata.api, path='/meteodata')
api.add_namespace(economics.api, path='/economics')
api.add_namespace(simulation.api, path='/simulation')
api.add_namespace(analysis.api, path='/analysis')
api.add_namespace(user.api, path='/user')

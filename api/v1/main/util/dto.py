from flask_restplus import Namespace, fields


class PlantSpecDto:
    api = Namespace('Plant Specification', description='Operations related to specifying the configuration of a power plant')
    plantSpecPvy = api.model('plantSpecPvy', {
        'plantSizeMetric': fields.String(required=True, description='Metric to define the size of the plant')
    })
    plantSpecSam = api.model('plantSpecSam', {
        'numberOfInverters': fields.String(required=True, description='Number of inverters')
    })


class MeteoDataDto:
    api = Namespace('Meteo Data', description='Operations related to creating meteorological and irradiance datatsets')


class economicsDto:
    api = Namespace('Economics', description='Operations related to the setting the inputs for the economic analysis of simulation results')


class SimulationDto:
    api = Namespace('Simulation', description='Operations related to simulations based on the PlantSpec, MeteoData, and Financials datasets')


class AnalysisDto:
    api = Namespace('Analysis', description='Operations related to analyzing simulation results')


class UserDto:
    api = Namespace('User', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })

import os
import unittest

from flask import redirect
from gevent.pywsgi import WSGIServer

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from werkzeug.middleware.proxy_fix import ProxyFix

# from flask_jwt import JWT
# from __security import authenticate, identity
# from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

import api.v1 as api_v1

# call the create_app function we created initially to create the application instance with the required parameter
# from the environment variable which can be either of the following - dev, prod, test.
# If none is set in the environment variable, the default dev is used.

app = api_v1.main.create_app(os.getenv('ENV_TYPE'))
app.register_blueprint(api_v1.blueprint, url_prefix='/v1')
app.app_context().push()
manager = Manager(app)
app.wsgi_app = ProxyFix(app.wsgi_app)
# jwt = JWT(app, authenticate, identity)

#migrate = Migrate(api, db)
#manager.add_command('db', MigrateCommand)


@app.route("/")
def index():
    return redirect('/v1/')


@manager.command  # marks function as executable from the command line.
def run():
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('api/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    sentry_sdk.init(
        dsn=os.getenv('SENTRY_DSN'),
        integrations=[FlaskIntegration()]
    )

    # run gevent
    http_server = WSGIServer(('0.0.0.0', 80), app)
    http_server.serve_forever()

    # run gunicorn
    # app.run(host='0.0.0.0')

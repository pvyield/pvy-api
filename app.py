import os
import unittest
from flask import redirect
from flask_jwt import JWT
# from __security import authenticate, identity

# from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from api.v1.main import create_app
from api.v1 import blueprint

# call the create_app function we created initially to create the application instance with the required parameter
# from the environment variable which can be either of the following - dev, prod, test.
# If none is set in the environment variable, the default dev is used.

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint, url_prefix='/v1')

app.app_context().push()
manager = Manager(app)
# jwt = JWT(app, authenticate, identity)

#migrate = Migrate(api, db)
#manager.add_command('db', MigrateCommand)


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


@app.route("/")
def index():
    return redirect('/v1/')


if __name__ == '__main__':
    app.run()  # manager.run()

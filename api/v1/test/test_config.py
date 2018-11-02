import os
import unittest

from flask import current_app
from flask_testing import TestCase

from application import application
from api import basedir


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        application.config.from_object('api.main.config.DevelopmentConfig')
        return application

    def test_app_is_development(self):
        self.assertFalse(application.config['SECRET_KEY'] is 'my_precious')
        self.assertTrue(application.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            application.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_main.db')
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        application.config.from_object('api.main.config.TestingConfig')
        return application

    def test_app_is_testing(self):
        self.assertFalse(application.config['SECRET_KEY'] is 'my_precious')
        self.assertTrue(application.config['DEBUG'])
        self.assertTrue(
            application.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
        )


class TestProductionConfig(TestCase):
    def create_app(self):
        application.config.from_object('api.main.config.ProductionConfig')
        return application

    def test_app_is_production(self):
        self.assertTrue(application.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()
# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import os


# basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    pass


class TestingConfig(Config):
    TESTING = True
    pass


class ProductionConfig(Config):
    DEBUG = False
    pass


config_dict = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}

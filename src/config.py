import os


class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = '123456789'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@localhost/chat_management'


class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI ='postgresql://postgres:123456@localhost/chat_management'
    JWT_SECRET_KEY = '123456789'


app_config = {
    'development': Development,
    'production': Production,
}
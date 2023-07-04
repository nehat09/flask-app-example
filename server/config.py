class DefaultConfig(object):
    DEBUG = True
    TESTING = False


class DevelopmentConfig(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///example.sqlite'


class TestConfig(DefaultConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

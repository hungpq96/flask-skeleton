class BaseConfig:

    DEBUG=True
    TEST=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI='sqlite:///:memory:'


class DevConfig(BaseConfig):

    ENV='development'


class ProdConfig(BaseConfig):

    DEBUG=False
    TEST=False
    ENV='production'


class TestConfig(BaseConfig):

    DEBUG=False
    Test=True
    ENV='testing'

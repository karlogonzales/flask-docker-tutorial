class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DefaultConfig(Config):
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True

import os


class Config(object):
    """Parent configuration class"""
    CSRF_ENABLED = True
    DEBUG = False
    SECRET = os.getenv("SECRET")


class DevelopmentConfig(Config):
    """Configurations for Development"""
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    """Configurations for Production"""
    DEBUG = False
    TESTING = False


app_config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}

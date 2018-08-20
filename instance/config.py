import os


class Config(object):
    """Parent Configurations."""
    DEBUG = False
    TESTING = False
    SECRET = os.urandom(24)

class TestingConfig(Config):
    """Configurations for Testing."""
    TESTING = True
    DEBUG = True

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True

app_config = {
    'testing': TestingConfig,
    'development': DevelopmentConfig
}
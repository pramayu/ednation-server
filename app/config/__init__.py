class Config(object):
    DEBUG=False
    DEVELOPMENT=False

class DevelopmentConfig(Config):
    DEBUG=True
    DEVELOPMENT=True
    MONGODB_HOST = 'mongodb://localhost:27017/db_dev_ednation'

class ProductionConfig(Config):
    pass
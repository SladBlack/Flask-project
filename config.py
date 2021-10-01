from decouple import config


class Config:
    DEBUG = False
    SECRET_KEY = config('SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = config('FLASK_DEBUG')
    ENV = config('FLASK_ENV')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    DB_USERNAME = config('DB_USERNAME')
    DB_NAME = config('DB_NAME')
    DB_PASSWORD = config('DB_PASSWORD')
    DB_HOST = config('DB_HOST')

    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

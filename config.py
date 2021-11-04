import os

class Config:

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key=999bbd53fa99dbb16324841ca2c577a1'
    MOVIE_API_KEY = os.environ.get('999bbd53fa99dbb16324841ca2c577a1')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:malcomiz0582@localhost/movies'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
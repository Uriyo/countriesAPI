import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres_user:postgres_password@localhost:5432/countries_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
    PORT=5000

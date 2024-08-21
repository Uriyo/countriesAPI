import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://default:AElZVWcDj6p5@ep-calm-butterfly-a7bus4ae.ap-southeast-2.aws.neon.tech:5432/verceldb?sslmode=require'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
    PORT=5000

# postgresql://postgres_user:postgres_password@localhost:5432/countries_db
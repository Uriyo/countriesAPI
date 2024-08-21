from flask import Flask
from config import Config
from db import db, migrate
from routes import init_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    init_routes(app)

    return app

app = create_app()


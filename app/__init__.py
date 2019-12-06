from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
migrate = Migrate()
marshmallow = Marshmallow()


def create_app(configs):

    app = Flask(__name__)
    app.config.from_object(configs)

    db.init_app(app)
    migrate.init_app(app, db)
    marshmallow.init_app(app)

    return app

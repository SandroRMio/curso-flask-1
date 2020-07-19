from flask_migrate import Migrate
from delivery.ext.db import models  # avisa o migrate das tabelas

migrate = Migrate()


def init_app(app):
    migrate.init_app(app)

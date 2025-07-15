# backend/app/__init__.py

from flask import Flask
from flask_cors import CORS
from .models import db
from .routes import main as main_blueprint

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configuración de la base de datos (SQLite local)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendees.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar la base de datos
    db.init_app(app)

    # Registrar las rutas
    app.register_blueprint(main_blueprint)

    return app


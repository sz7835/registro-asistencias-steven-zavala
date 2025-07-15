from flask import Flask
from .routes import example_bp  # 👈 importamos la ruta

def create_app():
    app = Flask(__name__)
    app.register_blueprint(example_bp)  # 👈 la registramos
    return app

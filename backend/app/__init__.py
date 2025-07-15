from flask import Flask

def create_app():
    app = Flask(__name__)

    # Importar y registrar los blueprints aquí si existen
    # por ejemplo:
    # from .routes import example_bp
    # app.register_blueprint(example_bp)

    return app

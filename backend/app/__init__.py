from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    # Habilitar CORS
    CORS(app)

    from .routes import api_bp
    app.register_blueprint(api_bp)

    return app

app = create_app()

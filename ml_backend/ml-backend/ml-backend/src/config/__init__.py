from flask import Blueprint
from .irrigation_routes import irrigation_bp
from .copra_routes import copra_bp
from .health_routes import health_bp

api_bp = Blueprint('api', __name__)

def init_app(app):
    app.register_blueprint(irrigation_bp, url_prefix='/api/irrigation')
    app.register_blueprint(copra_bp, url_prefix='/api/copra')
    app.register_blueprint(health_bp, url_prefix='/api/health')
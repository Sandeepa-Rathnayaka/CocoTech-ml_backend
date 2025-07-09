from flask import Blueprint
from src.api.irrigation_routes import irrigation_bp
from src.api.copra_routes import copra_bp
from src.api.health_routes import health_bp

def init_app(app):
    """Initialize all API routes"""
    # Register blueprints
    app.register_blueprint(irrigation_bp, url_prefix='/api/irrigation')
    app.register_blueprint(copra_bp, url_prefix='/api/copra')
    app.register_blueprint(health_bp, url_prefix='/api/health')
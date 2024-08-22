from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)

    from app.routes import usuario_routes, tipousuario_routes, computador_routes,home_route, perisferico_routes, registro_routes, vigilante_routes
    app.register_blueprint(usuario_routes.bp)
    app.register_blueprint(tipousuario_routes.bp)
    app.register_blueprint(computador_routes.bp)
    app.register_blueprint(home_route.bp)
    app.register_blueprint(perisferico_routes.bp)
    app.register_blueprint(registro_routes.bp)
    app.register_blueprint(vigilante_routes.bp)

    return app
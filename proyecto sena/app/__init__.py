from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_idUser):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        from .models.user import User
        return User.query.get(int(user_idUser))

    from app.routes import usuario_routes, tipousuario_routes, computador_routes,home_route, perisferico_routes, registro_routes, vigilante_routes
    app.register_blueprint(usuario_routes.bp)
    app.register_blueprint(tipousuario_routes.bp)
    app.register_blueprint(computador_routes.bp)
    app.register_blueprint(home_route.bp)
    app.register_blueprint(perisferico_routes.bp)
    app.register_blueprint(registro_routes.bp)
    app.register_blueprint(vigilante_routes.bp)

    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)
    
    return app
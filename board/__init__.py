from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    db.init_app(app)

    login_manager.init_app(app)
    from .home import index_bp as index_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(index_blueprint)
    app.register_blueprint(auth_blueprint)

    return app
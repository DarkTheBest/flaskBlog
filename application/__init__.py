from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .config import Config


db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder='../templates')
    app.config.from_object(Config)
    app.app_context().push()

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from authentication.models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    from .routes import bp as main_blueprint
    app.register_blueprint(main_blueprint)

    from authentication.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app

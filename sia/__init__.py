from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path, getenv, urandom
from flask_login import LoginManager


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = getenv("SECRET_KEY", urandom(24))
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    
 

    # blueprint for auth routes in our app
    from .auth import auth 
    app.register_blueprint(auth)

    # blueprint for non-auth parts of app
    from .views import views
    app.register_blueprint(views)

    from .models import User
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app


def create_database(app):
    if not path.exists('website/' + "db.sqlite"):
        db.create_all(app=app)
        print('Created Database!')

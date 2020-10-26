#import flask - from the package import a module
from flask import Flask 
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db=SQLAlchemy()

#create a function that creates a web application
# a web server will run this web application
def create_app():
    print(__name__)  #let us be curious - what is this __name__ 
    app=Flask(__name__)  # this is the name of the module/package that is calling this app
    app.secret_key='anythingyoulike'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///marketplace.sqlite'
    #initialize db with flask app
    db.init_app(app)

    UPLOAD_FOLDER = '/static/Images'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    #initialize the login manager
    login_manager = LoginManager()
    #set the name of the login function that lets user login
    # in our case it is auth.login (blueprintname.viewfunction name)
    login_manager.login_view='auth.login'
    login_manager.init_app(app)

    #create a user loader function takes userid and returns User
    from .models import User # importing here to avoid circular references
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    bootstrap = Bootstrap(app)
    from . import views
    app.register_blueprint(views.mainbp)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import items
    app.register_blueprint(items.bp)

    return app

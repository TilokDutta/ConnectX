from flask import Flask
from backend.models import *
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# from backend.api_controllers import api
app=None #initially none

def init_app():
    connectX_app=Flask(__name__) #object of Flask
    connectX_app.debug=True
    connectX_app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///connectX.sqlite3"
    connectX_app.app_context().push() #Direct access app by other modules(db, authentication)
    connectX_app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///connectX.sqlite3"
    db.init_app(connectX_app) #object.method(<parameter>)
    # api.init_app(connectX_app)
    migrate = Migrate(app, db)

    print("connectX application started....")
    return connectX_app

app=init_app()
from backend.controllers import *

if __name__=="__main__":
    app.run()
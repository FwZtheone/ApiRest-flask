# PYTHON IMPORT

# FLASK IMPORT
from flask import Flask
from flask_restful import  Api
from flask_sqlalchemy import SQLAlchemy


#PERSONNAL IMPORT
from .controller.user import User


database = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    api = Api(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
   
    database.init_app(app)
    
    
    api.add_resource(User, '/')
    return app
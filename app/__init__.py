# PYTHON IMPORT

# FLASK IMPORT
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api


#PERSONNAL IMPORT



database = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    api = Api(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
   
    database.init_app(app)
    
    class HelloWorld(Resource):
        def get(self):
            return {'hello': 'world'}

    api.add_resource(HelloWorld, '/')
        
    return app
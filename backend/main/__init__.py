from flask_jwt_extended import JWTManager
import os
from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail



api = Api()

db = SQLAlchemy()

jwt = JWTManager()

mailsender = Mail()


def create_app():
    app = Flask(__name__)
    load_dotenv()
    
    
    if not os.path.exists(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')):
        os.mknod(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME'))
    
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')
    db.init_app(app)

    import main.resources as resources
    
    api.add_resource(resources.PoemsResource, '/poems')
    api.add_resource(resources.PoemResource, '/poem/<id>')
    api.add_resource(resources.QualificationsResource, '/qualifications')
    api.add_resource(resources.QualifyResource, '/qualify/<id>')
    api.add_resource(resources.UsersResource, '/users')
    api.add_resource(resources.UserResource, '/user/<id>')
    api.add_resource(resources.PoemInfoResource,'/poeminfo')
    api.init_app(app)
    

    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = os.getenv('JWT_ACCESS_TOKEN_EXPIRES')
    jwt.init_app(app)
    
    from .auth import routes
    app.register_blueprint(auth.routes.auth)
    
    #Configuración de mail
    app.config['MAIL_HOSTNAME'] = os.getenv('MAIL_HOSTNAME')
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
    app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS')
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['FLASKY_MAIL_SENDER'] = os.getenv('FLASKY_MAIL_SENDER')
    #Inicializar en app
    mailsender.init_app(app)

    return app

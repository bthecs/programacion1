import os
from flask import Flask
from dotenv import load_dotenv
from main.routes import routes

def create_app():
    
    app = Flask(__name__)
    
    load_dotenv()
    app.register_blueprint(routes.app)
    
    
    return app
from flask import Flask
from db import mysql
from config import config
from routes import category_bp
from flask_cors import CORS

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    CORS(app, origins=["http://localhost:5173"], supports_credentials=True)
    # Initialize MySQL
    mysql.init_app(app)
    
    # Register blueprints
    app.register_blueprint(category_bp)
    
    return app
app = create_app()
if __name__ == '__main__':
    app.run(port=5001)
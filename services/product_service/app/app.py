from routes import product_bp
from flask import Flask
from db import mysql
from config import config
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"], supports_credentials=True)
mysql.init_app(app)
app.register_blueprint(product_bp)

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run(port=5002)
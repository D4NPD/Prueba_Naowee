from flask import Flask
from db import mysql
from config import config
from routes import order_bp
from flask_cors import CORS

app = Flask(__name__)
mysql.init_app(app)
CORS(app, origins=["http://localhost:5173"], supports_credentials=True)
app.register_blueprint(order_bp)

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run(port=5004)
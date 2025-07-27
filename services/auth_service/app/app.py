from flask import Flask
from routes import auth_bp
from config import config
from db import mysql
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"], supports_credentials=True)
app.register_blueprint(auth_bp)

mysql.init_app(app)

if __name__ == '__main__':
  app.config.from_object(config['development'])
  app.run()

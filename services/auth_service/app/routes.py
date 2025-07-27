from flask import jsonify, request, Blueprint, current_app
from models import loginFuntion
from User import User
import datetime
import jwt
from config import config

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods = ['GET', 'POST'])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    user = User(0, "", email, password, "")
    logged_user = loginFuntion(user)

    if logged_user:
        if logged_user.password:
            payload = {
                'user_id': logged_user.user_id,
                'rol': logged_user.rol,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
            }
            token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')

            return jsonify({
                'token': token,
                'user': {
                    'id': logged_user.user_id,
                    'name': logged_user.name,
                    'email': logged_user.email,
                    'rol': logged_user.rol
                }
            }), 200
        else:
            return jsonify({'error': 'Invalid password'}), 401
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

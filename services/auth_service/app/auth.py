from functools import wraps
from flask import request, jsonify, g, current_app
import jwt

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            parts = request.headers['Authorization'].split()
            if len(parts) == 2 and parts[0] == 'Bearer':
                token = parts[1]

        if not token:
            return jsonify({'error': 'Token requerido'}), 401

        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            g.user = {
                'id_usuario': data['user_id'],
                'rol': data['rol']
            }
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Token inválido'}), 401

        return f(*args, **kwargs)
    return decorated

def require_role(role):
    def decorator(f):
        @wraps(f)
        @token_required
        def wrapped(*args, **kwargs):
            if g.user['rol'] != role:
                return jsonify({'error': 'Acceso denegado, rol insuficiente'}), 403
            return f(*args, **kwargs)
        return wrapped
    return decorator
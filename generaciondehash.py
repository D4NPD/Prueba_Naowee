from werkzeug.security import generate_password_hash

print(generate_password_hash('test2', method='pbkdf2:sha256'))
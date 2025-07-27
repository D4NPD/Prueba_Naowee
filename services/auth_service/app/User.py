from werkzeug.security import generate_password_hash, check_password_hash

class User():
  
  def __init__ (self, user_id, name, email, password, rol)->None:
    self.user_id = user_id
    self.name = name
    self.email = email
    self.password = password
    self.rol = rol

  @classmethod
  def checkPassword(self, hashed_password, password):
    return check_password_hash(hashed_password, password)
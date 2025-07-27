from db import mysql
from User import User

def loginFuntion(user):
  try:
    cursor = mysql.connection.cursor()
    sql = "SELECT * FROM users WHERE email = %s"
    cursor.execute(sql, (user.email,))
    row = cursor.fetchone()
    if row != None:
      user = User(row[0], row[1], row[2], User.checkPassword(row[3],user.password), row[4])
      return user
    else:
      return None  
  except Exception as e:
    return {"error": str(e)}, 500
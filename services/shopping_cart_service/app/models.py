from db import mysql

def getCartByUserId(user_id):
  cursor = mysql.connection.cursor()
  sql = """
        SELECT cp.cart_product_id, p.name, cp.amount, p.unit_price, p.iva
        FROM shopping_carts c
        JOIN cart_product cp ON c.cart_id = cp.cart_id
        JOIN Products p ON p.product_id = cp.product_id
        WHERE c.user_id = %s
        """
  cursor.execute(sql, (user_id,))
  data = cursor.fetchall()
  return data
  cursor.close()

def addProductToCart(user_id, product_id, amount):
  cursor = mysql.connection.cursor()
  sql = "SELECT cart_id FROM shopping_carts WHERE user_id = %s"
  cursor.execute(sql, (user_id,))
  cart = cursor.fetchone()
  if not cart:
    sql = "INSERT INTO shopping_carts (user_id) VALUES (%s)"
    cursor.execute(sql, (user_id,))
    mysql.connection.commit()
    cart_id = cursor.lastrowid
  else:
    cart_id = cart[0]
  sql = "INSERT INTO cart_product (cart_id, product_id, amount) VALUES (%s, %s, %s)" \
        "ON DUPLICATE KEY UPDATE amount = amount + %s"
  cursor.execute(sql, (cart_id, product_id, amount, amount))
  mysql.connection.commit()
  cursor.close()
  return {'message': 'Product added to cart successfully', 'cart_id': cart_id}

def updateAmountInCart(cart_product_id, amount):
  cursor = mysql.connection.cursor()
  sql = "UPDATE cart_product SET amount = %s WHERE cart_product_id = %s"
  cursor.execute(sql, (amount, cart_product_id))
  mysql.connection.commit()
  return cursor.rowcount > 0

def deleteProductFromCart(cart_product_id):
  cursor = mysql.connection.cursor()
  sql = "DELETE FROM cart_product WHERE cart_product_id = %s"
  cursor.execute(sql, (cart_product_id,))
  mysql.connection.commit()
  return cursor.rowcount > 0

def emptyCart(user_id):
  cursor = mysql.connection.cursor()
  sql = "DELETE FROM cart_product WHERE cart_id IN (SELECT cart_id FROM shopping_carts WHERE user_id = %s)"
  cursor.execute(sql, (user_id,))
  mysql.connection.commit()
  return cursor.rowcount > 0
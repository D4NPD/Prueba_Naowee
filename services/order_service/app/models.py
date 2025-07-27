from db import mysql
from flask_mysqldb import MySQLdb
def createOrder(user_id):
  cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
  sql = "SELECT cart_id FROM shopping_carts WHERE user_id = %s"
  cursor.execute(sql, (user_id,))
  cart_id = cursor.fetchone()
  if not cart_id:
    return {"error": "Cart not found for user"}
  cart_id = cart_id['cart_id']
  sql = """SELECT cp.product_id, cp.amount, p.unit_price, p.iva
           FROM cart_product cp
           JOIN products p ON cp.product_id = p.product_id
           WHERE cp.cart_id = %s"""
  cursor.execute(sql, (cart_id,))
  products = cursor.fetchall()
  if not products:
    return {"error": "No products in cart"}
  total = sum([(p['unit_price'] * p['amount'])*(1 + p['iva']/100) for p in products])
  sql = """INSERT INTO orders (user_id, total)
           VALUES (%s, %s)"""
  cursor.execute(sql, (user_id, total))
  order_id = cursor.lastrowid
  for product in products:
    sql = """INSERT INTO order_product (order_id, product_id, amount, unit_price, iva)
             VALUES (%s, %s, %s, %s, %s)"""
    cursor.execute(sql, (order_id, product['product_id'], product['amount'], product['unit_price'], product['iva']))

  sql = "DELETE FROM cart_product WHERE cart_id = %s"
  cursor.execute(sql, (cart_id,))
  mysql.connection.commit()
  cursor.close()
  return {"mensaje": "Order created successfully", "order_id": order_id, "total": total}

def getOrderbyUserId(user_id):
  cursor = mysql.connection.cursor()
  sql = """SELECT order_id,date, total FROM orders WHERE user_id = %s ORDER BY date DESC"""
  cursor.execute(sql, (user_id,))
  orders = cursor.fetchall()
  cursor.close()
  return orders if orders else {"error": "No orders found for user"}

def getOrderDetails(order_id):
  cursor = mysql.connection.cursor()
  sql = """SELECT op.product_id, op.amount, op.unit_price, op.iva, p.name
           FROM order_product op
           JOIN products p ON op.product_id = p.product_id
           WHERE op.order_id = %s"""
  cursor.execute(sql, (order_id,))
  detalle = cursor.fetchall()
  if not detalle:
    return {"error": "No products found for order"}
  
  cursor.close()
  return detalle if detalle else {"error": "Order not found"}

def getAllOrders():
  cursor = mysql.connection.cursor()
  sql = """SELECT o.order_id, o.date, o.total, u.name
           FROM orders o
           JOIN users u ON o.user_id = u.user_id
           ORDER BY o.date DESC"""
  cursor.execute(sql)
  orders = cursor.fetchall()
  cursor.close()
  return orders if orders else {"error": "No orders found"}
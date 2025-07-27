from db import mysql

def getProducts():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()
    return data
    cursor.close()

def getProductById(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM products WHERE product_id = %s", (id,))
    data = cursor.fetchone()
    cursor.close()
    return data if data else None

def createProduct(product):
    cursor = mysql.connection.cursor()
    cursor.execute("""INSERT INTO products (name, description, size, url_picture, 
                   unit_price, iva, category_id) VALUES (%s, %s, %s,%s,%s,%s,%s)""", 
                   (product['name'], product['description'], product['size'], product['url_picture'],
                    product['unit_price'], product['iva'], product['category_id']))
    mysql.connection.commit()
    cursor.close()
    return cursor.lastrowid

def updateProduct(id, product):
    cursor = mysql.connection.cursor()
    cursor.execute("""UPDATE products SET name = %s, description = %s, size = %s, 
                   url_picture = %s, unit_price = %s, iva = %s, category_id = %s 
                   WHERE product_id = %s""", 
                   (product['name'], product['description'], product['size'], 
                    product['url_picture'], product['unit_price'], product['iva'], 
                    product['category_id'], id))
    mysql.connection.commit()
    cursor.close()
    return cursor.rowcount > 0

def deleteProduct(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM products WHERE product_id = %s", (id,))
    mysql.connection.commit()
    cursor.close()
    return cursor.rowcount > 0
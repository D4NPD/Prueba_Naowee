from db import mysql

def get_Allcategories():
    cursor=mysql.connection.cursor()
    sql = "SELECT * FROM categories"
    cursor.execute(sql)
    datos = cursor.fetchall()
    return datos

def get_Onecategory(id):
    cursor = mysql.connection.cursor()
    sql = "SELECT * FROM categories WHERE category_id = %s"
    cursor.execute(sql, (id,))
    datos = cursor.fetchone()
    return datos if datos else None

def create_Newcategory(name, description):
    cursor = mysql.connection.cursor()
    sql = "INSERT INTO categories (name, description) VALUES (%s, %s)"
    cursor.execute(sql, (name, description))
    mysql.connection.commit()
    return cursor.lastrowid   

def update_Onecategory(id, name, description):
    cursor = mysql.connection.cursor()
    sql = "UPDATE categories SET name = %s, description = %s WHERE category_id = %s"
    cursor.execute(sql, (name, description, id))
    mysql.connection.commit()
    return cursor.rowcount > 0

def delete_Onecategory(id):
    cursor = mysql.connection.cursor()
    sql = "DELETE FROM categories WHERE category_id = %s"
    cursor.execute(sql, (id,))
    mysql.connection.commit()
    return cursor.rowcount > 0
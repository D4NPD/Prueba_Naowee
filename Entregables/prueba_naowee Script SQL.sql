CREATE DATABASE prueba_naowee;
USE prueba_naowee;

-- Tabla: Usuario
CREATE TABLE IF NOT EXISTS Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    rol ENUM('cliente', 'admin') NOT NULL
);

-- Tabla: Categoria
CREATE TABLE IF NOT EXISTS Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

-- Tabla: Producto
CREATE TABLE IF NOT EXISTS Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    size VARCHAR(20),
    url_picture VARCHAR(255),
    unit_price DECIMAL(10,2) NOT NULL,
    iva DECIMAL(5,2) NOT NULL,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

-- Tabla: Carrito
CREATE TABLE IF NOT EXISTS Shopping_Carts (
    cart_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Tabla: Carrito_Producto
CREATE TABLE IF NOT EXISTS Cart_Product (
    PRIMARY KEY (cart_id, product_id),
    cart_id INT NOT NULL,
    product_id INT NOT NULL,
    amount INT NOT NULL,
    FOREIGN KEY (cart_id) REFERENCES Shopping_Carts(cart_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- Tabla: Pedido
CREATE TABLE IF NOT EXISTS Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    date DATETIME DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(12,2),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Tabla: Pedido_Producto
CREATE TABLE IF NOT EXISTS Order_Product (
    PRIMARY KEY (order_id, product_id),
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    amount INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    iva DECIMAL(5,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);


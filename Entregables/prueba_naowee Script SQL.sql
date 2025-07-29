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

INSERT INTO users (name, email, password, rol) VALUES ('admin', 'admin@test.com', 'pbkdf2:sha256:600000$gGrGH111ApbDhdaK$2727854757efe7dc0123c7fbdfc83a862e1c33ff9951986ca47e242c071b532e',2)
INSERT INTO users (name, email, password, rol) VALUES ('test', 'test@test.com', 'pbkdf2:sha256:600000$lQcocU3GUzPLongl$3cf66aaf7d075c75749695be6f75df4aa13db23318a07c3bc3a94685c1ca4888',1)
INSERT INTO users (name, email, password, rol) VALUES ('test2', 'test2@test.com', 'pbkdf2:sha256:600000$AQhb1AZaxrk0A3ey$aeaac7e8f2de82d6c3c4edcc7a82c33f723d682680b7ce62adddb90a0346fdf9',1)

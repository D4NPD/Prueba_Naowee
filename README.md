Tienda Deportiva - Full Stack App
Esta es una aplicación web de comercio electrónico desarrollada como parte de una prueba
técnica. Permite a los usuarios explorar productos deportivos, agregarlos al carrito, realizar
compras, y a los administradores gestionar el catálogo y pedidos.
Tecnologías utilizadas
Frontend
- React + Vite
- Context API para autenticación
- Axios para consumo de API REST
- CSS personalizado
Backend
Microservicios desarrollados con Flask y organizados en:
- auth_service: autenticación con JWT y manejo de roles.
- products_service: gestión de productos y categorías.
- cart_service: gestión del carrito.
- orders_service: creación y consulta de pedidos.
Base de datos
- MySQL 8+
Requisitos
- Node.js 18+
- Python 3.10+
- MySQL (con base de datos ya creada según el script)
- Pipenv o entorno virtual (recomendado)
Instalación y ejecución
1. Clonar el repositorio
git clone https://github.com/D4NPD/Prueba_Naowee.git
cd tienda-deportiva
2. Configurar la base de datos
- Crea la base de datos en MySQL.
- Ejecuta el script db_script.sql proporcionado en /entregables/.
- Ajusta los datos de conexión en cada microservicio (config.py o .env).
3. Backend - Levantar microservicios
Para cada microservicio:
cd backend/auth_service
python -m venv env
env\Scripts\activate
python app.py
4. Frontend - React
cd frontend
npm install
npm run dev
Rutas protegidas y roles
- Autenticación mediante tokens JWT.
-CREDENCIALES DE AUTENTICACION:
 admin@test.com : admin123
 test@test.com : test
 test2@test.com : test2
- Validación por roles: user y admin.
Navegación principal
/login Inicio de sesión Público
/productos Catálogo de productos Usuario
/carrito Visualización y checkout Usuario
/pedidos Historial de pedidos Usuario
/admin Dashboard de administración Admin
Microservicios y puertos
Servicio Puerto Endpoints
Auth 5000 /login, /register
Products 5001 /products, /categories
Cart 5003 /cart, /cart/add
Orders 5002 /create_order, /get_order
Funcionalidades completas
- Login con JWT y control de roles
- Navegación protegida
- Visualización de productos
- Carrito y checkout
- Historial de pedidos
- Panel de administración (categorías, productos, pedidos)
- Arquitectura de microservicios
Autor
Desarrollado por Daniel Pizarro De Moya como parte de la prueba técnica para Naowee S.A

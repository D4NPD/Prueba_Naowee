import { useEffect, useState, useContext } from "react";
import apiProducts from "../services/apiProducts";
import apiCart from "../services/apiCart";
import { AuthContext } from "../context/AuthContext";
import "../styles/Product.css";

const Products = () => {
  const { token, user } = useContext(AuthContext);
  const [productos, setProductos] = useState([]);

  const fetchProductos = async () => {
    try {
      const res = await apiProducts.get("/products", {
        headers: { Authorization: `Bearer ${token}` },
      });
      setProductos(res.data);
    } catch (err) {
      console.error("Error al obtener productos:", err);
    }
  };

  const agregarAlCarrito = async (producto) => {
    try {
      await apiCart.post(
        "/cart/add",
        {
          user_id: user.id,
          product_id: producto[0],
          amount: 1,
        },
        {
          headers: { Authorization: `Bearer ${token}` },
        }
      );
      alert("Producto añadido al carrito.");
    } catch (err) {
      console.error("Error al agregar al carrito:", err);
    }
  };

  useEffect(() => {
    fetchProductos();
  }, []);

  return (
    <div className="container">
      <h2>Productos</h2>
      <div className="productos-grid">
        {productos.map((prod) => (
          <div className="card" key={prod[0]}>
            <img src={prod[4]} alt="" />
            <h3>{prod[1]}</h3>
            <p>{prod[2]}</p>
            <p><strong>${prod[5].toLocaleString()}</strong></p>
            <button className="btn btn-crear" onClick={() => agregarAlCarrito(prod)}>
              Añadir al carrito
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Products;

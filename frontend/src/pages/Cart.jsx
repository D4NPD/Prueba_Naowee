import { useEffect, useState, useContext } from "react";
import apiCart from "../services/apiCart";
import apiOrder from "../services/apiorder";
import { AuthContext } from "../context/AuthContext";
import { Navigate } from "react-router-dom";

const Cart = () => {
  const { token, user } = useContext(AuthContext);
  const [carrito, setCarrito] = useState([]);

  const fetchCarrito = async () => {
    try {
      const res = await apiCart.get(`/cart/${user.id}`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      setCarrito(res.data);
    } catch (err) {
      console.error("Error al obtener carrito:", err);
    }
  };

  const finalizarCompra = async () => {
    try {
      await apiOrder.post(
        "/create_order",
        { user_id: user.id },
        {
          headers: { Authorization: `Bearer ${token}` },
        }
      );
      fetchCarrito();
      alert("¡Compra realizada con éxito!");
      <Navigate to="/order" />;
    } catch (err) {
      console.error("Error al finalizar compra:", err);
    }
  };

  useEffect(() => {
    fetchCarrito();
  }, []);

  return (
    <div>
      <h2>🛒 Carrito</h2>
      {carrito.length === 0 ? (
        <p>Tu carrito está vacío.</p>
      ) : (
        <>
          <ul>
            {carrito.map((item) => (
              <li key={item[0]}>
                {item[1]} × {item[2]} – ${ (item[3] * item[2]).toLocaleString() }
              </li>
            ))}
          </ul>
          <button className="btn btn-editar" onClick={finalizarCompra}>
            Finalizar compra
          </button>
        </>
      )}
    </div>
  );
};

export default Cart;

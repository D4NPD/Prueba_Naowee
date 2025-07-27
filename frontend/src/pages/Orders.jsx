
import { useEffect, useState, useContext } from "react";
import apiOrder from "../services/apiorder";
import { AuthContext } from "../context/AuthContext";

const Orders = () => {
  const { token, user } = useContext(AuthContext);
  const [historial, setHistorial] = useState([]);

  const fetchHistorial = async () => {
    try {
      const res = await apiOrder.get(`/get_order/${user.id}`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      setHistorial(Array.isArray(res.data) ? res.data : []);
    } catch (err) {
      console.error("Error al obtener historial:", err);
      setHistorial([]);
    }
  };

  useEffect(() => {
    fetchHistorial();
  }, []);

  return (
    <div>
      <h2>📜 Historial de pedidos</h2>
      {historial.length === 0 ? (
        <p>No has realizado compras aún.</p>
      ) : (
        <ul>
          {historial.map((pedido) => (
            <li key={pedido[0]}>
              Pedido #{pedido[0]} – Total: ${pedido[2].toLocaleString()} –{" "}
              {new Date(pedido[1]).toLocaleDateString()}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default Orders;

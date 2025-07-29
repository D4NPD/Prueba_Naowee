import { useState, useEffect, useContext } from "react";
import apiOrder from "../../services/apiOrder";
import { AuthContext } from "../../context/AuthContext";

const AdminOrders = () => {
  const { token } = useContext(AuthContext);
  const [pedidos, setPedidos] = useState([]);
  const [detalle, setDetalle] = useState([]);
  const [pedidoActivo, setPedidoActivo] = useState(null);

  const fetchPedidos = async () => {
    try {
      const res = await apiOrder.get("/get_all_orders", {
        headers: { Authorization: `Bearer ${token}` },
      });
      setPedidos(Array.isArray(res.data) ? res.data : []);
    } catch (err) {
      console.error("Error al obtener pedidos:", err);
    }
  };

  const fetchDetalle = async (id) => {
    try {
      const res = await apiOrder.get(`/get_order_details/${id}`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      setDetalle(res.data);
      setPedidoActivo(id);
    } catch (err) {
      console.error("Error al obtener detalle:", err);
    }
  };

  useEffect(() => {
    fetchPedidos();
  }, []);

  return (
    <div>
      <h2>Historial de Pedidos</h2>

      <table className="table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Usuario</th>
            <th>Fecha</th>
            <th>Total</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {pedidos.map((pedido) => (
            <tr key={pedido[0]}>
              <td>{pedido[0]}</td>
              <td>{pedido[3]}</td>
              <td>{new Date(pedido[1]).toLocaleString()}</td>
              <td>${pedido[2].toLocaleString()}</td>
              <td>
                <button className="btn btn-editar" onClick={() => fetchDetalle(pedido[0])}>
                  Ver detalle
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {pedidoActivo && detalle.length > 0 && (
        <div className="modal">
          <h3>Detalle del pedido #{pedidoActivo}</h3>
          <table className="table">
            <thead>
              <tr>
                <th>Producto</th>
                <th>Cantidad</th>
                <th>Precio Unitario</th>
                <th>IVA</th>
                <th>Subtotal</th>
              </tr>
            </thead>
            <tbody>
              {detalle.map((item) => (
                <tr key={item[0]}>
                  <td>{item[4]}</td>
                  <td>{item[1]}</td>
                  <td>${item[2].toLocaleString()}</td>
                  <td>{item[3]}%</td>
                  <td>
                    ${((item[2] * item[1]) * (1 + item[3] / 100)).toLocaleString()}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
          <button className="btn" onClick={() => setPedidoActivo(null)}>
            Cerrar detalle
          </button>
        </div>
      )}
    </div>
  );
};

export default AdminOrders;

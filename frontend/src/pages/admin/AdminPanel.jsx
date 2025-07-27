import Sidebar from "./Sidebar";
import { Outlet } from "react-router-dom";

const AdminPanel = () => {
  return (
    <div style={{ display: "flex" }}>
      <Sidebar />
      <main style={{ marginLeft: "220px", padding: "24px", width: "100%" }}>
        <h1>Bienvenido al Panel de Administración</h1>
        <Outlet/>
      </main>
    </div>
  );
};

export default AdminPanel;

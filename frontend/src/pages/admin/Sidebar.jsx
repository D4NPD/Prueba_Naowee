import { Link, useLocation } from "react-router-dom";
import "../../styles/Sidebar.css"; // 

const Sidebar = () => {
  const location = useLocation();

  const links = [
    { path: "/admin/categorias", label: "Categorías" },
    { path: "/admin/productos", label: "Productos" },
    { path: "/admin/pedidos", label: "Pedidos" },
  ];

  return (
    <aside className="sidebar">
      <h2>Admin</h2>
      <nav>
        {links.map((link) => (
          <Link
            key={link.path}
            to={link.path}
            className={location.pathname === link.path ? "active" : ""}
          >
            {link.label}
          </Link>
        ))}
      </nav>
    </aside>
  );
};

export default Sidebar;

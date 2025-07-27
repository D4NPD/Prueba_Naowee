import { useContext } from "react";
import { Link, useNavigate } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";
import "../styles/Navbar.css";

const Navbar = () => {
  const { token, logout, user } = useContext(AuthContext);
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  return (
    <nav className="navbar">
      <div className="navbar-logo">
        <Link to="/">SportShop</Link>
      </div>
      <div className="navbar-links">
        {token ? (
          <>
            <Link className="link-btn" to="/products">Productos</Link>
            <Link className="link-btn" to="/cart">Carrito</Link>
            <Link className="link-btn" to="/order">Pedidos</Link>
            {user?.rol === "admin" && <Link className="link-btn" to="/admin">Admin</Link>}
            <button onClick={handleLogout} className="logout-btn">
              Cerrar sesión
            </button>
          </>
        ) : (
          <Link to="/login">Login</Link>
        )}
      </div>
    </nav>
  );
};

export default Navbar;

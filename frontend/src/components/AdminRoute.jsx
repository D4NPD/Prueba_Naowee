import { useContext } from "react";
import { Navigate } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";

const AdminRoute = ({ children }) => {
  const { token, user } = useContext(AuthContext);

  if (!token) return <Navigate to="/login" replace />;
  if (user?.rol !== "admin") return <Navigate to="/" replace />;

  return children;
};

export default AdminRoute;

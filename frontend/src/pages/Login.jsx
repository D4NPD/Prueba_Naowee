import { useState, useContext } from "react";
import { AuthContext } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";
import apiAuth from "../services/apiAuth";
import "../styles/Login.css";
const Login = () => {
  const { login } = useContext(AuthContext);
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const res = await apiAuth.post("/login", { email, password });
      login(res.data.token, res.data.user);
      if (res.data.user.rol === "admin") {
        console.log(res.data.user.rol);
        navigate("/admin",{ replace: true });
      }else{
        navigate("/products",{ replace: true });
      }
    } catch (err) {
      console.log(err);
      setError("Credenciales incorrectas");
    }
  };

  return (
    <div className="login-container">
      <form onSubmit={handleSubmit} className="login-form">
        <h2 className="login-title">Iniciar Sesión</h2>

        <input
          className="login-input"
          type="email"
          placeholder="Correo electrónico"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <input
          className="login-input"
          type="password"
          placeholder="Contraseña"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        {error && <p className="login-error">{error}</p>}

        <button className="login-button" type="submit">
          Ingresar
        </button>
      </form>
    </div>
  );
};

export default Login;

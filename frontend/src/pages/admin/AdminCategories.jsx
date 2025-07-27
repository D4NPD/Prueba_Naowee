import { useEffect, useState, useContext } from "react";
import apiCategory from "../../services/apiCategory";
import CategoriaForm from "../../components/CategoryForm";
import { AuthContext } from "../../context/AuthContext";
import "../../styles/AdminCategory.css";

const Categorias = () => {
  const [categorias, setCategorias] = useState([]);
  const [mostrarForm, setMostrarForm] = useState(false);
  const [categoriaActual, setCategoriaActual] = useState(null);
  const { token } = useContext(AuthContext);

  const fetchCategorias = async () => {
    try {
      const res = await apiCategory.get("/categories", {
        headers: { Authorization: `Bearer ${token}` },
      });
      setCategorias(res.data);
    } catch (err) {
      console.error("Error al obtener categorías:", err);
    }
  };

  useEffect(() => {
    fetchCategorias();
  }, []);

  const handleEliminar = async (id) => {
    if (!window.confirm("¿Estás seguro de eliminar esta categoría?")) return;
    try {
      await apiCategory.delete(`/categories/${id}`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      fetchCategorias();
    } catch (err) {
      console.error("Error al eliminar:", err);
    }
  };

  return (
    <div>
      <h2>Categorías</h2>
      <button
        className="btn btn-crear"
        onClick={() => {
          setCategoriaActual(null);
          setMostrarForm(true);
        }}
      >
        ➕ Crear categoría
      </button>

      <table className="table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Descripción</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {categorias.map((cat) => (
            <tr key={cat[0]}>
              <td>{cat[0]}</td>
              <td>{cat[1]}</td>
              <td>{cat[2]}</td>
              <td>
                <button
                  className="btn btn-editar"
                  onClick={() => {
                    setCategoriaActual(cat);
                    setMostrarForm(true);
                  }}
                >
                  Editar
                </button>
                <button
                  className="btn btn-eliminar"
                  onClick={() => handleEliminar(cat[0])}
                >
                  Eliminar
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {mostrarForm && (
        <CategoriaForm
          categoria={categoriaActual}
          onClose={() => setMostrarForm(false)}
          onSuccess={fetchCategorias}
        />
      )}
    </div>
  );
};

export default Categorias;

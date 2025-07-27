import { useState, useContext } from "react";
import apiCategory from "../services/apiCategory.js";
import { AuthContext } from "../context/AuthContext";

const CategoryForm = ({ categoria, onClose, onSuccess }) => {
  const [name, setName] = useState(categoria?.name || "");
  const [description, setDescription] = useState(categoria?.description || "");
  const { token } = useContext(AuthContext);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = { name, description };

    try {
      if (categoria) {
        // Editar
        await apiCategory.put(`/categories/${categoria[0]}`, data, {
          headers: { Authorization: `Bearer ${token}` },
        });
      } else {
        // Crear
        await apiCategory.post("/categories", data, {
          headers: { Authorization: `Bearer ${token}` },
        });
      }
      onClose();
      onSuccess();
    } catch (err) {
      console.error("Error al guardar categoría:", err);
    }
  };

  return (
    <div className="modal">
      <form onSubmit={handleSubmit}>
        <h3>{categoria ? "Editar" : "Crear"} Categoría</h3>
        <input
          type="text"
          placeholder="Nombre"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <textarea
          placeholder="Descripción"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          rows="3"
        />
        <button type="submit" className="btn btn-crear">
          Guardar
        </button>
        <button type="button" className="btn" onClick={onClose}>
          Cancelar
        </button>
      </form>
    </div>
  );
};

export default CategoryForm;

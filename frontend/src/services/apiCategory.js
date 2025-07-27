import axios from "axios";

const apiCategory = axios.create({
  baseURL: "http://localhost:5001", // Cambia si usas otro puerto
  headers: {
    "Content-Type": "application/json",
  },
});

export default apiCategory;

import axios from "axios";

const apiCart = axios.create({
  baseURL: "http://localhost:5003", // puerto real de tu microservicio
});

export default apiCart;

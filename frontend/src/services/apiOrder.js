import axios from "axios";

const apiOrder = axios.create({
  baseURL: "http://localhost:5004", // Puerto de tu microservicio de pedidos
});

export default apiOrder;

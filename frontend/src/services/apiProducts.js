import axios from "axios";

const apiProducts = axios.create({
  baseURL: "http://localhost:5002",
});

export default apiProducts;
import axios from "axios";


const apiAuth = axios.create({
  baseURL: "http://localhost:5000",
  headers: {
    "Content-Type": "application/json",
  },
});

export default apiAuth;

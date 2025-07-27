import { Routes, Route } from "react-router-dom";
import Login from "./pages/login";
import Products from "./pages/Products";
import Navbar from "./components/Navbar";
import PrivateRoute from "./components/PrivateRoute";
import AdminRoute from "./components/AdminRoute";
import AdminPanel from "./pages/admin/AdminPanel";
import AdminCategories from "./pages/admin/AdminCategories";
import AdminProducts from "./pages/admin/AdminProducts";
import AdminOrders from "./pages/admin/AdminOrders";
import Cart from "./pages/Cart";
import Orders from "./pages/Orders";

const App = () => {
  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route
          path="/products"
          element={
            <PrivateRoute>
              {" "}
              <Products />{" "}
            </PrivateRoute>
          }
        />
        <Route
          path="/admin"
          element={
            <AdminRoute>
              <AdminPanel />
            </AdminRoute>
          }
        >
          <Route path="categorias" element={<AdminCategories />} />
          <Route path="productos" element={<AdminProducts />} />
          <Route path="pedidos" element={<AdminOrders />} />
        </Route>
        <Route
          path="/cart"
          element={
            <PrivateRoute>
              <Cart />
            </PrivateRoute>
          }
        />
        <Route
          path="/order"
          element={
            <PrivateRoute>
              <Orders />
            </PrivateRoute>
          }
        />
      </Routes>
    </>
  );
};

export default App;

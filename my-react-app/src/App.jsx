import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import CustomerForm from './components/CustomerForm';
import ProductForm from './components/ProductForm';
import OrderForm from './components/OrderForm';
import CustomerList from './components/CustomerList';
import ProductList from './components/ProductList';
import OrderList from './components/OrderList';

const Home = () => <h1>Home Page</h1>; 
const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />  
        <Route path="/customer/new" element={<CustomerForm />} />
        <Route path="/customer/edit/:id" element={<CustomerForm />} />
        <Route path="/customers" element={<CustomerList />} />

        <Route path="/product/new" element={<ProductForm />} />
        <Route path="/product/edit/:id" element={<ProductForm />} />
        <Route path="/products" element={<ProductList />} />

        <Route path="/order/new" element={<OrderForm />} />
        <Route path="/order/edit/:id" element={<OrderForm />} />
        <Route path="/orders" element={<OrderList />} />
      </Routes>
    </Router>
  );
};

export default App;

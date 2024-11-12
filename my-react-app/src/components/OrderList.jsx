import React, { useState, useEffect } from 'react';
import { getOrders } from '../services/orderService';
import { Button, Table } from 'react-bootstrap';

const OrderList = () => {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    const fetchOrders = async () => {
      try {
        const response = await getOrders();
        setOrders(response.data);
      } catch (error) {
        console.error('Error fetching orders:', error);
      }
    };

    fetchOrders();
  }, []);

  const handleDelete = (id) => {
    
  };

  return (
    <div>
      <h2>Order List</h2>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>Order Number</th>
            <th>Shipping Address</th>
            <th>Payment Method</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {orders.map((order) => (
            <tr key={order.id}>
              <td>{order.number}</td>
              <td>{order.shippingAddress}</td>
              <td>{order.paymentMethod}</td>
              <td>
                <Button variant="primary" href={`/order/edit/${order.id}`}>
                  Edit
                </Button>
                <Button
                  variant="danger"
                  onClick={() => handleDelete(order.id)}
                >
                  Delete
                </Button>
              </td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export default OrderList;

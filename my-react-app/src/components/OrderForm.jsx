import React, { useState } from 'react';
import { createOrder } from '../services/orderService';
import { Button, Form } from 'react-bootstrap';

const OrderForm = () => {
  const [number, setNumber] = useState('');
  const [shippingAddress, setShippingAddress] = useState('');
  const [paymentMethod, setPaymentMethod] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    const orderData = { number, shippingAddress, paymentMethod };

    await createOrder(orderData);
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group controlId="number">
        <Form.Label>Order Number</Form.Label>
        <Form.Control
          type="text"
          value={number}
          onChange={(e) => setNumber(e.target.value)}
          required
        />
      </Form.Group>

      <Form.Group controlId="shippingAddress">
        <Form.Label>Shipping Address</Form.Label>
        <Form.Control
          type="text"
          value={shippingAddress}
          onChange={(e) => setShippingAddress(e.target.value)}
          required
        />
      </Form.Group>

      <Form.Group controlId="paymentMethod">
        <Form.Label>Payment Method</Form.Label>
        <Form.Control
          type="text"
          value={paymentMethod}
          onChange={(e) => setPaymentMethod(e.target.value)}
          required
        />
      </Form.Group>

      <Button type="submit">Submit</Button>
    </Form>
  );
};

export default OrderForm;

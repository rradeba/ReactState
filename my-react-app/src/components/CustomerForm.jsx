import React, { useState, useEffect } from 'react';
import { createCustomer, updateCustomer } from '../services/customerService';
import { Button, Form } from 'react-bootstrap';

const CustomerForm = ({ customerId, existingData }) => {
  const [name, setName] = useState(existingData ? existingData.name : '');
  const [email, setEmail] = useState(existingData ? existingData.email : '');
  const [phone, setPhone] = useState(existingData ? existingData.phone : '');

  useEffect(() => {
    if (existingData) {
      setName(existingData.name);
      setEmail(existingData.email);
      setPhone(existingData.phone);
    }
  }, [existingData]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const customerData = { name, email, phone };

    if (customerId) {
      // Update customer
      await updateCustomer(customerId, customerData);
    } else {
      // Create new customer
      await createCustomer(customerData);
    }
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group controlId="name">
        <Form.Label>Name</Form.Label>
        <Form.Control
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
      </Form.Group>

      <Form.Group controlId="email">
        <Form.Label>Email</Form.Label>
        <Form.Control
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
      </Form.Group>

      <Form.Group controlId="phone">
        <Form.Label>Phone</Form.Label>
        <Form.Control
          type="text"
          value={phone}
          onChange={(e) => setPhone(e.target.value)}
          required
        />
      </Form.Group>

      <Button type="submit">Submit</Button>
    </Form>
  );
};

export default CustomerForm;

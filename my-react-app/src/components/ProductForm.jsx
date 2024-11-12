import React, { useState, useEffect } from 'react';
import { createProduct, updateProduct } from '../services/productService';
import { Button, Form } from 'react-bootstrap';

const ProductForm = ({ productId, existingData }) => {
  const [name, setName] = useState(existingData ? existingData.name : '');
  const [price, setPrice] = useState(existingData ? existingData.price : '');

  useEffect(() => {
    if (existingData) {
      setName(existingData.name);
      setPrice(existingData.price);
    }
  }, [existingData]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const productData = { name, price };

    if (productId) {
      // Update product
      await updateProduct(productId, productData);
    } else {
      // Create new product
      await createProduct(productData);
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

      <Form.Group controlId="price">
        <Form.Label>Price</Form.Label>
        <Form.Control
          type="text"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
          required
        />
      </Form.Group>

      <Button type="submit">Submit</Button>
    </Form>
  );
};

export default ProductForm;

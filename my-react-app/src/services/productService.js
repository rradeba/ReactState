import axiosInstance from './axiosInstance';

export const getProducts = () => {
  return axiosInstance.get('/products'); 
};

export const createProduct = (productData) => {
  return axiosInstance.post('/products', productData);  
};

export const updateProduct = (productData) => {
  return axiosInstance.post('/products', productData);  
};
import axiosInstance from './axiosInstance';

export const getOrders = () => {
  return axiosInstance.get('/orders');  
};

export const createOrder = (orderData) => {
  return axiosInstance.post('/orders', orderData);  
};

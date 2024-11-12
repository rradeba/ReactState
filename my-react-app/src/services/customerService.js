import axiosInstance from './axiosInstance';

export const getCustomers = () => {
  return axiosInstance.get('/customers');  
};

export const createCustomer = (customerData) => {
  return axiosInstance.post('/customers', customerData);  
};


export const deleteCustomer = async (id) => {
  try {
    await axios.delete(`${API_URL}/${id}`);
  } catch (error) {
    console.error('Error deleting customer:', error);
    throw error; 
  }
};

export const updateCustomer = (customerData) => {
  return axiosInstance.post('/customers', customerData);  
};



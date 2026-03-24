// API configuration
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://127.0.0.1:8000';

// API endpoints
export const API_ENDPOINTS = {
  // User endpoints
  users: `${API_BASE_URL}/api/users/`,
  login: `${API_BASE_URL}/api/login/`,
  logout: `${API_BASE_URL}/api/logout/`,
  profiles: `${API_BASE_URL}/api/profiles/`,
  
  // Product endpoints
  products: `${API_BASE_URL}/api/products/`,
  productDetail: (id) => `${API_BASE_URL}/api/products/${id}/`,
  
  // Cart endpoints
  cart: `${API_BASE_URL}/api/cart/`,
  cartItem: (id) => `${API_BASE_URL}/api/cart/${id}/`,
  
  // Wishlist endpoints
  wishlists: `${API_BASE_URL}/api/wishlists/`,
  wishlistDetail: (id) => `${API_BASE_URL}/api/wishlists/${id}/`,
  
  // Order endpoints
  orders: `${API_BASE_URL}/api/orders/`,
  orderDetail: (id) => `${API_BASE_URL}/api/orders/${id}/`,
};

// Appwrite configuration (if using Appwrite services)
export const APPWRITE_CONFIG = {
  endpoint: process.env.REACT_APP_APPWRITE_ENDPOINT || 'https://cloud.appwrite.io/v1',
  projectId: process.env.REACT_APP_APPWRITE_PROJECT_ID || '',
};

export default API_BASE_URL;

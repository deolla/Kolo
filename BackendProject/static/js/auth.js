// This file handles user authentication logic
import { loginUser } from './api';

export const authenticateUser = async (username, password) => {
  try {
    const response = await loginUser(username, password);

    if (response.token) {
      localStorage.setItem('token', response.token);  // Store the token in localStorage
      return true;  // Authentication successful
    }

    // Handle authentication failure
    return false;
  } catch (error) {
    console.error('Authentication error:', error);
    throw error;
  }
};

import { create } from 'zustand'
import axios from 'axios';
const useAuthStore = create(set => ({
  user: null,
  token: null,
  isLoading: false,
  error: null,

  login: async (email, pwd) => {
    set({ isLoading: true, error: null });
    try {
      const response = await axios.post('http://192.168.30.145:8080/api/login', { email, pwd });
      const { user, token } = response.data;
      set({ user, token, isLoading: false });
    } catch (error) {
      set({ error: error.response?.data?.message || 'Login failed', isLoading: false });
    }
  },

  logout: () => set({ user: null, token: null })
}));

export default useAuthStore;
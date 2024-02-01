import axios from 'axios';
import useAuthStore from '../store/store';

const api = axios.create({
  // baseURL: 'http://192.168.30.145:8080/api' //민수
  baseURL: 'http://192.168.30.206:8080/api' //동현
});

api.interceptors.request.use(config => {
  const accessToken = useAuthStore.getState().accessToken;
  if (accessToken) {
    config.headers.Authorization = `Bearer ${accessToken}`;
  }
  return config;
});

export const fetchProtectedData = async () => {
  try {
    const response = await api.get('/protected');
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const refreshToken = async () => {
  try {
    const response = await api.post('/auth/reissu', {
      refreshToken: localStorage.getItem('refreshToken'),
    });
    const { accessToken, refreshToken } = response.data;
    localStorage.setItem('token', `Bearer ${accessToken}`);
    localStorage.setItem('refreshToken', refreshToken);
    return { accessToken, refreshToken };
  } catch (error) {
    throw error;
  }
};

export { api };

import axios from "axios";
import { ACCESS_TOKEN } from "./constants";

const apiUrl = "/choreo-apis/awbo/backend/rest-api-be2/v1.0";

const api = axios.create({
    // Import anything in env var file
    baseURL: import.meta.env.VITE_API_URL ? import.meta.env.VITE_API_URL : apiUrl,
  });

api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem(ACCESS_TOKEN);
        if (token) {
        config.headers.Authorization = `Bearer ${token}`; // Pass JWT token
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

// Default to using api instead of axios
export default api;
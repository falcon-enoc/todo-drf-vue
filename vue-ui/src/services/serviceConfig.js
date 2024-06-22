// services/serviceConfig.js
import axios from "axios";

// Definir apiUrl
//const apiUrl = import.meta.env.VITE_BACKEND_URL || "http://localhost:8000";

//console.log("API URL:", apiUrl);

// Crear una instancia de Axios
const api = axios.create({
  //baseURL: `${apiUrl}/api/`, // URL base API
  baseURL: "http://192.168.1.21:8000/api",
  timeout: 10000, // Tiempo de espera en milisegundos
  headers: {
    "Content-Type": "application/json",
    // Puedes agregar otros encabezados predeterminados aquí
  },
});

// Interceptor de solicitud
api.interceptors.request.use(
  (config) => {
    // Agrega lógica antes de enviar la solicitud, como agregar un token de autenticación
    // Ejemplo: config.headers['Authorization'] = 'Bearer ' + token;
    return config;
  },
  (error) => {
    // Manejo de error en la solicitud
    return Promise.reject(error);
  }
);

// Interceptor de respuesta
api.interceptors.response.use(
  (response) => {
    // Maneja la respuesta aquí si es necesario
    return response;
  },
  (error) => {
    // Manejo de error en la respuesta
    return Promise.reject(error);
  }
);

export default api;

// services/taskService.js
import api from "./serviceConfig";

// Obtener todas las tareas
export const getAllTasks = async () => {
  try {
    const response = await api.get("/tasks/");
    return response.data;
  } catch (error) {
    throw error;
  }
};

// Obtener una tarea por ID
export const getTaskById = async (id) => {
  try {
    const response = await api.get(`/tasks/${id}`);
    return response.data;
  } catch (error) {
    throw error;
  }
};

// Crear una nueva tarea
export const createTask = async (task) => {
  try {
    const response = await api.post("/tasks/", task);
    return response.data;
  } catch (error) {
    throw error;
  }
};

// Actualizar una tarea existente
export const updateTask = async (id, task) => {
  try {
    const response = await api.put(`/tasks/${id}`, task);
    return response.data;
  } catch (error) {
    throw error;
  }
};

// Eliminar una tarea
export const deleteTask = async (id) => {
  try {
    await api.delete(`/tasks/${id}`);
  } catch (error) {
    throw error;
  }
};

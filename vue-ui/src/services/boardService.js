// services/boardService.js
import api from "./serviceConfig";

// Obtener todas lss tableros
export const getAllBoards = async () => {
  try {
    const response = await api.get("/boards/");
    return response.data;
  } catch (error) {
    throw error;
  }
};

// Obtener un tablero por ID
export const getBoardById = async (id) => {
  try {
    const response = await api.get(`/boards/${id}/`);
    return response.data;
  } catch (error) {
    throw error;
  }
};

// Obtener todas las boards por project_id
export const getBoardsByProjectId = async (projectId) => {
    try {
        const response = await api.get(`/boards/?project=${projectId}`);
        return response.data;
    } catch (error) {
        throw error;
    }
};

// Crear un nuevo tablero
export const createBoard = async (board) => {
  try {
    const response = await api.post("/boards/", board);
    return response.data;
  } catch (error) {
    throw error;
  }
};

// Actualizar un tablero existente
export const updateBoard = async (id, board) => {
  try {
    const response = await api.put(`/boards/${id}/`, board);
    return response.data;
  } catch (error) {
    throw error;
  }
};

// Eliminar una tablero
export const deleteBoard = async (id) => {
  try {
    await api.delete(`/boards/${id}/`);
  } catch (error) {
    throw error;
  }
};

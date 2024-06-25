import api from "./serviceConfig";

export const getTags = async () => {
  try {
    const response = await api.get('/tags/');
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const createTag = async (tag) => {
  try {
    const response = await api.post('/tags/', tag);
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const updateTag = async (id, tag) => {
  try {
    const response = await api.put(`/tags/${id}/`, tag);
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const deleteTag = async (id) => {
  try {
    const response = await api.delete(`/tags/${id}/`);
    return response.data;
  } catch (error) {
    throw error;
  }
};

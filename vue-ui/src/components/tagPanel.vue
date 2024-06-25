<template>
    <div class="tag-panel">
      <h3>Gestionar Etiquetas</h3>
      <form @submit.prevent="saveChanges">
        <div class="mb-3 d-flex align-items-center" v-for="(tag, index) in editableTags" :key="tag.id">
          <input
            type="text"
            class="form-control me-2"
            v-model="tag.tag"
            placeholder="Nombre de la etiqueta"
          />
          <button type="button" class="btn btn-danger" @click="removeTag(index)">Eliminar</button>
        </div>
        <div class="mb-3">
          <button type="button" class="btn btn-secondary" @click="addTag">Agregar Etiqueta</button>
        </div>
        <div class="mb-3">
          <button type="submit" class="btn btn-success">Guardar Cambios</button>
          <button type="button" class="btn btn-secondary" @click="cancelChanges">Cancelar</button>
        </div>
      </form>
    </div>
  </template>
  
<script>
import { createTag, updateTag, deleteTag, getTags } from "../services/tagService";

export default {
  data() {
    return {
      editableTags: [], // Almacena las etiquetas editables
    };
  },
  created() {
    this.loadTags();
  },
  methods: {
    async loadTags() {
      try {
        this.editableTags = await getTags();
      } catch (error) {
        console.error("Error al cargar etiquetas:", error);
      }
    },
    addTag() {
      this.editableTags.push({ id: null, tag: '' });
    },
    async removeTag(index) {
      const tag = this.editableTags[index];
      if (tag.id) {
        try {
          await deleteTag(tag.id); // Elimina la etiqueta de la base de datos
        } catch (error) {
          console.error("Error al eliminar etiqueta:", error);
          return;
        }
      }
      this.editableTags.splice(index, 1); // Elimina la etiqueta de la lista editable
    },
    async saveChanges() {
      try {
        for (let tag of this.editableTags) {
          if (tag.id) {
            await updateTag(tag.id, tag); // Actualiza la etiqueta existente
          } else {
            await createTag(tag); // Crea una nueva etiqueta
          }
        }
        this.$emit('tags-updated'); // Emite un evento para indicar que las etiquetas se han actualizado
        this.$emit('close'); // Emite un evento para cerrar el panel
      } catch (error) {
        console.error("Error al guardar cambios:", error);
      }
    },
    cancelChanges() {
      this.$emit('close'); // Emite un evento para cerrar el panel sin guardar
    }
  }
};
</script>

  
  <style scoped>
  .tag-panel {
    background-color: #fff;
    padding: 1rem;
    border: 1px solid #ddd;
    border-radius: 0.5rem;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    position: fixed;
    top: 20%;
    left: 50%;
    transform: translate(-50%, -20%);
    z-index: 1000;
  }
  
  .me-2 {
    margin-right: 0.5rem;
  }
  </style>
  
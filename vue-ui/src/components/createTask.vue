<!-- CreateTaskComponent.vue -->
<template>
  <div class="container mt-4">
    <h2>Crear Nueva Tarea</h2>
    <form @submit.prevent="submitTask">
      <div class="mb-3">
        <label for="title" class="form-label">Título:</label>
        <input type="text" id="title" class="form-control" v-model="task.title" required />
      </div>

      <div class="mb-3">
        <label for="priority" class="form-label">Prioridad:</label>
        <select id="priority" class="form-select" v-model="task.priority" required>
          <option value="High">High</option>
          <option value="Low">Low</option>
        </select>
      </div>

      <div class="mb-3">
        <label for="description" class="form-label">Descripción:</label>
        <textarea id="description" class="form-control" v-model="task.description"></textarea>
      </div>

      <div class="mb-3">
        <label for="deadline_time" class="form-label">Fecha de Vencimiento:</label>
        <input
          type="datetime-local"
          id="deadline_time"
          class="form-control"
          v-model="task.deadline_time"
        />
      </div>
      <!-- Desplegables de etiquedas -->
      <div class="mb-3">
        <label for="tags" class="form-label">Etiquetas:</label>
        <div class="d-flex">
          <multiselect
            v-model="selectedTags"
            :options="tags"
            :multiple="true"
            :close-on-select="false"
            :clear-on-select="false"
            :preserve-search="true"
            placeholder="Selecciona etiquetas"
            label="tag"
            track-by="id"
            :preselect-first="true"
            class="custom-multiselect flex-grow-1 me-2"
          >
            <template v-slot:tag="{ option, remove }">
              <span class="custom__tag badge bg-primary me-2">
                <span>{{ option.tag }}</span>
                <span class="custom__remove" @click="remove(option)">❌</span>
              </span>
            </template>
            <template v-slot:option="{ option }">
              <div class="custom__option">
                <span>{{ option.tag }}</span>
              </div>
            </template>
          </multiselect>
          <button type="button" class="btn btn-primary" @click="showTagPanel = true">Gestionar</button>
        </div>
      </div>
      
      <TagPanel v-if="showTagPanel" @close="showTagPanel = false" @tags-updated="loadTags" />
      
      <div class="mb-3">
        <label for="refeer_task" class="form-label">Referencia a Tarea:</label>
        <input type="number" id="refeer_task" class="form-control" v-model="task.refeer_task" />
      </div>

      <div class="mb-3">
        <label for="level" class="form-label">Nivel:</label>
        <input type="number" id="level" class="form-control" v-model="task.level" />
      </div>

      <button type="submit" class="btn btn-success">Crear Tarea</button>
    </form>
    <div v-if="error" class="alert alert-danger mt-3">Ocurrió un error: {{ error.message }}</div>
  </div>
</template>

<script>
import Multiselect from 'vue-multiselect'
import TagPanel from './tagPanel.vue'; 
import { createTask } from "../services/taskService";
import { getTags } from "../services/tagService";

export default {
  components: { Multiselect, TagPanel },
  data() {
    return {
      showTagPanel: false,
      task: {
        title: "",
        priority: "Low",
        description: "",
        deadline_time: "",
        tags: [],
        completed: false,
        active: true,
        refeer_task: null,
        level: 0,
      },
      tags: [], // Lista de etiquetas disponibles
      selectedTags: [], // Etiquetas seleccionadas
      error: null,
    };
  },
  created() {
    this.loadTags();
  },
  methods: {
    async loadTags() {
      try {
        this.tags = await getTags();
      } catch (error) {
        console.error("Error al cargar etiquetas:", error);
        this.error = error;
      }
    },
    async submitTask() {
      try {
        // Asigna los IDs de las etiquetas seleccionadas
        this.task.tags = this.selectedTags.map(tag => tag.id);

        // Formatear fecha y hora correctamente para Django
        if (this.task.deadline_time) {
          this.task.deadline_time = new Date(this.task.deadline_time).toISOString();
        }

        await createTask(this.task);
        alert("Tarea creada con éxito");
        this.resetForm();
      } catch (error) {
        this.error = error;
      }
    },
    resetForm() {
      this.task = {
        title: "",
        priority: "Low",
        description: "",
        deadline_time: "",
        tags: [],
        completed: false,
        active: true,
        refeer_task: null,
        level: 0,
      };
      this.selectedTags = [];
      this.error = null;
    }
  }
};
</script>

<style src="../../node_modules/vue-multiselect/dist/vue-multiselect.css"></style>
<style scoped>
.custom-multiselect {
  font-size: 0.875rem; /* Cambia el tamaño de la fuente */
  height: auto; /* Ajusta la altura automáticamente */
}

.custom-multiselect .multiselect__input {
  min-height: 2rem; /* Ajusta la altura mínima del input */
}

.custom__tag {
  font-size: 0.75rem; /* Tamaño de fuente más pequeño para las etiquetas */
  padding: 0.2em 0.4em; /* Ajusta el relleno de las etiquetas */
  margin-right: 0.2em;
  color: #fff;
  background-color: #007bff;
  border-radius: 0.2em;
}

.custom__remove {
  cursor: pointer;
  margin-left: 0.5em;
}

.custom__option {
  padding: 0.25em; /* Reduce el padding de las opciones */
}
</style>

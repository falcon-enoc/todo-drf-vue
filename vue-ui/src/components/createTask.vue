<template>
  <div>
    <div class="task-button-container">
      <button type="button" class="btn-circle" @click="openModal">+</button>
    </div>

    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Crear Nueva Tarea</h5>
          <div class="form-check form-check-inline">
            <label for="auto_fill" class="form-check-label">Autocompletar</label>
            <input type="checkbox" id="auto_fill" class="form-check-input" v-model="autoFill" @change="handleAutoFillChange" />
          </div>
        </div>
        <form @submit.prevent="submitTask">
          <div class="form-row">
            <div class="form-group">
              <label for="title" class="form-label">Título:</label>
              <input type="text" id="title" class="form-control" v-model="task.title" required />
            </div>
            <div class="form-group">
              <label for="priority" class="form-label">Prioridad:</label>
              <select id="priority" class="form-select" v-model="task.priority" required>
                <option value="High">High</option>
                <option value="Low">Low</option>
              </select>
            </div>
          </div>

          <div class="form-group">
            <label for="description" class="form-label">Descripción:</label>
            <textarea id="description" class="form-control" v-model="task.description"></textarea>
          </div>
          
          <div class="form-group">
            <label for="deadline_time" class="form-label">Fecha de Vencimiento:</label>
            <input type="datetime-local" id="deadline_time" class="form-control" v-model="task.deadline_time" />
          </div>
            <div class="form-group">
              <label for="tags" class="form-label">Etiquetas:</label>
              <div class="tags-wrapper">
                <div class="tags-container">
                  <div
                    v-for="tag in tags"
                    :key="tag.id"
                    class="tag-item"
                    :class="{ selected: selectedTags.includes(tag.id) }"
                    @click="toggleSelect(tag.id)"
                  >
                    {{ tag.tag }}
                  </div>
                </div>
                <button type="button" class="btn btn-primary" @click="showTagPanel = true">Gestionar</button>
              </div>
          </div>

          <TagPanel v-if="showTagPanel" @close="showTagPanel = false" @tags-updated="loadTags" />

          <div class="form-row">
            <div class="form-group">
              <label for="refeer_task" class="form-label">Referencia a Tarea:</label>
              <input type="number" id="refeer_task" class="form-control" v-model="task.refeer_task" />
            </div>
            <div class="form-group">
              <label for="level" class="form-label">Nivel:</label>
              <input type="number" id="level" class="form-control" v-model="task.level" />
            </div>
          </div>

          <div class="form-row">
            <button type="button" class="btn btn-secondary" @click="closeModal">Cancelar</button>
            <button type="submit" class="btn btn-success">Crear Tarea</button>
          </div>
        </form>
        <div v-if="error" class="alert alert-danger mt-3">Ocurrió un error: {{ error.message }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue';
import TagPanel from './tagPanel.vue';
import { createTask } from '../services/taskService';
import { getTags } from '../services/tagService';
import { defineEmits } from 'vue';

// Props
const props = defineProps({
boardId: {
  type: Number,
  required: true
}
});

// Emits
const emit = defineEmits(['taskCreated']);

// Refs y reactive
const showModal = ref(false);
const showTagPanel = ref(false);
const autoFill = ref(false);
const error = ref(null);
const selectedTags = ref([]); // Asegúrate de que selectedTags es un array
const tags = ref([]);

const task = reactive({
title: "",
priority: "Low",
description: "",
deadline_time: "",
tags: [],
completed: false,
active: true,
refeer_task: null,
level: 0,
board: props.boardId,
user: 1
});

// Computed
const selectedTagObjects = computed(() => {
return selectedTags.value.map(tagId => tags.value.find(tag => tag.id === tagId));
});

// Funciones
const openModal = () => {
showModal.value = true;
};

const closeModal = () => {
showModal.value = false;
};

const loadTags = async () => {
try {
  tags.value = await getTags();
} catch (error) {
  console.error("Error al cargar etiquetas:", error);
  error.value = error;
}
};

const submitTask = async () => {
try {
  task.tags = selectedTags.value;
  if (task.deadline_time) {
    task.deadline_time = new Date(task.deadline_time).toISOString();
  }
  await createTask(task);
  emit('taskCreated');
  resetForm();
  closeModal();
} catch (error) {
  error.value = error;
}
};

const resetForm = () => {
task.title = "";
task.priority = "Low";
task.description = "";
task.deadline_time = "";
task.tags = [];
task.completed = false;
task.active = true;
task.refeer_task = null;
task.level = 0;
task.board = props.boardId;
task.user = 1;
selectedTags.value = [];
error.value = null;
autoFill.value = false;
};

const handleAutoFillChange = () => {
if (autoFill.value) {
  task.title = "Tarea Ejemplo";
  task.priority = "High";
  task.description = "Descripción de ejemplo";
  task.deadline_time = new Date().toISOString().slice(0, 16);
  task.level = 1;
} else {
  task.title = "";
  task.priority = "Low";
  task.description = "";
  task.deadline_time = "";
  task.level = 0;
}
};

const toggleSelect = (tagId) => {
const index = selectedTags.value.indexOf(tagId);
if (index === -1) {
  selectedTags.value.push(tagId);
} else {
  selectedTags.value.splice(index, 1);
}
};

// Lifecycle
onMounted(() => {
loadTags();
});
</script>

<style scoped>
.modal {
  display: block;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: hidden; /* Asegúrate de que el modal no tenga desplazamiento */
  background-color: rgba(0, 0, 0, 0.5);
  color: var(--text-color);
}

.modal-content {
  background-color: var(--primary-color);
  margin: 5% auto; /* Ajusta esta propiedad para cambiar la altura desde la parte superior */
  padding: 20px;
  border: 1px solid var(--secondary-color);
  width: 100%;
  max-width: 600px;
  min-width: 300px;
  color: var(--text-color);
  overflow: hidden; /* Asegúrate de que el contenido del modal no tenga desplazamiento */
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.task-button-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.btn-circle {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  background-color: var(--buttons-color);
  color: white;
  border: none;
  outline: none;
  cursor: pointer;
}

.btn-circle:hover {
  background-color: #0056b3;
}

.form-row {
  display: flex;
  justify-content: right;
  gap: 10px;
  margin-bottom: 15px;
}

.form-group {
  flex: 1;
  margin-bottom: 10px;
}

.form-check {
  margin-left: 15px;
}

.form-label {
  color: var(--text-color);
}

.form-control, .form-select {
  background-color: var(--secondary-color);
  color: var(--text-color);
  border: 1px solid var(--primary-color);
}

.btn-success {
  background-color: var(--buttons-color);
  border-color: var(--buttons-color);
  margin-right: 2em;
}

.btn-success:hover {
  background-color: #0056b3;
  border-color: #0056b3;
}

.btn-primary{
  background-color: var(--buttons-color);
  border-color: var(--buttons-color);
}
.btn-primary:hover {
  background-color: #0056b3;
  border-color: #0056b3;
}

.btn-secondary {
  background-color: var(--secondary-color);
  border-color: var(--secondary-color);
}

.btn-secondary:hover {
  background-color: rgb(176, 52, 52);
  border-color: var(--primary-color);
}

.tags-wrapper {
  display: flex;
  align-items: flex-start; /* Alinea el botón Gestionar con el inicio de las etiquetas */
}

.tags-container {
  display: flex;
  flex-wrap: wrap;
  background-color: var(--secondary-color);
  border-radius: 10px;
  max-height: 6em; /* Ajusta esta altura para que sea apropiada para dos filas de etiquetas */
  overflow-x: hidden;
  height: 4em;
  width: calc(100% - 100px); /* Ajusta el ancho para dejar espacio para el botón Gestionar */
  padding: 5px;
  box-sizing: border-box;
  white-space: normal; /* Permite el ajuste de las etiquetas */
  margin-right: 10px; /* Espacio entre el contenedor de etiquetas y el botón */
}

.tag-item {
  padding: 5px 8px;
  cursor: pointer;
  border: 1px solid var(--primary-color);
  background-color: var(--secondary-color);
  color: var(--text-color);
  border-radius: 10px;
  user-select: none;
  margin-right: 5px; /* Añade espacio entre etiquetas */
  margin-bottom: 5px; /* Añade espacio entre filas */
}

.tag-item.selected {
  background-color: var(--buttons-color);
  color: var(--text-color);
}

.btn-primary {
  margin-top: 5px; /* Ajusta la separación superior del botón */
}
</style>

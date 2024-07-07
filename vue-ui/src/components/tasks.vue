<!-- TaskComponent.vue -->
<template>
  <div class="container mt-4">
    <button class="btn btn-primary mb-3" @click="loadTasks">Cargar Tareas</button>
    <div class="row">
      <div v-for="task in tasks" :key="task.id" class="col-md-4 mb-4">
        <div class="card h-100">
          <div class="card-header">
            <h5 class="card-title">{{ task.title }}</h5>
          </div>
          <div class="card-body">
            <p class="card-text"><strong>ID:</strong> {{ task.id }}</p>
            <p class="card-text">{{ task.description }}</p>
            <p class="card-text"><strong>Prioridad:</strong> {{ task.priority }}</p>
            <p class="card-text"><strong>Fecha Límite:</strong> {{ task.deadline_time }}</p>
          </div>
        </div>
      </div>
    </div>
    <div v-if="error" class="alert alert-danger mt-3">Ocurrió un error: {{ error.message }}</div>
  </div>
</template>

<script>
import { getAllTasks } from "../services/taskService";

export default {
  data() {
    return {
      tasks: [],
      error: null,
    };
  },
  methods: {
    async loadTasks() {
      try {
        this.tasks = await getAllTasks();
        // this.sortTasksById();
      } catch (error) {
        this.error = error;
      }
    },
    sortTasksById() {
      this.tasks.sort((a, b) => a.id - b.id);
    },
  },
};
</script>

<style scoped>
.card-header {
  background-color: var(--buttons-color);
  color: white;
}

.btn-primary {
  background-color: var(--buttons-color);
  border-color: var(--buttons-color);
}

.btn-primary:hover, .btn-primary:focus, .btn-primary:active {
  background-color: darken(var(--buttons-color), 10%);
  border-color: darken(var(--buttons-color), 10%);
}

.btn-primary:focus {
  box-shadow: none;
}
</style>

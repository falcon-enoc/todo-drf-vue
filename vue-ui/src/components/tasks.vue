<!-- TaskComponent.vue -->
<template>
  <div class="container">
    <button @click="loadTasks">Cargar Tareas</button>
    <ul>
      <li v-for="task in tasks" :key="task.id">
        <div class="card">
          <div class="card-header">
            <h3>{{ task.title }}</h3>
          </div>
          <div class="card-body">
            <p>ID: {{ task.id }}</p>
            <p>{{ task.description }}</p>
            <p>Prioridad: {{ task.priority }}</p>
            <p>Deadline: {{ task.deadline_time }}</p>
          </div>
        </div>
      </li>
    </ul>
    <div v-if="error">Ocurrió un error: {{ error.message }}</div>
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
.container {
  width: 40%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 16px;
}
.container li {
  list-style: none;
}
.card {
  border: 1px solid #444;
  border-radius: 4px;
  margin: 16px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.card-header {
  font-weight: bold;
  margin-bottom: 8px;
  border-radius: 3px 3px 0px 0px;
  background-color: #444;
  text-align: center;
  color: whitesmoke;
}
.card-body {
  font-size: 14px;
  margin: 1em;
  color: #111;
}
</style>

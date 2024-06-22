<!-- TaskComponent.vue -->
<template>
  <div>
    <button @click="loadTasks">Cargar Tareas</button>
    <ul>
      <li v-for="task in tasks" :key="task.id">{{ task.title }}</li>
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
      } catch (error) {
        this.error = error;
      }
    },
  },
};
</script>

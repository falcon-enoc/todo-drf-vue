<!-- CreateTaskComponent.vue -->
<template>
  <div>
    <h2>Crear Nueva Tarea</h2>
    <form @submit.prevent="submitTask">
      <div>
        <label for="title">Título:</label>
        <input type="text" id="title" v-model="task.title" required />
      </div>

      <div>
        <label for="priority">Prioridad:</label>
        <select id="priority" v-model="task.priority" required>
          <option value="High">High</option>
          <option value="Low">Low</option>
        </select>
      </div>

      <div>
        <label for="description">Descripción:</label>
        <textarea id="description" v-model="task.description"></textarea>
      </div>

      <div>
        <label for="deadline_time">Fecha de Vencimiento:</label>
        <input
          type="datetime-local"
          id="deadline_time"
          v-model="task.deadline_time"
        />
      </div>

      <div>
        <label for="tags">Etiquetas:</label>
        <input type="text" id="tags" v-model="tagsInput" @input="updateTags" />
        <small>Separar etiquetas con comas.</small>
      </div>

      <div>
        <label for="refeer_task">Referencia a Tarea:</label>
        <input type="number" id="refeer_task" v-model="task.refeer_task" />
        <small>Ingresa el ID de la tarea a la que se refiere, si aplica.</small>
      </div>

      <div>
        <label for="level">Nivel:</label>
        <input type="number" id="level" v-model="task.level" />
      </div>

      <button type="submit">Crear Tarea</button>
    </form>
    <div v-if="error">Ocurrió un error: {{ error.message }}</div>
  </div>
</template>

<script>
import { createTask } from "../services/taskService";

export default {
  data() {
    return {
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
      tagsInput: "",
      error: null,
    };
  },
  methods: {
    async submitTask() {
      try {
        this.task.tags = this.tagsInput.split(",").map((tag) => tag.trim());

        // Formatear fecha y hora correctamente para Django
        if (this.task.deadline_time) {
          this.task.deadline_time = new Date(
            this.task.deadline_time
          ).toISOString();
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
        related_tasks: [],
        level: 0,
        assignments: [],
      };
      this.tagsInput = "";
      this.error = null;
    },
    updateTags() {
      this.task.tags = this.tagsInput.split(",").map((tag) => tag.trim());
    },
  },
};
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
}

form > div {
  margin-bottom: 10px;
}

button {
  width: 150px;
  padding: 10px;
  background-color: #4caf50;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}
</style>

<!-- CreateTaskComponent.vue -->
<template>
  <div>
    <!-- Botón que abre el modal -->
    <!-- <button type="button" class="btn btn-primary card" @click="openModal">Crear Nueva Tarea</button> -->
    <div class="task-button-container">
      <button type="button" class="btn-circle" @click="openModal">+</button>
    </div>

    <!-- Modal del formulario -->
    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <span class="close" @click="closeModal">&times;</span>
        <h5 class="modal-title">Crear Nueva Tarea</h5>
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
            <input type="datetime-local" id="deadline_time" class="form-control" v-model="task.deadline_time" />
          </div>

          <!-- Desplegables de etiquetas -->
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
    </div>
  </div>
</template>

<script>
import Multiselect from 'vue-multiselect'
import TagPanel from './tagPanel.vue'; 
import { createTask } from "../services/taskService";
import { getTags } from "../services/tagService";

export default {
  components: { Multiselect, TagPanel },
  props: {
    boardId: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      showModal: false, // Estado para mostrar u ocultar el modal
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
        board: this.boardId // Utiliza la prop para asignar el board
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
    openModal() {
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    },
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
        this.$emit('taskCreated'); // Emitir el evento con los datos de la tarea creada
        // alert("Tarea creada con éxito");
        this.resetForm();
        this.closeModal(); // Cierra el modal después de crear la tarea
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
        board: this.boardId // Resetea el board al valor de la prop
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

.modal {
  display: block;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.5);
  color: black;
}

.modal-content {
  background-color: #fefefe;
  margin: 15% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
}

.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}

.task-button-container {
  display: flex;
  justify-content: center;
  margin-top: 20px; /* Ajusta según sea necesario */
}


.btn-circle {
            width: 50px; /* Ajusta el tamaño según tus necesidades */
            height: 50px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px; /* Tamaño del símbolo + */
            background-color: #007bff;
            color: white;
            border: none;
            outline: none;
            cursor: pointer;
        }

.btn-circle:hover {
    background-color: #0056b3;
}

</style>

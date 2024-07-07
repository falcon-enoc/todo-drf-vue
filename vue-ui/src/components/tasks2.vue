<template>
    <div class="container">
        <div class="btn-create-card">
            <CreateTasks 
                    @taskCreated="loadTasks"
                    :boardId="boardId"/>
        </div>
        <div class="card" v-for="(task, taskIndex) in tasks" :key="taskIndex" @click="openModal(task)">
            {{ task.id }} , {{ task.title }}
        </div>
        <div v-if="isModalOpen" class="modal">
            <div class="modal-content">
                <span class="close-btn" @click="closeModal">&times;</span>
                <!-- <p>{{ modalContent }}</p> -->
            </div>
        </div>
    </div>
</template>

<script setup>
import CreateTasks from './createTask.vue';
import { ref, onMounted, watch } from 'vue';
import { getTaskByBoardId } from "../services/taskService";

const props = defineProps({
    boardId: {
        type: Number,
        required: true
    }
});

const isModalOpen = ref(false);
const modalContent = ref('');
const tasks = ref([]);
const error = ref(null);

const openModal = (task) => {
    modalContent.value = `ID: ${task.id}\nTitle: ${task.title}`;
    isModalOpen.value = true;
}

const closeModal = () => {
    isModalOpen.value = false;
    modalContent.value = '';
}

const loadTasks = async () => {
    try {
        tasks.value = await getTaskByBoardId(props.boardId);
        sortTasksById();
    } catch (err) {
        error.value = err;
    }
}

const sortTasksById = () => {
    tasks.value.sort((a, b) => a.id - b.id);
}

onMounted(() => {
    loadTasks();
});

watch(() => props.boardId, (newBoardId) => {
    loadTasks();
});

</script>

<style scoped>
.card {
    height: 50px;
    width: 100%; /* Ocupa todo el ancho disponible dentro del tablero */
    background-color: var(--secondary-color);
    color: whitesmoke;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 10px;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    cursor: pointer;
}

.modal {
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgba(0, 0, 0, 0.4);
}

.modal-content {
    background-color: #fefefe;
    margin: 15% auto;
    padding: 20px;
    border: 1px solid #888;
    width: 80%;
    max-width: 600px;
    border-radius: 5px;
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}

.close-btn {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
    cursor: pointer;
}

.close-btn:hover,
.close-btn:focus {
    color: black;
    text-decoration: none;
    cursor: pointer;
}
</style>

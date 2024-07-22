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
                <div class="task-details">
                    <p><strong>ID:</strong> {{ modalContent.id }}</p>
                    <p><strong>Title:</strong> {{ modalContent.title }}</p>
                    <p><strong>Priority:</strong> {{ modalContent.priority }}</p>
                    <p><strong>Completed:</strong> {{ modalContent.completed }}</p>
                    <p><strong>Active:</strong> {{ modalContent.active }}</p>
                    <p><strong>Description:</strong> {{ modalContent.description }}</p>
                    <p><strong>Created At:</strong> {{ modalContent.created_at }}</p>
                    <p><strong>Updated At:</strong> {{ modalContent.updated_at }}</p>
                    <p><strong>Deadline Time:</strong> {{ modalContent.deadline_time }}</p>
                    <p><strong>Tags:</strong>
                        <span v-for="tag in modalContent.tags" :key="tag.id" class="tag-badge">{{ tag.tag }}</span>
                    </p>
                    <p><strong>Referrer Task:</strong> {{ modalContent.refeer_task?.title }}</p>
                    <p><strong>Level:</strong> {{ modalContent.level }}</p>
                    <p><strong>Board:</strong> {{ modalContent.board }}</p>
                    <p><strong>User:</strong> {{ modalContent.user }}</p>
                </div>

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
const modalContent = ref(null);
const tasks = ref([]);
const error = ref(null);

const openModal = (task) => {
    console.log(task);
    modalContent.value = { 
        id: task.id,
        title: task.title,
        priority: task.priority,
        completed: task.completed,
        active: task.active,
        description: task.description,
        created_at: task.created_at,
        updated_at: task.updated_at,
        deadline_time: task.deadline_time,
        tags: task.tags.map(tag => ({ id: tag.id, tag: tag.tag })),
        refeer_task: task.refeer_task ? { id: task.refeer_task.id, title: task.refeer_task.title } : null,
        level: task.level,
        board: task.board,
        user: task.user
    };
    
    isModalOpen.value = true;
}

const closeModal = () => {
    isModalOpen.value = false;
    modalContent.value = null;
}

const loadTasks = async () => {
    try {
        tasks.value = await getTaskByBoardId(props.boardId);
        console.log(task.value);
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

watch(() => props.boardId, () => {
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
    background-color: rgba(0, 0, 0, 0.4);
}

.modal-content {
    background-color: var(--primary-color);
    margin: 5% auto; /* Ajusta esta propiedad para cambiar la altura desde la parte superior */
    padding: 20px;
    border: 1px solid var(--secondary-color);
    width: 80%;
    max-width: 600px;
    min-width: 300px;
    border-radius: 5px;
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
    color: var(--text-color);
}

.task-details p {
    margin: 5px 0;
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

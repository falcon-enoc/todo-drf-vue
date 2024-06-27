<!-- componets/board.vue -->
<template>
    <button @click="addItem">Agregar Elemento</button>
    <div class="grid-container">
        <div class="tablero" v-for="(item, index) in items" :key="item.id">
            <div class="elemento">
                {{ item.name }}
                <button @click="openEditModal(item.id)">Editar</button>
                <CreateTasks 
                @taskCreated="fetchBoards"
                :boardId="item.id"/>
            </div>
            <button class="delete-btn" @click="removeItemAt(index)">X</button>
            <Tasks2 :boardId="item.id" />
        </div>
    </div>

    <div v-if="showModal" class="modal">
        <div class="modal-content">
            <span class="close" @click="closeModal">&times;</span>

            <h2>Edit Board</h2>

            <form @submit.prevent="editBoard">
                <div>
                    <label for="title">Title:</label>
                    <input id="title" v-model="board.title" required />
                </div>
                <div>
                    <label for="deadline">Deadline:</label>
                    <input id="deadline" type="datetime-local" v-model="board.deadline_time" />
                </div>
                <div>
                    <label for="project">Project ID:</label>
                    <input id="project" v-model="board.project" required />
                </div>
                <button type="submit">Save</button>
            </form>

            <p v-if="message">{{ message }}</p>
        </div>
    </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue';
import Tasks2 from './tasks2.vue';
import CreateTasks from './createTask.vue';
import { createBoard, deleteBoard, getBoardById, updateBoard, getBoardsByProjectId } from '../services/boardService';

const items = ref([]); // Lista inicial de elementos
const nextId = ref(1); // Variable para llevar el control del próximo ID
const projectId = 1; // ID del proyecto
const editingBoardId = ref(null); // Variable para almacenar el ID del board que se está editando

// Variables para el modal de edición
const showModal = ref(false);
const board = reactive({
    title: '',
    deadline_time: '',
    project: ''
});
const message = ref('');

const addItem = async () => {
    const newBoard = {
        title: `Board ${nextId.value}`,
        description: `Description for board ${nextId.value}`,
        project: projectId,
    };

    try {
        const createdBoard = await createBoard(newBoard);
        const newItem = {
            id: createdBoard.id,
            name: createdBoard.title
        };
        items.value.push(newItem);
        nextId.value++;
    } catch (error) {
        console.error('Error creating board:', error);
        alert('Failed to create board.');
    }
};

const removeItemAt = async (index) => {
    try {
        const boardId = items.value[index].id;
        await deleteBoard(boardId);
        items.value.splice(index, 1);
        alert('Board deleted successfully!');
    } catch (error) {
        console.error('Error deleting board:', error);
        alert('Failed to delete board.');
    }
};

const fetchBoards = async () => {
    try {
        console.log('fetchBoards llamado'); // Agregar este log
        const response = await getBoardsByProjectId(projectId);
        items.value = response.map(board => ({
            id: board.id,
            name: board.title
        }));
        nextId.value = response.length + 1;
    } catch (error) {
        console.error('Error fetching boards:', error);
    }
};

const openEditModal = async (boardId) => {
    editingBoardId.value = boardId;
    try {
        const data = await getBoardById(boardId);
        board.title = data.title;
        board.deadline_time = data.deadline_time;
        board.project = data.project;
        showModal.value = true;
    } catch (error) {
        console.error('Error fetching board details:', error);
        message.value = 'Error fetching board details.';
    }
};

const editBoard = async () => {
    try {
        await updateBoard(editingBoardId.value, board);
        message.value = 'Board successfully updated.';
        showModal.value = false;
        fetchBoards(); // Refresh the list of boards
    } catch (error) {
        console.error('Error updating board:', error);
        message.value = 'Error updating the board. Please try again.';
    }
};

const closeModal = () => {
    showModal.value = false;
};

onMounted(() => {
    fetchBoards();
});

</script>

<style scoped>
.grid-container {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    /* Fuerza 4 columnas en la grilla */
    grid-auto-flow: row;
    justify-content: center;
    overflow-x: auto;
    gap: 10px;
    padding: 10px;
    max-width: 100%;
}

.tablero {
    background-color: #0F1204;
    border: 1px solid #0F1204;
    padding: 20px;
    min-width: 300px;
    /* Ancho mínimo más pequeño para permitir 4 elementos */
    max-width: 600px;
    /* Ancho máximo para los tableros */
    min-height: 500px;
    /* Altura mínima para los tableros */
    max-height: 800px;
    /* Altura máxima para los tableros */
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    align-items: center;
    border-radius: 7px;
}

.elemento {
    font-size: 1.2em;
    width: auto;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    color: aliceblue;
}

button {
    padding: 10px 20px;
    cursor: pointer;
    margin-top: 10px;
}

.delete-btn {
    background-color: red;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 5px 10px;
    cursor: pointer;
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

form {
    display: flex;
    flex-direction: column;
}

form>div {
    margin-bottom: 10px;
}

label {
    margin-bottom: 5px;
}

input {
    padding: 8px;
    font-size: 14px;
}

button {
    padding: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
</style>
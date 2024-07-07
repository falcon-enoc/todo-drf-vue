<!-- src/components/board.vue -->
<template>
    <button class="btn-add-board" @click="addItem">Agregar Elemento</button>
    <div class="grid-container">
        <div class="tablero" v-for="(item, index) in items" :key="item.id">
            <div class="elemento"> <!-- header elemento -->
                <p class="titulo">
                    {{ item.name }}
                </p>
                <div class="iconos">
                    <button class="edit-icon" @click="openEditModal(item.id)">
                        <img src="../assets/edit-1.svg" alt="Edit" width="24" height="24">
                    </button>
                    <button class="delete-icon" @click="removeItemAt(index)">
                        <img src="../assets/delete-1.svg" alt="Delete" width="24" height="24">
                    </button>
                </div>
            </div>
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
        items.value.unshift(newItem); // Agregar al inicio de la lista
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
    display: flex;
    flex-direction: row;
    gap: 20px;
    padding: 10px;
    max-width: 100%;
    overflow-x: auto;
}

.tablero {
    background-color: var(--primary-color);
    min-width: 300px;
    max-width: 600px;
    min-height: 500px;
    max-height: 800px;
    display: flex;
    flex-direction: column;
    align-items: center;
    border-radius: 7px;
    box-shadow: 5px 3px 9px rgba(1, 1, 1, 0.4); /* Sombra agregada */
}

.elemento {
    margin-top: 10px;
    color: aliceblue;
    display: grid;
    grid-template-columns: 1fr auto;
    align-items: center;
    /* gap: 10px; */
    /* padding: 0 10px; */
    /* padding-inline: 10px; */
    padding-left: 10px;
    width: 100%;
}

.titulo {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis; /* clip */
    margin: 0;
    margin-top: 0.4rem;
    font-size: 1.2em;
}

.iconos {
    display: flex;
    /* gap: 10px; */
}

.iconos button {
    background-color: transparent;
    border: none;
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

form > div {
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
    color: white;
    border: none;
    cursor: pointer;
}

.btn-add-board {
    background-color: var(--buttons-color);
}

button:hover {
    background-color: #0056b3;
    border-radius: 4px;
}
</style>

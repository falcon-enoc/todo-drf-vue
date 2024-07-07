<template>
  <div class="main">
    <!-- <CreateTask /> -->
    <Board />
    <!-- <Tasks /> -->
  </div>
</template>

<script setup>
import MyComponent from "../components/MyComponent.vue";
// import Tasks from "../components/tasks.vue";
// import CreateTask from "../components/createTask.vue";
import Board from "../components/board.vue";
</script>

<style setup>
.main {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  list-style: none;
}
</style>

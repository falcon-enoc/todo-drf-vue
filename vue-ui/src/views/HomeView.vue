<template>
  <div>
    <h1>Home View</h1>
    <MyComponent message="Welcome to the Home Page!"></MyComponent>
    <Tasks />
    <CreateTask />
  </div>
</template>

<script setup>
import MyComponent from "../components/MyComponent.vue";
import Tasks from "../components/tasks.vue";
import CreateTask from "../components/createTask.vue";
</script>

<template>
  <div class="main">
    <Board />
  </div>
</template>

<script setup>
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

<template>
  <div>
    <p>{{ message }}</p>
  </div>
</template>

<script setup>
const props = defineProps({
  message: String,
});
</script>

<style scoped>
p {
  font-size: 1.2em;
  color: #333;
}
</style>

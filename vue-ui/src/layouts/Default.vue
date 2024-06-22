<template>
  <div>
    <Header />

    <main>
      <slot></slot>
    </main>

    <footer>
      <p>© 2024 Vue Example</p>
    </footer>
  </div>
</template>

<script setup>
import Header from "../components/header.vue";
</script>

<style scoped>
header {
  background: #333;
  color: #fff;
  padding: 10px;
}

footer {
  background: #333;
  color: #fff;
  text-align: center;
  padding: 10px;
  position: fixed;
  bottom: 0;
  width: 100%;
  box-sizing: border-box;
}
</style>

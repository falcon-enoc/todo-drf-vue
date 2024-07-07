<template>
  <div>
    <!-- <Header /> -->

    <main class="content">
      <slot></slot>
    </main>
    
    <Footer />
  </div>
</template>

<script setup>
import Header from "../components/header.vue";
import Footer from "../components/footer.vue";
</script>

<style scoped>
.content {
  padding-bottom: 5rem; /* Asegura espacio para el footer */
}
</style>

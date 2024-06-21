<template>
  <div>
    <header>
      <nav>
        <router-link to="/">Home</router-link> |
        <router-link to="/about">About</router-link>
      </nav>
    </header>
    <main>
      <slot></slot>
    </main>
    <footer>
      <p>© 2024 Vue Example</p>
    </footer>
  </div>
</template>

<script setup></script>

<style>
header {
  background: #333;
  color: #fff;
  padding: 10px;
}
nav a {
  color: #fff;
  margin: 0 10px;
  text-decoration: none;
}
footer {
  background: #333;
  color: #fff;
  text-align: center;
  padding: 10px;
}
</style>

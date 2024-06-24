<template>
  <header class="header">
    <div class="logo">Mi Logo</div>
    <nav class="nav">
      <ul class="nav-list">
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/about">About</router-link></li>
        <li><a href="#">Servicios</a></li>
        <li><a href="#">Contacto</a></li>
      </ul>
    </nav>
    <div class="menu-toggle" id="mobile-menu">
      <span class="bar"></span>
      <span class="bar"></span>
      <span class="bar"></span>
    </div>
  </header>
</template>

<script setup></script>

<style setup>
/* styles.css */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, sans-serif;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: #333;
  color: #fff;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.nav {
  display: flex;
}

.nav-list {
  display: flex;
  list-style: none;
}

.nav-list li {
  margin: 0 1rem;
}

.nav-list a {
  color: #fff;
  text-decoration: none;
  font-weight: bold;
}

.menu-toggle {
  display: none;
  flex-direction: column;
  cursor: pointer;
}

.menu-toggle .bar {
  width: 25px;
  height: 3px;
  background-color: #fff;
  margin: 4px 0;
}

/* Responsivo */
@media (max-width: 768px) {
  .nav {
    display: none;
  }
  .menu-toggle {
    display: flex;
  }
}

@media (max-width: 768px) {
  .nav-list {
    flex-direction: column;
    position: absolute;
    top: 60px;
    left: 0;
    width: 100%;
    background-color: #333;
  }
  .nav-list li {
    margin: 1rem 0;
    text-align: center;
  }
  .nav-list a {
    display: block;
    width: 100%;
    padding: 1rem;
  }
}

.nav.active {
  display: flex !important;
}
</style>

<template>
  <div id="app">
    <div id="nav">
      <img class="logo" alt="logo" src="./assets/logo/Logo.png" width="50" height="50">
      <b-row>
        <b-col>
          <router-link to="/">Home</router-link>
          <router-link to="/dashboard">Dashboard</router-link>
          <router-link to="/about">About</router-link>
        </b-col>
      </b-row>
    </div>
    <br/>
    <router-view />
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
img {
  margin: 0px;
  padding: 0px;
  position: absolute;
  top: 0;
}
#nav {
  padding: 0px 10px 30px 10px;
  top: 10;
}
#nav a {
  font-weight: bold;
  color: #2c3e50;
  padding: 0 15px;
}
#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

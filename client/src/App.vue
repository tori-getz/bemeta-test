<template>
  <div id="app" v-if="loaded">
    <router-view />
  </div>
  <h1 v-else> Loading... </h1>
</template>

<script>
export default {
  name: 'App',
  computed: {
    loaded () {
      return this.$store.getters.LOADED;
    }
  },
  mounted () {
    this.$store.dispatch("GET_DOCTORS")
  }
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
</style>

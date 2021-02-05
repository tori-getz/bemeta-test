<template>
  <div id="app">
    <ViewDoctor :photo="photo" :name="name" :methods="methods" />
  </div>
</template>

<script>
import ViewDoctor from './components/ViewDoctor.vue'
import Axios from "axios"

export default {
  name: 'App',
  data: () => {
    return {
      name: "",
      photo: "",
      methods: []
    }
  },
  created: () => {
    Axios.
      get('http://localhost:5000/doctors/recvKqu0DhZ1fBG1h')
      .then(res => {
        console.log(res.data);
        this.name = res.data.fields["Имя"];
        this.methods = res.data.fields["Методы"];
        this.photo = res.data.fields["Фотография"][0].url;
      });
  },
  components: {
    ViewDoctor
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

<template>
  <div id="app">
    <img src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <app-container></app-container>
    <app-collaboration></app-collaboration>
    <app-environment></app-environment>
    <app-foundation></app-foundation>
    <app-source></app-source>


  </div>

</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import AppContainer from './components/AppContainer.vue'
import Collaboration from './components/Collaboration.vue'
import Environment from './components/Environment.vue'
import Foundation from './components/Foundation.vue'
import Source from './components/Source.vue'

import axios from 'axios';

export default {
  name: 'app',

  components: {
    HelloWorld,
    'app-container' : AppContainer,
    'app-collaboration' : Collaboration,
    'app-environment' : Environment,
    'app-foundation' : Foundation,
    'app-source' : Source
  },

  data(){
    return{
      list: []
    }
  },

  mounted(){
    var vueScope = this;
    axios.get('/example1.json')
    .then(function (response) {
      vueScope.list = response.data;
    })
    .catch(function (error) {
      console.log(error);
    });
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

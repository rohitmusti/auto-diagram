<template>
  <div id="app">
    <img src="./assets/logo.png">
    <app-collaboration :collaborationTools="collab_list"></app-collaboration>
    <app-environment :environments="env_list"></app-environment>
    <app-foundation :foundations="found_list"></app-foundation>
    <app-source :sourceControls="source_list"></app-source>


  </div>

</template>

<script>
import Collaboration from './components/Collaboration.vue'
import Environment from './components/Environment.vue'
import Foundation from './components/Foundation.vue'
import Source from './components/Source.vue'

import axios from 'axios';

export default {
  name: 'app',

  components: {
    'app-collaboration' : Collaboration,
    'app-environment' : Environment,
    'app-foundation' : Foundation,
    'app-source' : Source
  },

  data(){
    return{
      list: [],
      collab_list: [],
      env_list: [],
      found_list: [],
      source_list: []
    }
  },

  mounted(){
    var vueScope = this;
    axios.get('/example1.json')
    .then(function (response) {
      vueScope.list = response.data;
      vueScope.collab_list = response.data.collaborationTools;
      vueScope.env_list = response.data.environments;
      vueScope.found_list = response.data.hosting;
      vueScope.source_list = response.data.sourceControl;


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

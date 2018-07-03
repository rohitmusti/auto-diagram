<template>
  <!-- <div id="collaboration-app">
    <collaboration-tag
      v-for="item in list"
      v-bind:struct="item"
      v-bind:key="item.id">
    </collaboration-tag>
  </div> -->

  <div id="app">
    <img src="./assets/rhlabs.png">
    <div class="organization">
        <!-- <h1>Organization</h1> -->
        <p>{{ input_data.organization[0] }}</p>
    </div>

    <!-- <h1>Collaborations</h1> -->
    <app-collaboration
      v-for="item in input_data.collaborationTools"
      v-bind:struct="item">
    </app-collaboration>

    <!-- <h1>Environments</h1> -->
    <app-environment :applications="input_data.appContainers"
      v-for="item in input_data.environments"
      v-bind:struct="item">
    </app-environment>



    <!-- <h1>Source</h1> -->
    <app-source
      v-for="item in input_data.sourceControl"
      v-bind:struct="item">
    </app-source>

    <!-- <h1>Testing</h1> -->
    <app-test
      v-for="item in input_data.testLibraries"
      v-bind:struct="item">
    </app-test>

    <!-- <h1>Hosting</h1> -->
    <div class="hosting-wrapper">
        <app-hosting
          v-for="item in input_data.hosting"
          v-bind:struct="item">
        </app-hosting>
    </div>




  </div>

</template>

<script>
import Collaboration from './components/Collaboration.vue'
import Environment from './components/Environment.vue'
import Hosting from './components/Hosting.vue'
import Source from './components/Source.vue'
import Test from './components/Test.vue'


import axios from 'axios';

export default {
  name: 'app',

  components: {
    'app-collaboration' : Collaboration,
    'app-environment' : Environment,
    'app-hosting' : Hosting,
    'app-source' : Source,
    'app-test': Test
  },

  data(){
    return{
      input_data: [],
    }
  },

  mounted(){
    var vueScope = this;
    axios.get('/example1.json')
    .then(function (response) {
      vueScope.input_data = response.data;
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

<template>
  <!-- <div id="collaboration-app">
    <collaboration-tag
      v-for="item in list"
      v-bind:struct="item"
      v-bind:key="item.id">
    </collaboration-tag>
  </div> -->

  <div id="app">
      <div class="logo">
          <img src="./assets/rhlabs.png">
      </div>
    <div class="organization-wrapper">
        <div class="organization">
            <p>{{ input_data.organization[0] }}</p>
        </div>
    </div>

    <div class="collaboration-wrapper">
        <app-collaboration
          v-for="item in input_data.collaborationTools"
          v-bind:struct="item">
        </app-collaboration>
    </div>

    <div class="environment-wrapper">
        <app-environment :applications="input_data.appContainers"
          v-for="item in input_data.environments"
          v-bind:struct="item">
        </app-environment>
    </div>

    <div class="source-wrapper">
        <app-source
          v-for="item in input_data.sourceControl"
          v-bind:struct="item">
        </app-source>
    </div>

    <div class="test-wrapper">
        <app-test
          v-for="item in input_data.testLibraries"
          v-bind:struct="item">
        </app-test>
    </div>

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
    axios.get('/example.json')
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
    display: grid;
    grid-template-columns: repeat( 5, 1fr);
    grid-template-rows: repeat( 7, 1fr);
    grid-gap: 10px;
    grid-template-areas:
    "l o o o o"
    "t e e e e"
    "t e e e e"
    "t e e e e"
    "s s s s c"
    "h h h h h";
}

* {
    padding: 5px;
}

.organization-wrapper {
    background-color: #d63031;
    grid-area: o;
    display: grid;
    grid-column: 1fr 1fr;
    grid-row: 1fr;
}

.organization {
    background-color: #ff7675;
    margin: 5px;
    padding: 3px;

}

.hosting-wrapper {
    background-color: #d63031;
    grid-area: h;
    display: grid;
    grid-row: repeat(2, 1fr);
}


.environment-wrapper {
    grid-area: e;
    display: grid;
    grid-row: repeat(3, 1fr);
}

.collaboration-wrapper {
    background-color: #00b894;
    grid-area: c;
    display: grid;
    grid-row: repeat(2, 1fr);
}

.test-wrapper {
    background-color: #6c5ce7;
    grid-area: t;
    display: grid;
    grid-row: repeat(2, 1fr);

}

.source-wrapper {
    background-color: #fdcb6e;
    grid-area: s;
    display: grid;
    grid-row: repeat(1, 1fr);
}

</style>

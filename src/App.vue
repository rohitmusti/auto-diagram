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
            <p>{{ organization }}</p>
        </div>
    </div>

    <div class="collaboration-wrapper">
        <app-collaboration
          v-for="item in input_data.stack.collaborationTools" :class="item.icon"
          v-bind:struct="item">
        </app-collaboration>
    </div>

    <div class="environment-wrapper">
        <app-environment :applications="input_data.stack.appContainers"
          v-for="item in input_data.stack.environments"
          v-bind:struct="item">
        </app-environment>
    </div>

    <div class="source-wrapper">
        <app-source
          v-for="item in input_data.stack.sourceControl" :class="item.icon"
          v-bind:struct="item">
        </app-source>
    </div>

    <div class="test-wrapper">
        <app-test
          v-for="item in input_data.stack.testLibraries" :class="item.icon"
          v-bind:struct="item">
        </app-test>
    </div>

    <div class="hosting-wrapper">
        <app-hosting
          v-for="item in input_data.stack.hosting" :class="item.icon"
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
      organization: ""
    }
  },

  mounted(){
    var vueScope = this;
    axios.get('/example-api.json')
    .then(function (response) {
      vueScope.input_data = response.data;
      vueScope.organization = response.data.metadata.customerName;
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
    grid-template-columns: [logo-start test-start source-start hosting-start] 1fr [logo-end test-end organization-start environment-start] 1fr 1fr 1fr [source-end collaboration-start] 1fr [organization-end environment-end collaboration-end hosting-end];
    grid-template-rows: [logo-start organization-start] auto [logo-end organization-end test-start environment-start] auto auto auto [test-end environment-end collaboration-start source-start] auto [collaboration-end source-end hosting-start] auto [hosting-end];
    grid-gap: 5px;
}

* {
    padding: 5px;
}


span {
    font-weight: normal;
}

.organization-wrapper {
    background-color: #d63031;
    grid-area: organization;
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
    grid-area: hosting;
    display: grid;
    grid-row: repeat(2, 1fr);
}


.environment-wrapper {
    grid-area: environment;
    display: grid;
    grid-row: repeat(3, 1fr);
}

.collaboration-wrapper {
    background-color: #00b894;
    grid-area: collaboration;
    display: grid;
    grid-row: repeat(2, 1fr);
}

.test-wrapper {
    background-color: #6c5ce7;
    grid-area: test;
    display: grid;
    grid-row: repeat(2, 1fr);

}

.source-wrapper {
    background-color: #fdcb6e;
    grid-area: source;
    display: grid;
    grid-row: repeat(1, 1fr);
}

</style>

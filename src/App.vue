<template>
  <!-- <div id="collaboration-app">
    <collaboration-tag
      v-for="item in list"
      v-bind:struct="item"
      v-bind:key="item.id">
    </collaboration-tag>
  </div> -->

  <div id="app">
<!--      <div class="logo">
          <img src="./assets/rhlabs.png">
      </div>
    <div class="organization-wrapper">
        <div class="organization">
	<div class="box-heading"> <h2>ORGANIZATION</h2> </div>
            <p>{{ organization }}</p>
        </div>
    </div> -->
    <div class="content-box-collaboration">
        <div class="collaboration-wrapper">
            <div class="box-heading"> <h2>COLLABORATION</h2> </div>
            <app-collaboration
              v-for="item in input_data.stack.collaborationTools" :class="item.icon"
              v-bind:struct="item">
            </app-collaboration>
        </div>
    </div>
    <div class="content-box-environment">
        <div class="environment-wrapper">
            <div class="box-heading"> <h2>ENVIRONMENT</h2> </div>
            <app-environment :applications="input_data.stack.appContainers"
              v-for="item in input_data.stack.environments"
              v-bind:struct="item">
            </app-environment>
        </div>
    </div>
    <div class="content-box-source">
        <div class="source-wrapper">
            <div class="box-heading"> <h2>SOURCE CONTROL</h2> </div>
            <app-source
              v-for="item in input_data.stack.sourceControl" :class="item.icon"
              v-bind:struct="item">
            </app-source>
        </div>
    </div>

    <div class="content-box-test">
	<div class="box-heading"><h2>PIPELINE</h2></div>
        <div class="test-wrapper">
            <app-test
              v-for="item in input_data.stack.testLibraries" :class="item.icon"
              v-bind:struct="item">
            </app-test>
        </div>
    </div>

    <div class="content-box-hosting">
	<div class="box-heading"><h2>HOSTING</h2></div>
        <div class="hosting-wrapper">
            <app-hosting
              v-for="item in input_data.stack.hosting" :class="item.icon"
              v-bind:struct="item">
            </app-hosting>
        </div>
    </div>
    <!-- <div class="builder">
        <img src="./assets/builder.png">
    </div> -->




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
@import url('https://fonts.googleapis.com/css?family=Overpass');
html {
    font-family: Overpass;
}

#app {
    display: grid;
/*    grid-template-columns: [logo-start test-start source-start hosting-start] 1fr [logo-end test-end organization-start environment-start] 1fr 1fr 1fr [source-end collaboration-start] 1fr [organization-end environment-end collaboration-end hosting-end];
    grid-template-rows: [logo-start organization-start] auto [logo-end organization-end test-start environment-start] auto auto auto [test-end environment-end collaboration-start source-start] auto [collaboration-end source-end hosting-start] auto [hosting-end];*/
    grid-template-columns: [test-start source-start hosting-start] auto [test-end environment-start] auto auto auto [source-end collaboration-start] auto [environment-end collaboration-end hosting-end];
    grid-template-rows: [test-start environment-start] auto auto auto [test-end environment-end collaboration-start source-start] auto [collaboration-end source-end hosting-start] auto [hosting-end] 25px;
    grid-gap: 5px;
}

h2 {

    margin: 0px;
}

* {
    padding: 5px;
}

span {
    font-weight: normal;
}

.box-heading {
    margin: 0px;
    text-align: center;
    background: #bc202a;
    color: #fff;
    margin: 0px;
}

.builder {
    grid-area: builder;
    transform: scale(0.25);
}


.organization-wrapper {
    grid-area: organization;
    display: grid;
    grid-column: 1fr 1fr;
    grid-row: 1fr;
}

.organization {
    border: 10px solid #d8dcdd;
    padding: 3px;

}

.content-box-hosting {
    border: 10px solid #d8dcdd;
    grid-area: hosting;
}
.hosting-wrapper {
    display: grid;
    grid-row: repeat(2, 1fr);
}


.content-box-environment{
    border: 10px solid #d8dcdd;
    grid-area: environment;

}
.environment-wrapper {
    display: grid;
    grid-row: repeat(3, 1fr);
}

.collaboration-wrapper {
    border: 10px solid #d8dcdd;
    grid-area: collaboration;
    display: grid;
    grid-row: repeat(2, 1fr);
}

.content-box-test{
    border: 10px solid #d8dcdd;
    grid-area: test;
}
.test-wrapper {
    display: grid;
    grid-row: repeat(2, 1fr);

}

.content-box-source{
    border: 10px solid #d8dcdd;
    grid-area: source;
}
.source-wrapper {
    display: grid;
    grid-row: repeat(1, 1fr);
}

</style>

<template>
  <div class="environment">
      {{ struct.name }}
      <app-container
        v-for="item in applications" :class="'fab fa-'+ item.icon"
        v-bind:substruct="item">
      </app-container>
  </div>
</template>

<script>
import AppContainer from './AppContainer.vue'

  export default {
    props: ['struct', 'applications'],
    name: 'app-environment',
    components: {
      "app-container" : AppContainer
    },
    data () {
      return {}
    }
  }
</script>

<style scoped>
.environment {
    background-color: #81ecec;
    margin: 5px;
    display: grid;
    grid-row: repeat(3, 1fr);
}
</style>

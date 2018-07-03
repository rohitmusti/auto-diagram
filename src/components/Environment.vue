<template>
  <div class="environment">
      {{ struct }}
      <app-container
        v-for="item in applications"
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

</style>

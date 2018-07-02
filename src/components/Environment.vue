<template>
  <div>
      <h1>Message from Environment</h1>
      <p>{{ environments }}</p>
  </div>
</template>

<script>
import AppContainer from './AppContainer.vue'

  export default {
    props: ['environments'],
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

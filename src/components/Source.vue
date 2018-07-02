<template>
  <div>
      <h1>Message from Source</h1>
      <p>{{ sourceControls }}</p>
  </div>
</template>

<script>
  export default {
    props: ['sourceControls'],
    name: 'app-source',
    data () {
      return {}
    }
  }
</script>

<style scoped>

</style>

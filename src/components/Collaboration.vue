<template>
  <div>
      <h1>Message from Collaboration</h1>
      <p>{{ collaborationTools }}</p>
  </div>
</template>

<script>
  export default {
    props: ['collaborationTools'],
    name: 'app-collaboration',
    data () {
      return {}
    }
  }
</script>

<style scoped>

</style>

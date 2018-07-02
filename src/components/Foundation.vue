<template>
  <div>
      <h1>Message from Foundation</h1>
      <p>{{ foundations }}</p>
  </div>
</template>

<script>
  export default {
    props: ['foundations'],
    name: 'app-foundation',
    data () {
      return {}
    }
  }
</script>

<style scoped>

</style>

<template>
  <div class="source">
      <i> {{struct.name}} </i>
  </div>

</template>

<script>
  export default {
    props: ['struct'],
    name: 'app-source',
    data () {
      return {}
    }
  }
</script>

<style scoped>
.source {
    background-color: #ffeaa7;
}
</style>

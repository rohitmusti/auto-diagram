<template>
      <i class="source" > <span>{{ struct.name }}</span> </i>
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

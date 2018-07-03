<template>
  <div class="test">
      {{ struct }}
  </div>
</template>

<script>
  export default {
    props: ['struct'],
    name: 'app-test',
    data () {
      return {}
    }
  }
</script>

<style scoped>

.test {
    background-color: #a29bfe;
    margin: 5px;
}
</style>

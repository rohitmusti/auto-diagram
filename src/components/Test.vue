<template>
  <!-- <div class="test">
      {{ struct.name }}
  </div> -->
  <i> {{struct.name}} </i>

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

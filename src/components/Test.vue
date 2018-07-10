<template>
      <i class="test"> <span>{{struct.name}}</span> </i>

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

<template>
  <div class="collaboration">
      <i> {{ struct.name }}</i>
  </div>
</template>

<script>
  export default {
    props: ['struct'],
    name: 'app-collaboration',
    data () {
      return {}
    }
  }
</script>

<style scoped>
.collaboration {
    margin: 5px;
    background-color: #55efc4;
}
</style>

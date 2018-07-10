<template>
  <div class="host">
      <i> {{struct.name}} </i>
  </div>

</template>

<script>
  export default {
    props: ['struct'],
    name: 'app-hosting',
    data () {
      return {}
    }
  }
</script>

<style scoped>
.host {
    background-color: #ff7675;
    margin: 5px;
    padding: 3px;

}

</style>

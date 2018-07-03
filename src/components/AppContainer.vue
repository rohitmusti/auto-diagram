<template>
  <div class="container">
    {{substruct}}
  </div>
</template>

<script>
  export default {
    props:['substruct'],
    name: "app-container"
  }
</script>

<style scoped>
.container {
    background-color: #0984e3;
    margin: 5px;

}

</style>

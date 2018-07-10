<template>
  <!-- <div class="container">
      <i class="fas fa-" + {{substruct.icon}}> </i>

    {{substruct.name}}
  </div> -->
  <i></i>
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

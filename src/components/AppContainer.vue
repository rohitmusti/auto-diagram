<template>
      <i class="container"> <span>{{substruct.name}}</span></i>
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

<template>
    <button class="btn">
        <svg-icon class="svg-button" :name=icon />
        <p class="font-weight-regular">{{title}}</p>
    </button> 
</template>

<script>
   import svgIcon from '../components/Svg';
   export default {
       components: {
           'svg-icon': svgIcon
       },
       props:{
           title: String,
           icon: String,
       }
   }
</script>

<style lang="scss" scoped>
  .btn:hover {
    .svg-button{
        stroke: #5D21D2;
    } 
  }
</style>
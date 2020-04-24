<template>
    <button class="btn">
        <svg-icon class="svg-button" :name=icon />
        <p class="label">{{title}}</p>
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
    .btn:hover{
         .label{
            color: #5D21D2 !important;
        }
        .svg-button{
            fill: #5D21D2;
        }
       
    }
  
  .svg-button{
    fill:rgb(83, 86, 88);
  }
  p{
      color: rgb(83, 85, 87) !important;
      font-size: 15px !important;
      width: 0% !important;
      padding-left: 16px !important;
      font-weight: 400;
  }
</style>
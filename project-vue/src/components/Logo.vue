<template>
    <div class="d-flex flex-nowrap mt-2 ml-2">
         <svg-icon name="svg-logo"/>
         <p class="label-1">СГУПП</p><p class="label-2">ЖКХ</p>
    </div>
</template>

<script>
import svgIcon from '../components/Svg';
export default {
    components: {
           'svg-icon': svgIcon
       },
}
</script>

<style lang="scss" scoped>
    .label-1{
        padding-left: 15px !important;
        padding-top: 4px;
        color: #3A3C3D;
        font-weight: bold;
        font-size: 16px;
    }
    .label-2{
        padding-left: 0px !important;
        padding-top: 4px;
        color: #3A3C3D !important;
        font-weight: bold !important;
        font-size: 16px;
    }
</style>
<template>
    <div>
        <div>
            <p class="label-welcome">Добро пожаловать,<span class="label-name"> Сергей</span></p>
        </div>
        <div>
            <div>
                <Card/>
            </div>  
        </div>  
    </div>
</template>

<script>
import Card from './Card';

export default {
    components:{
        Card,
    }
}
</script>

<style lang="scss" scoped>

    .label-welcome{
        color: #828588;
        font-size: 20px;
        padding-left: 0px !important;
    }

    .label-name{
        color: rgb(44, 48, 51);

    }
</style>
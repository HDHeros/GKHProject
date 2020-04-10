<template>
    <v-menu class="menu"
      v-model="value"
      :close-on-click="closeOnClick"
      :close-on-content-click="closeOnContentClick"
      :offset-y="offsetY"
      
    >
      <template  v-slot:activator="{ on }">
        <v-btn class="btn-avatar" v-on="on">
            <v-avatar size="40">
                <img src="https://cdn.vuetifyjs.com/images/john.jpg" alt="John">
            </v-avatar>
            <p class="subtitle-2">Сергей</p>
            <img class="down" src="../assets/down.png" alt="">
        </v-btn>
      </template>

      <v-list class="list">
         <v-list-item  v-for="(item, index) in items" v-bind:key="index">
          <v-list-item-title  class="list-item">{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
        
    </v-menu>
</template>

<script>
export default {
    data: () => ({
      items: [
        { title: 'Click Me' },
        { title: 'Click Me' },
        { title: 'Click Me' },
        { title: 'Click Me 2' },
      ],
      closeOnClick: true,
      closeOnContentClick: true,
      offsetY: true,
    }),
}
</script>

<style>
    .btn-avatar{
       height: 100% !important;
       width: 100% !important;
       box-shadow: none; 
       text-transform: none;
       justify-content: space-between;
       padding-left: 10px !important;
       padding-right: 10px !important;
    }
    p{
        width: 100% !important;
        margin-bottom: 0px !important;
        padding-left: 6px !important;
        padding-right: 5px !important;
        color: #636C76;
    }
    .list :hover {
      cursor: pointer;
      background-color: ghostwhite;
    }
    
    .theme--light.v-btn:not(.v-btn--flat):not(.v-btn--text):not(.v-btn--outlined) {
    background-color: #F5F5F5 !important;
    }
    .v-btn:before {
      background-color: ghostwhite;
}


</style>
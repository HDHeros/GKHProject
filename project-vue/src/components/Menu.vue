<template>
    <v-navigation-drawer app
      v-model="drawer"
      :mini-variant.sync="mini"
      permanent
    >
      <v-list-item class="px-2">
        <v-list-item-avatar @click.stop="mini = !mini" style="margin-left: 4px !important;" size="30" tile>
          <v-img src="../assets/menu.svg" height="30" width="30"></v-img>
        </v-list-item-avatar>
      </v-list-item>

      <v-divider></v-divider>
      <div class="text-center">      
        <ButtomMenu 
          v-for="item in bottom_list"
          :key="item.title"
          :title="item.title"
          :icon ="item.icon"
        />
      </div>
    </v-navigation-drawer>

</template>

<script>
  import ButtomMenu from '../components/ButtomMenu';
  export default {
    components: {
    ButtomMenu,
  },
    name: 'Menu',
    data () {
      return {
        drawer: true,
        mini: true,
        bottom_list:[
          {
            title: 'Главная',
            icon: 'svg-home'
          },
          {
            title: 'Контакты',
            icon: 'svg-contacts'
          }
        ]
      }
    },
  }
</script>

<style lang="scss" scoped>
  .theme--light.v-navigation-drawer .v-divider {
    border-color: rgb(255, 255, 255);
}
  .v-application .text-center {
    padding-left: 15px;
  }
  .v-application p {
    width: 70% !important;
}
  .btn {
    display: flex;
    width: 160px;
    height: 40px;
    border-radius: 20px;
    margin:auto;
    padding-left: 8%;
    outline: none;
  }
  
  .btn:hover { 
      background-color: rgba(82, 81, 81, 0.055) !important; 
  }
</style>
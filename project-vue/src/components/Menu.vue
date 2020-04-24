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
         <logo/>
      </v-list-item>

      <div class="text-center mb-10">      
        <ButtomMenu
          v-for="item in bottom_list"
          :key="item.title"
          :title="item.title"
          :icon ="item.icon"   
        />
      </div>
      <div class="BIT">
        <v-subheader>BIT</v-subheader>
        <v-divider class="hr"></v-divider>
        <ButtomMenu
          v-for="item in bottom_listBIT"
          :key="item.title"
          :title="item.title"
          :icon ="item.icon"   
        />
      </div>
    </v-navigation-drawer>
   
</template>

<script>
  import ButtomMenu from '../components/ButtomMenu';
  import Logo from '../components/Logo';
  export default {
    components: {
    ButtomMenu,
    Logo,
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
        ],
        bottom_listBIT:[
          {
            title: 'Заявки',
            icon: 'svg-request'
          }
        ],
      }
    }
  }
</script>

<style lang="scss" scoped>
  .v-application .text-center {
    padding-left: 3px;
    margin-top: 60px;
  
  }
  .btn {
    display: flex;
   
    width: 160px;
    height: 40px;
    border-radius: 20px;
    margin:auto;
    padding-left: 15px;
    padding-top: 5px;
    outline: none;
  }
  
  .btn:hover { 
      background-color: rgba(82, 81, 81, 0.055) !important; 
  }

  .BIT{
    
  }
  .hr{
 
  }
</style>
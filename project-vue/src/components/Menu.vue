<template>
    <v-navigation-drawer app
      v-model="drawer"
      :mini-variant.sync="mini"
      permanent
    >
      <v-list-item class="px-2">
        <v-list-item-avatar style="margin-left: 4px !important;" size="30" tile>
          <v-img src="../assets/menu.svg" height="30" width="30"></v-img>
        </v-list-item-avatar>

        <p style="color: #232426;" class="font-weight-bold">ЖКХ «‎Комплекс»</p>‎

        <v-btn
          icon
          @click.stop="mini = !mini"
        >
          <v-icon>mdi-chevron-left</v-icon>
        </v-btn>
      </v-list-item>

      <v-divider></v-divider>
      <div class="text-center">
          <button class="btn">
              <img src="../assets/home.svg" height="22" width="22">
              <p class="font-weight-regular">Home</p>
          </button>       
      </div>
    </v-navigation-drawer>

</template>

<script>
  export default {
    data () {
      return {
        drawer: true,
        items: [
          { title: 'Home', icon: 'mdi-home-city' },
          { title: 'My Account', icon: 'mdi-account' },
          { title: 'Users', icon: 'mdi-account-group-outline' },
        ],
        mini: true,
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
    width: 150px;
    height: 40px;
    border-radius: 20px;
    margin:auto;
    padding-left: 6%;
    outline: none;
      
  }
  
  .btn:hover { 
      background-color: rgba(71, 71, 71, 0.089) !important; 
  }


  

</style>
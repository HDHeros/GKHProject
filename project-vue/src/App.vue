<template>
  <v-app>
    <Menu/>
    <v-app-bar class="heder pr-5" app>
      <Header/>
    </v-app-bar>

    <v-content class = "content mt-9 pr-2">
      <v-container class="pl-0 pt-0 pr-12" fluid>
          <Home/>
          <!-- <Users/> -->
          
        <router-view></router-view>
      </v-container>
    </v-content>

    <v-footer  app>
    </v-footer>
  </v-app>
</template>

<script>
// import Users from './components/Users';
import Header from './components/Header';
import Menu from './components/Menu';
import Home from './components/Home';
export default {
  name: 'App',

  components: {
    // Users,
    Home,
    Header,
    Menu,
  },

  data: () => ({
    //
  }),
};
</script>

<style lang="scss" scoped>
  .heder {
    box-shadow: none ;
    background-color: #F6F7FA;
  }
  .content {
    background-color: #F6F7FA;
    margin-left: 56px;
  }

  .v-app-bar.v-toolbar__content {
    width: 100% !important;
  }
  
</style>
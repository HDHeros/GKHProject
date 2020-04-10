<template>
  <v-app>
    <Menu/>
    <v-app-bar class="heder" app>
      <Header/>
    </v-app-bar>

    <v-content class = "content">
      <v-container fluid>
          <Home/>
        <router-view></router-view>
      </v-container>
    </v-content>

    <v-footer  app>
    </v-footer>
  </v-app>
</template>

<script>
import Home from './components/Home';
import Header from './components/Header';
import Menu from './components/Menu';
export default {
  name: 'App',

  components: {
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
  // #navigation {
  //   display: flex;
  //   height: 100%;
  //   background-color: #ffffff;
  // }
  .content {
    background-color: #F6F7FA;
  }

  .v-app-bar.v-toolbar__content {
    width: 100% !important;
  }
  
</style>
<template>
  <v-app>
    <v-navigation-drawer floating id="navigation" app>
    </v-navigation-drawer>

    <v-app-bar class="heder" app>
      <Header/>
    </v-app-bar>

    <!-- Sizes your content based upon application components -->
    <v-content class = "content">

      <!-- Provides the application the proper gutter -->
      <v-container fluid>
          <Home/>
        <router-view></router-view>
      </v-container>
    </v-content>

    <v-footer  app>
      <!-- -->
    </v-footer>
  </v-app>
</template>

<script>
import Home from './components/Home';
import Header from './components/Header';

export default {
  name: 'App',

  components: {
    Home,
    Header,
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
  #navigation {
    display: flex;
    height: 100%;
    background-color: #ff0000;
  }
  .content {
    background-color: #F6F7FA;
    border: none;
  }

  .v-app-bar.v-toolbar__content {
    width: 100% !important;
  }
  
</style>
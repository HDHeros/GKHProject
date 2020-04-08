<template>
  <v-app>
    <v-navigation-drawer app>
      
    </v-navigation-drawer>

    <v-app-bar  class="white" app>
      <Header/>
    </v-app-bar>

    <!-- Sizes your content based upon application components -->
    <v-content>

      <!-- Provides the application the proper gutter -->
      <v-container fluid>
        <Home/>
        <router-view></router-view>
      </v-container>
    </v-content>

    <v-footer app>
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

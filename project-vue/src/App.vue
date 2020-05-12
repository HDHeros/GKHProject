<template>
  <div app>
      <router-view></router-view>
  </div>
</template>

<script>
import Axios from 'axios'
  export default {
    name: 'App',
    created() {
      if (localStorage.getItem("auth_token")) {
          Axios.defaults.headers.common['Authorization'] = 'Token ' + localStorage.getItem('auth_token')
          this.$router.push({name:"home"})
      }
      else
      {
        this.$router.push({name:"login"})
      }
    }
  }
</script>

<style lang="scss" scoped>
  
</style>
<template>
        <div class="contener-flex">
          <div class="search-item-flex">
              <Search/>
          </div>
          <div class="Login">
              <Avatars/>
          </div>
        </div>    
</template>

<script>
import Search from '../components/Search';
import Avatars from '../components/Avatars';
export default {
    name: 'Header',
    components: {
    Search,
    Avatars,
  }
}
</script>

<style lang="scss" scoped>
    .contener-flex {
      display: flex;
      width: 100%;
      justify-content: space-between;
      
    }
    .search-item-flex {
      width: 75%;
      margin-left: 40px;
      margin-right: 20px;
    }
    .Login {
      margin-right: 10px;
    }
</style>

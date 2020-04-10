<template>
    <div class="flex-contener">
        <div class="search-form">
            <button type="submit" class="search-button">
                <img src="../assets/search.svg" alt="Vue Logo" height="25" width="25">
            </button>
            <input type="search" class="search-input">   
        </div>
        <!-- Сделать 2 бокса во flex-contener, в одном будет поиск на 70%, сторой на 30% для Логина -->
    </div>
</template>


<script>
export default {
    
}
</script>

<style lang="scss" scoped>
    .flex-contener {
        display: flex;
        flex: auto; 
        width: 100%;        
    }

    .search-form {
        display: flex;
        width: 100%;
        min-height: 40px;
        border-radius: 10px;
        border: 1px solid #E5E7ED;
        background: #fff;
        box-sizing: border-box;
    }

    .search-input {
        width: 100%;
        height: 29px;
        margin: auto;
        background-color:none;
        font-size: 14px;  
        color: #5a6674;
        outline: none;
    }
    .search-button {
        height: 25px;
        width: 25px;
        padding: 0;
        margin: 7px 12px 0 15px;
        border: none;
        background: none;
        outline: none !important;
        cursor: pointer;
    }
</style>
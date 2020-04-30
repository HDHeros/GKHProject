<template>
    <div>
        <input v-model="login" type="text" placeholder="Логин">
        <input v-model="password" type="password" placeholder="Пароль">
        <button @click="goMain">Войти</button>
    </div>
</template>

<script>
export default {
    name: "Login",
    data(){
        return {
            login: '',
            password: '',
        }
    },
    methods:{
        goMain(){
            this.$router.push({name:"home"})
        }
    }
}
</script>
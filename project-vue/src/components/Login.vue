<template>
    <div class="box">
        <div id="header">
            <div id="cont-lock">
                <p class="lock">СГУПП ЖКХ «Комплекс»</p>
            </div>
        </div> 
            <div class="group">      
                <input v-model="login" class="inputMaterial" type="text" required>
                <span class="highlight"></span>
                <span class="bar"></span>
                <label>Логин</label>
            </div>
            <div class="group">      
                <input v-model="password" class="inputMaterial" type="password" required>
                <span class="highlight"></span>
                <span class="bar"></span>
                <label>Пароль</label>
            </div>
            <button @click="setLogin" id="buttonlogintoregister" type="submit">Войти</button>
    </div>
</template>

<script>
import Axios from 'axios'
export default {
    name: "Login",
    data(){
        return {
            login: '',
            password: '',
        }
    },
    methods:{
        setLogin(){
            // this.$router.push({name:"home"})
            Axios.post('http://192.168.1.89:8000/auth/token/login/',{
                username: this.login,
                password: this.password
            })
            .then((response)=>{
                localStorage.setItem("auth_token",response.data.auth_token);
                this.$router.push({name:"home"});
            })
            .catch((response)=>{
                if(response == "Error: Request failed with status code 400"){
                  alert("Логин или пароль не верен")
                }
            })
        }
    }
}
</script>

<style lang="scss" scoped>

/* BOX LOGIN */
.box{
	position: relative;
	margin: auto;
	height: 350px;
    top: 100px;
	left: 0;
	z-index: 200;
	right: 0;
	width:400px;
	color:#666;
	border-radius: 3px;
	background: #FFF;
    margin-bottom: 100px;
    box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
    overflow: hidden;
}

#header{
  background: #5D21D2;
  position: relative;
  height: 80px;
  width: 100%;
  margin-bottom: 20px;
}

#cont-lock{
  width: 100%;
  height: 65px;
  position: relative;
}

.lock{
  text-align: center;
  color: rgb(255, 255, 255);
  position: absolute;
  left: 0;
  right: 0;
  margin: 0;
  top: 0;
  bottom: 0;
  line-height: 80px;
  font-size: 23px !important;
  font-family: "Roboto";
}

#bottom-head::after{
  content: '';
  width: 0px;
  height: 0px;
  display: block;
  position: absolute;
  margin: auto;
  left: 0;
  right: 0;
  bottom: 0;
  border-bottom: 7px solid white;
  border-right: 7px solid rgba(0,0,0,0);
  border-left: 7px solid rgba(0,0,0,0);
  border-top: 7px solid rgba(0,0,0,0);
}

.box h1{
  margin-left: 20px;
  margin-top: 0;
	font-size: 24px;
  font-weight: 300;
  color: #cfd8dc;
  line-height: 35px;
}

.box button{
	background: #5D21D2;
	border:0;
	color: rgb(255, 255, 255);
	padding:10px;
	font-size: 15px;
    font-family: "Roboto Regular";
    font-weight: 300;
	width:330px;
	margin:20px auto;
	display:block;
	cursor:pointer;
    -webkit-transition: all 0.4s;
	transition: all 0.4s;
	border-radius: 2px;
}

.box button:active{
	background: #5D21D2;
    color: #5D21D2;
}

.box button:hover{
	background: rgba(92, 33, 210, 0.863);
    color: #FFF;
    -webkit-transition: all 0.4s;
	transition: all 0.4s;
}

.group 			  { 
  position:relative; 
  margin-bottom: 35px; 
  margin-left: 40px;
}

.inputMaterial 				{
  font-size:18px;
  padding:10px 10px 10px 5px;
  display:block;
  width:315px;
  border:none;
  border-bottom:1px solid #757575;
}

.inputMaterial:focus { outline:none;}

/* LABEL ======================================= */

label 				 {
  color:rgb(66, 66, 66); 
  font-size:14px;
    font-family: "Roboto Regular";
  font-weight:normal;
  position:absolute;
  pointer-events:none;
  left:5px;
  top:10px;
  transition:0.2s ease all; 
  -moz-transition:0.2s ease all; 
  -webkit-transition:0.2s ease all;
}

/* active state */
.inputMaterial:focus ~ label, .inputMaterial:valid ~ label 		{
  top:-10px;
  font-size:14px;
  color: #5D21D2;
}

/* BOTTOM BARS ================================= */
.bar 	{ position:relative; display:block; width:315px; }
.bar:before, .bar:after 	{
  content:'';
  height:2px; 
  width:0;
  bottom:1px; 
  position:absolute;
  background: #5D21D2; 
  transition:0.2s ease all; 
  -moz-transition:0.2s ease all; 
  -webkit-transition:0.2s ease all;
}
.bar:before {
  left:50%;
}
.bar:after {
  right:50%; 
}

/* active state */
.inputMaterial:focus ~ .bar:before, .inputMaterial:focus ~ .bar:after {
  width:50%;
}

/* active state */
.inputMaterial:focus ~ .highlight {
  -webkit-animation:inputHighlighter 0.3s ease;
  -moz-animation:inputHighlighter 0.3s ease;
  animation:inputHighlighter 0.3s ease;
}

body{
  background: #F6F7FA;
}
</style>
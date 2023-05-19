<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/annonce">Annonce</router-link> |
    <router-link to="/contact">Contact</router-link> |
    <router-link to="/login">Login</router-link> |
    <router-link to="/Profile">Mon Profile</router-link>
  </nav>
  <router-view/>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;800&display=swap');
* {
  font-family: 'Poppins', sans-serif;
  margin:0;
  padding: 0;
  box-sizing: border-box;
}

body {
  margin: 0 auto;
  background: cornflowerblue;
  padding-bottom: 4rem;
  overflow-x: hidden;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
}

nav {
  overflow: hidden;
  background-color :white;
  width : 100%;
  padding: 30px;
}

nav a {
  text-align: center;
  font-weight: bold;
  padding: 10px 12px;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: black;
  text-decoration: none;
}
h1{
  text-align: center;
  color: antiquewhite;
  font-size: 3em;
  text-shadow: 1px 3px 2px black;
}
#imagePrincipale{
  padding-top: 60px;
  background: url(shark.jpg) no-repeat fixed 50% 50%;
  background-size: cover;
  height: 799px;
}


</style>

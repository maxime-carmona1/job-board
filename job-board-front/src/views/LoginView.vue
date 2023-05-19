<template>
    <div class="card">
    <h1 class="card__title" v-if="mode == 'login'">Connexion</h1>
    <h1 class="card__title" v-else>Inscription</h1>
    <p class="card__subtitle" v-if="mode == 'login'">Tu n'as pas encore de compte ? <span class="card__action" @click="switchToCreateAccount()">Créer un compte</span></p>
    <p class="card__subtitle" v-else>Tu as déjà un compte ? <span class="card__action" @click="switchToLogin()">Se connecter</span></p>
    <div class="form-row">
      <input v-model="mail_adress" class="form-row__input" type="text" placeholder="Adresse mail"/>
    </div>
    <div class="form-row" v-if="mode == 'create'">
      <input v-model="user_name" class="form-row__input" type="text" placeholder="nom d'utilisateur"/>
      <input v-model="first_name" class="form-row__input" type="text" placeholder="Prénom"/>
      <input v-model="last_name" class="form-row__input" type="text" placeholder="Nom"/>
      <input v-model="phone" class="form-row__input" type="text" placeholder="phone"/>
      <input v-model="user_description" class="form-row__input" type="text" placeholder="description"/>
    </div>
    <div class="form-row">
      <input v-model="mdp" class="form-row__input" type="password" placeholder="Mot de passe"/>
    </div>
    <div class="form-row" v-if="mode == 'login' && status == 'error_login'">
      Adresse mail et/ou mot de passe invalide
    </div>
    <div class="form-row" v-if="mode == 'create' && status == 'error_create'">
      Adresse mail déjà utilisée
    </div>
    <div class="form-row">
      <button @click="login()" class="button" :class="{'button--disabled' : !validatedFields}" v-if="mode == 'login'">
        <span v-if="status == 'loading'">Connexion en cours...</span>
        <span v-else>Connexion</span>
      </button>
      <button @click="createAccount()" class="button" :class="{'button--disabled' : !validatedFields}" v-else>
        <span v-if="status == 'loading'">Création en cours...</span>
        <span v-else>Créer mon compte</span>
      </button>
    </div>
  </div>
  </template>
  
  <script>
export default {
  async mounted() {
      //const result =  await
       await axios.get(
        'http://127.0.0.1:5000/API/USERS'
      )
      .then((response) => {
        console.log(response)
        this.tableau = response.data.result
      } ).catch((error) => console.log(error))

      //console.log(result);
  },
  async mounted() {
      //const result =  await
       await axios.post(
        'http://127.0.0.1:5000/API/USERS',{"user_name": user_name},{"first_name": first_name}
        ,{"last_name": last_name},{"mdp": mdp},{"phone":phone},{"user_description": user_description}
      )
      .then((response) => {
        console.log(response)
        this.tableau = response.data.result
      } ).catch((error) => console.log(error))

      //console.log(result);
  },
  data() {
    return {
     tableau: [],
     count: false,
     user_name :"",
     first_name :"",
     last_name:"",
     mdp :"",
     phone :"",
     user_description: ""
    };
  }
}
  </script>
<style scoped>
.form-row {
  display: flex;
  margin: 16px 0px;
  gap:16px;
  flex-wrap: wrap;
}
.form-row__input {
  padding:8px;
  border: none;
  border-radius: 8px;
  background:#f2f2f2;
  font-weight: 500;
  font-size: 16px;
  flex:1;
  min-width: 100px;
  color: black;
}
.form-row__input::placeholder {
  color:#aaaaaa;
}
</style>>

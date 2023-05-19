<template>
  <div class="home">
    <h1>Bienvenue sur la page d'annonce</h1>
  </div>
  <div class="restaurantCards">
    <h2>Toutes les annonces</h2>
  </div>
  <div class="dive">
   <div v-for="tab in tableau" :key="tab.id" class="cards">
      <p>{{tab.entreprise}}</p>
      <p>{{tab.job_title}}</p>
      <p>{{tab.contratType}}</p>
    <button @click="learnMore(tab.id)">learn more</button>
      <div v-if="count === tab.id">
        <p>salaire: {{tab.salaire}}euro/net</p>
        <p>{{tab.job_description}}</p>
        <p>{{tab.online_date}}</p>
      </div>
</div>
</div>
<div><h2>Vous voulez déposer une annonce ?</h2></div>
<div><p>Remplisez le formulaire ci-dessous</p></div>
  <input v-model="entreprise" placeholder="Entreprise">
    <input v-model="job_title" placeholder="Intituler du poste">
    <input v-model="contratType" placeholder="Type de contract">
    <input v-model="salaire" placeholder="Salaire">
    <input v-model="job_description" placeholder="Description du poste">
    <input v-model="online_date" placeholder="Date de mise en ligne">
    <button>Publier</button>
    <div></div>
</template>
<script>
import axios from "axios";
export default {
  methods: {
    learnMore(id) {
        this.count = id
    }
  },
  async mounted() {
      //const result =  await
       await axios.get(
        'http://127.0.0.1:5000/API/ADVERTISMENTS'
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
        'http://127.0.0.1:5000/API/ADVERTISMENTS',{"entreprise": entreprise},{"job_title": job_title}
        ,{"contact_type": contact_type},{"salaire": salaire},{"job_description":job_description}
        ,{"online_date": online_date}
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
     entreprise :"",
     job_title :"",
     contact_type:"",
     salaire :"",
     job_description :"",
     online_date: ""
    };
  }
}
</script>

<style scoped>
.cards{
  padding: 15px;
  background-color: azure;
  border-radius: 20px;
  margin: auto;
}

.dive {
  display: flex;
}
</style>
<template>
  <div class="home">
    <h1>Bienvenue sur Find Job</h1>
  </div>
  <p v-if="result == 0">Aucune annonce pour le moment 😥</p>
  <p v-else-if="result ==1">il y a {{result}} annonce consutable sur le site 💪</p>
  <p v-else>il y a {{result}} annonces consultable sur le site 🔥</p>
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
data() {
    return {
     tableau: [],
     count: false,
    };
  }
}
</script>
<style scoped>

</style>
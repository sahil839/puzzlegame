<template>
  <div id="app">
  <Toolbar></Toolbar>
  <v-app id="inspire">
  <v-hover>
  <v-container grid-list-xl>
     <v-layout row wrap>
       <v-flex xs12 sm6 md6 v-for="card in cards" :key="card">
         <v-card hover=true id="card" color="brown lighten-2"
         >
           <v-card-media
           :src="card.src"
             height="150px"
             id="media-card"
           >
           <div id="About-genre">
           About Genre hi try this genre play
           </div>
             </v-card-media>
          <v-card-title primary-title=false id="genre-name">
               <div >
                 <h3 class="headline" >{{card.genre}}</h3>
               </div>
             </v-card-title>
             <v-card-actions>
            <v-btn flat color="orange">Explore</v-btn>
          </v-card-actions>

         </v-card>
       </v-flex>
     </v-layout>
     </v-container>
     </v-hover>
   </v-app>
  </div>
</template>

<script>
import Toolbar from './toolbar.vue'
export default {
  name: 'App',
  components: {
    'Toolbar': Toolbar
  },
  data () {
    return {
      cards: [
        {
          src: 'http://thecsrjournal.in/wp-content/uploads/2017/04/Sports-I.jpg',
          genre: 'Sports'
        },
        {
          src: 'http://www.priorparkcollege.com/resources/images/general/_hero/politics-2.PNG',
          genre: 'Politics'
        },
        {
          src: 'https://www.colourbox.com/preview/4233974-old-vintage-golden-compass-on-ancient-map.jpg',
          genre: 'History'
        },
        {
          src: 'https://cdn.thisiswhyimbroke.com/images/fractal-jigsaw-640x533.jpg',
          genre: 'Puzzle'
        }
      ]
    }
  }
}
</script>

<style scoped>
#inspire{
  padding-top:30px;
  background-color:#D7CCC8;
}
#media-card{
  transition:transform 2s,opacity 0s linear 0.5s;
  color:black;
}
#card:hover #media-card{
  transform:rotateY(180deg);
  opacity:0.8;
}
#card:hover #About-genre{
  opacity:1;
  transform:rotateY(180deg);
}
#About-genre{
  opacity:0;
  transition:transform 2s,opacity 0s linear 0.5s;
  margin:auto auto auto auto;
  font-size:20px;
  font-weight:bold;
}
</style>

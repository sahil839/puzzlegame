<template>
<v-app id="inspire">
  <v-carousel ma-0 id="imp" style="height:100%">
    <v-carousel-item :src="src1" id="img1">
    <v-jumbotron dark>
             <v-container fill-height>
              <v-layout align-center>
             <v-flex>
                  <h3 class="display-3">WELCOME TO WORLD OF PUZZLES</h3>
              </v-flex>
              </v-layout>
   </v-container>
    </v-jumbotron></v-carousel-item>
 <v-carousel-item :src="src2" id="img2"></v-carousel-item>
<v-carousel-item :src="src3" id="img3" ></v-carousel-item>
<v-carousel-item :src="src4" id="img4"></v-carousel-item>
  </v-carousel>
</v-app>
</template>

<script>
export default{
  name:'HelloWorld',
  data () {
    return {
      src1: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg',
      src2: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg',
      src3: 'https://cdn.pixabay.com/photo/2016/03/16/16/27/puzzle-1261138__340.jpg',
      src4: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#inspire{
  height: 100vh;
 }
</style>

<template>
<v-app id="inspire">
  <v-carousel ma-0 id="imp" style="height:100%">
    <v-carousel-item :src="src1" id="img1">
    <v-jumbotron dark>
             <v-container fill-height>
              <v-layout align-center>
             <v-flex>
                  <span class="black--text"><h3 class="display-3">WELCOME TO WORLD OF PUZZLES</h3></span>
              </v-flex>
              </v-layout>
   </v-container>
    </v-jumbotron></v-carousel-item>
 <v-carousel-item :src="src2" id="img2">
  <v-jumbotron dark>
             <v-container fill-height>
              <v-layout align-center>
             <v-flex>
                  <span class="black--text"><h3 class="display-3">DESCRIPTION</h3></span>
              </v-flex>
              </v-layout>
   </v-container>
    </v-jumbotron>
 </v-carousel-item>
<v-carousel-item :src="src3" id="img3" >
<div id="login">
 <v-container grid-list-lg>
    <v-layout column justify-center align-center>
      <v-flex mt-4>
        <v-card  width="350px">
          <v-container
            fluid>
            <v-layout justify-center>
               <v-card-title primary-title>
              <span class="display-1 blue--text">Login</span>
            </v-card-title></v-layout>
            <v-form>
              <v-text-field prepend-icon="person" name="Username" label="Username"></v-text-field>
              <v-text-field prepend-icon="lock" name="Password" label="Password" type="password"></v-text-field>
              <v-flex>
                <v-layout align-center justify-space-around wrap>
                  <v-checkbox label="Remember me"></v-checkbox></v-layout></v-flex>
                  <v-flex>
                  <v-layout justify-center>
                  <router-link to="password-reset">
                    <span class="blue--text"> Forgot Password?</span>
                  </router-link></v-layout>
                 </v-flex>
            </v-form>
            <v-card-actions>
              <v-btn primary round large block color="info">Login</v-btn>
            </v-card-actions>
          </v-container>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</div>
</v-carousel-item>
  </v-carousel>
</v-app>
</template>

<script>
export default{
  name: 'HelloWorld',
  data () {
    return {
      src1: 'https://www.amare.at/wp-content/uploads/2016/04/bgimg3.jpg',
      src2: 'http://blog.visme.co/wp-content/uploads/2017/07/50-Beautiful-and-Minimalist-Presentation-Backgrounds-08.jpg',
      src3: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmSbgRjZMvFGkJsuWhHGETGpGxCCboMkrt83dhQxzRo9TcUTUf'
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

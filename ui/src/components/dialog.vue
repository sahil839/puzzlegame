<template>
 <v-container grid-list-lg>
  <v-layout justify-center>
  <v-flex xs12 sm12>
   <v-card>
     <v-layout justify-center><v-card-title>Rate this Image</v-card-title></v-layout>
     <v-layout row wrap>
     <v-flex xs4 sm4 pl-3><v-card-media :src="img1" height="300px"></v-card-media></v-flex>
     <v-flex xs8 sm8>
     <v-card-content>
       <v-container grid-list-lg>
          <v-layout row wrap>
          <v-flex xs12 v-for="(item,i) in criteria" :key=i>
                <div class="d-flex align-center justify-start">
               <v-flex xs1><label><span style="color:cyan darken-2">{{ item }}</span></label></v-flex>
              <v-flex xs10><v-rating v-model=list[i] @input="store(list[i],i)" length=10 color="cyan dark">
               </v-rating></v-flex>
               <v-flex xs1><label>{{ list[i] }}</label></v-flex>
              </div>
          </v-flex>
          </v-layout>
        </v-container>
      </v-card-content>
      </v-flex>
      </v-layout>
      <v-card-actions>
       <v-layout justify-center pb-2><v-btn v-on:click="save()">Submit</v-btn></v-layout>
      </v-card-actions>
   </v-card>
  </v-flex>
 </v-layout>
 </v-container>
</template>

<script>
export default{
  name: 'rate-page',
  data () {
    return {
      img1: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXbA_HAbV9XrrENtVaEJbYM6Q1vcMWNglwQbK5NCsLe7NhgESV',
      criteria: ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE'],
      list: [0, 0, 0, 0, 0]
    }
  },
  methods: {
    store (value, key) {
      this.list[key] = value
    },
    save () {
      for (var i = 0; i < 5; i++) {
        console.log(this.list[i])
      }
    }
  }
}
</script>

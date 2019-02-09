<template>
  <div id="app">
  <v-toolbar color="cyan dark" id="toolbar" clipped-left>
      <v-toolbar-title >Title</v-toolbar-title>
      <v-spacer></v-spacer>
     <div class="hidden-sm-and-down">
      <v-toolbar-items >
        <v-btn round flat>
        <v-icon>account_circle</v-icon>
        UserName
        </v-btn>
        <template>
          <v-dialog v-model="dialog" width="500" >
                <v-btn round slot="activator" flat ><v-icon>error</v-icon>About</v-btn>
                <v-card >
                <v-card-title primary-title id="dialog" >
                  Rules of the Game
                </v-card-title>
                <v-card-text>
                  India is my country.</v-card-text>
              <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="primary" flat @click="dialog = false">I accept</v-btn>
              </v-card-actions>
              </v-card>
              </v-dialog>
        </template>
        <v-btn round flat>
        <v-icon>settings_power</v-icon>
        logout</v-btn>
      </v-toolbar-items>
      </div>
      <div class="hidden-md-and-up">
      <v-toolbar-items >
        <v-tooltip bottom>
        <v-btn fab slot="activator" flat>
        <v-icon >account_circle</v-icon>
        </v-btn>
        <span>UserName</span>
        </v-tooltip>
          <template>
          <v-dialog v-model="dialog" width="500" >
                <v-tooltip slot="activator" bottom><v-btn fab slot="activator" flat ><v-icon>error</v-icon></v-btn><span>About</span></v-tooltip>
                <v-card >
                <v-card-title primary-title id="dialog" >
                  Rules of the Game
                </v-card-title>
                <v-card-text>
                  India is my country.</v-card-text>
              <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="primary" flat @click="dialog = false">I accept</v-btn>
              </v-card-actions>
              </v-card>
              </v-dialog>
        </template>
        <v-tooltip bottom>
        <v-btn fab slot="activator" flat>
        <v-icon>settings_power</v-icon>
        </v-btn>
        <span>Logout</span>
        </v-tooltip>
      </v-toolbar-items>
      </div>
    </v-toolbar>
  </div>
</template>

<script>

export default{
  name: 'app',
  data () {
    return {
      dialog: false
    }
  }
}

</script>
<style scoped>
@import url('https://fonts.googleapis.com/css?family=Alegreya:900');
#toolbar{
  color:black;
}
#dialog{
 font-family: Algreya;
 font-size: 40px;
}
</style>

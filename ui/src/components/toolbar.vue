<template>
  <div id="app">
  <v-toolbar color="cyan dark" id="toolbar" clipped-left>
      <v-toolbar-title >Title</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn flat>
        <v-icon>account_circle</v-icon>
        UserName
        </v-btn>
        <v-btn flat>
        <v-icon>settings_power</v-icon>
        logout</v-btn>
        <v-btn flat>
        <v-icon>error</v-icon>
        About</v-btn>
      </v-toolbar-items>
      <v-toolbar-items class="hidden-md-and-up">
        <v-tooltip bottom>
        <v-btn slot="activator" flat>
        <v-icon >account_circle</v-icon>
        </v-btn>
        <span>UserName</span>
        </v-tooltip>
        <v-tooltip bottom>
        <v-btn slot="activator" flat>
        <v-icon>settings_power</v-icon>
        </v-btn>
        <span>Logout</span>
        </v-tooltip >
        <v-tooltip bottom>
        <v-btn slot="activator" flat>
        <v-icon>error</v-icon>
        </v-btn>
        <span>About</span>
        </v-tooltip >
      </v-toolbar-items>
    </v-toolbar>
  </div>
</template>

<script>

export default{
  name: 'app'
}

</script>
<style scoped>
#toolbar{
  color:black;
}
</style>

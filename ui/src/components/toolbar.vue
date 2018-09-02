<template>
  <div id="app">
  <v-toolbar color="brown darken-1" id="toolbar">
      <v-toolbar-side-icon></v-toolbar-side-icon>
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
    </v-toolbar>
  </div>
</template>

<script>

export default{
  name:'app',
    data(){
      return
    }
}
</script>
<style scoped>
#toolbar{
  color:black;
}
</style>

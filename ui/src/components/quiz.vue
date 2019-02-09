<template>
  <div id="app">
  <v-app id="inspire">
    <Toolbar></Toolbar>
    <v-container style="max-width:100%" grid-list-xl justify-center>
    <v-layout>
    <v-flex sm12>
    <div style="font-size:35px;" id="question">
    <v-card color="light-blue accent-1" id="">
    <P>
    Here Goes The Question {{i}} to be  asked to the use followed by the options ?
    <v-progress-circular
      :rotate="360"
      :size="90"
      :width="15"
      :value="value"
      color="teal"
    >
      {{ value/10 }}
    </v-progress-circular>
    </p>
    <v-container grid-list-xl>
    <v-flex >
    <v-layout row wrap justify-start>
    <v-radio-group v-model="radioGroup" id="radio">
      <v-radio
        v-for="option in options"
        :key="option"
        :label="option.option"
        :value="option"
      >
      </v-radio>
    </v-radio-group>
    </v-layout>
    </v-flex>
    </v-container>
    </v-card>
    <v-container justify-center grid-list-xl>
    <v-tooltip bottom>
    <v-btn slot="activator" fab dark large color="amber lighten-1">
    <v-icon dark>flash_on</v-icon>
    </v-btn>
    <span>Hint</span>
    </v-tooltip>
    <v-tooltip bottom>
    <v-btn slot="activator" fab dark large color="green accent-3">
    <v-icon dark>check</v-icon>
    </v-btn>
    <span>Submit</span>
    </v-tooltip>
    <v-tooltip bottom>
    <v-btn slot="activator" fab dark large color="red lighten-1">
    <v-icon dark>arrow_forward</v-icon>
    </v-btn>
    <span>Skip</span>
    </v-tooltip>
    </v-container>
    </div>
    </v-flex>
    <v-flex sm6>
    <v-data-table
      :headers="headers"
      :items="users"
      hide-actions
      class="elevation-1"
      disable-initial-sort
    >
      <template slot="items" slot-scope="props" >
        <td style="text-align:left; font-weight:bold;background-color:#E0F7FA;">{{props.item.rank}}</td>
        <td class="text-xs-left" style="background-color:#E0F7FA;">{{ props.item.name }}</td>
        <td class="text-xs-left" style="background-color:#E0F7FA;">{{ props.item.points }}</td>
      </template>
    </v-data-table>
    </v-flex>
    </v-layout>
    </v-container>
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
      interval: {},
      value: 0,
      i: 1,
      headers: [
        {
          text: 'Rank',
          align: 'left',
          value: 'name'
        },
        {
          text: 'Username',
          value: 'username'
        },
        {
          text: 'Points',
          value: 'points'
        }
      ],
      users: [
        {
          value: false,
          rank: '1',
          name: 'user1',
          points: '0'
        },
        {
          value: false,
          rank: '2',
          name: 'user2',
          points: '0'
        },
        {
          value: false,
          rank: '3',
          name: 'user3',
          points: '0'
        },
        {
          value: false,
          rank: '4',
          name: 'user4',
          points: '0'
        }
      ],
      options: [
        {
          number: 'A',
          option: 'option1 option1 option1 option1 option1 option1'
        },
        {
          number: 'B',
          option: 'option2 option2 option2 option2 option2 option2'
        },
        {
          number: 'C',
          option: 'option3 option3 option3 option3 option3 option3'
        },
        {
          number: 'D',
          option: 'option4 option4 option4 option4 option4 option4'
        }
      ]
    }
  },
  beforeDestroy () {
    clearInterval(this.interval)
  },
  mounted () {
    this.interval = setInterval(() => {
      if (this.value === 100) {
        this.i++
        if (this.i === 5) {
          this.i = 0
        }
        return (this.value = 0)
      }
      this.value += 10
    }, 1000)
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Pacifico');
@import url('https://fonts.googleapis.com/css?family=Poiret+One');
#question{
  font-family:'Pacifico';
}
#radio{
  font-size:30px;
  font-weight:bold;
  font-family:'Poiret one';
}
#options{
  font-size:20px;
}
</style>

<template>
  <!-- https://github.com/David-Desmaisons/vue-plotly -->
  <!-- https://david-desmaisons.github.io/vue-plotly/?ref=madewithvuejs.com -->
  <v-row class="fill-height ma-2" no-gutters>
    <v-col cols="12" sm="3" >
      <v-card
      ></v-card>
    </v-col>
    <v-col cols="12" sm="6">
      <v-card>
        <Plotly
        :data="data"
        :layout="layout"
        :display-mode-bar="false"></Plotly>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import { Plotly } from 'vue-plotly'

export default {
  name: 'PlotView',
  components: {
    Plotly,
  },
  data () {
    return {
      data:[{
        x: [1,2,3,4],
        y: [10,15,13,17],
        type:"scatter"
      }],
      layout:{
        title: "My graph"
      }
    }
  },
}
</script>
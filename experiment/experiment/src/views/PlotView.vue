<template>
  <!-- https://github.com/David-Desmaisons/vue-plotly -->
  <!-- https://david-desmaisons.github.io/vue-plotly/?ref=madewithvuejs.com -->
  <Plotly
  :data="data"
  :layout="layout"
  :display-mode-bar="false"></Plotly>
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
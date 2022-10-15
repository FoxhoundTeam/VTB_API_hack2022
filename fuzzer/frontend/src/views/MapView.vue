<template>
  <!-- <v-container no-gutters> -->
    <v-row class="fill-height ma-2" no-gutters>
      <v-col cols="12" sm="3" >
        <v-card
        ></v-card>
      </v-col>
      <v-col cols="12" sm="6">
        <v-card>
        <!-- https://vue2-leaflet.netlify.app/quickstart/#hello-map -->
        <!-- https://github.com/vue-leaflet/Vue2Leaflet -->
        <l-map style="height: 400px" :zoom="zoom" :center="center">
          <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
          <l-marker :lat-lng="markerLatLng"></l-marker>
        </l-map>
      </v-card>
      </v-col>
    </v-row>
  <!-- </v-container> -->
</template>

<script>
// @ is an alias to /src
// import L from 'leaflet';
import { LMap, LTileLayer, LMarker } from "vue2-leaflet";
import "leaflet/dist/leaflet.css";
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: "MapView",
  components: {
    // HelloWorld,
    LMap,
    LTileLayer,
    LMarker,
  },
  data() {
    return {
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 15,
      center: [55.751244, 37.618423],
      markerLatLng: [55.751244, 37.618423],
    };
  },
  mounted() {
    console.log("HelloWorld: mounted()");
    // const element = document.getElementsByClassName('leaflet-attribution-flag')[0];
    // console.log("element = ", element);
    // element.remove(); // Removes the div with the 'div-02' id
    this.removeflag();
  },
  updated() {
    console.log("HelloWorld: updated()");
    this.removeflag();
    // const element = document.getElementsByClassName('leaflet-attribution-flag')[0];
    // console.log("element = ", element);
    // element.remove(); // Removes the div with the 'div-02' id
  },
  methods: {
    removeflag() {
      console.log("HelloWorld: removeflag()");
      const element = document.getElementsByClassName(
        "leaflet-attribution-flag"
      )[0];
      // const element = document.getElementsByClassName('leaflet-attribution-flag')[0];
      console.log("element = ", element);
      // console.log("remove = ", element.remove()); // Removes the div with the 'div-02' id
    },
  },
};
</script>

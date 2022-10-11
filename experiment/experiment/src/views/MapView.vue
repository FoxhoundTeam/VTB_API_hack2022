<template>
  <l-map style="height: 300px" :zoom="zoom" :center="center">
    <l-tile-layer
      :url="url"
      :attribution="attribution"
    ></l-tile-layer>
    <l-marker
      :lat-lng="markerLatLng"
    ></l-marker>
  </l-map>
</template>

<script>
// @ is an alias to /src
// import L from 'leaflet';
import {LMap, LTileLayer, LMarker} from 'vue2-leaflet';
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'MapView',
  components: {
    // HelloWorld,
    LMap,
    LTileLayer,
    LMarker,
  },
  data () {
    return {
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 15,
      center: [51.505, -0.159],
      markerLatLng: [51.504, -0.159]
    }
  },
  mounted(){
    console.log("HelloWorld: mounted()");
    // const element = document.getElementsByClassName('leaflet-attribution-flag')[0];
    // console.log("element = ", element);
    // element.remove(); // Removes the div with the 'div-02' id
    this.removeflag();
  },
  updated(){
    console.log("HelloWorld: updated()");
    this.removeflag();
    // const element = document.getElementsByClassName('leaflet-attribution-flag')[0];
    // console.log("element = ", element);
    // element.remove(); // Removes the div with the 'div-02' id
  },
  methods:{
    removeflag(){
      console.log("HelloWorld: removeflag()");
      const element = document.getElementsByClassName('leaflet-attribution-flag')[0];
      console.log("element = ", element);
      console.log("remove = ", element.remove()); // Removes the div with the 'div-02' id
    },
  }
}
</script>

<template>
  <div v-html="mdContent"></div>
</template>

<script lang="ts">
import Vue from "vue";
import { marked } from "marked";
export default Vue.extend({
  props: {
    source: {
      type: String,
    },
  },
  computed: {
    mdContent(): any {
      return marked(this.source || "");
    },
  },
});
</script>

<style>
</style>
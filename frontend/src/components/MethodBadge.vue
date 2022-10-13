<template>
    <span
          :style="`color: ${methodsColors[method]}`"
          >{{ method }}</span
        >
</template>
<script lang="ts">
import { methodsColors } from "@/constants";
import Vue from "vue";
export default Vue.extend({
    props: {
        method: {
            type: String,
        }
    },
    data() {
        return {
            methodsColors
        }
    }
})
</script>
<style lang="">
    
</style>
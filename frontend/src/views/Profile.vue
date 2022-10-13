<template>
  <v-card title="Профиль">
    <v-card-title>Профиль</v-card-title>
    <v-container fluid>
      <v-row>
        <v-col><profile-settings /></v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
import ProfileSettings from "@/components/forms/ProfileSettings.vue";
import Vue from "vue";
export default Vue.extend({
  components: { ProfileSettings },
});
</script>

<style>
</style>
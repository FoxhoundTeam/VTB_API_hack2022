
<template>
  <div id="app">
    <v-app style="min-height: 100vh">
      <nav-bar />
      <v-main class="m-2">
        <router-view></router-view>
      </v-main>
      <v-dialog v-model="showErrorModalLocal" max-width="300">
        <v-card>
          <v-card-title class="text-h5"> Ошибка </v-card-title>

          <v-card-text>
            {{ errorModalContent }}
          </v-card-text>

          <v-card-actions>
            <v-btn
              color="green darken-1"
              text
              @click="showErrorModalLocal = false"
            >
              OK
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <v-snackbar
        v-model="showSnackbarLocal"
        :color="snackbarColor || 'success'"
        :timeout="2000"
      >
        {{ snackbarText }}

        <template v-slot:action="{ attrs }">
          <v-btn
            color="white"
            text
            v-bind="attrs"
            @click="showSnackbarLocal = false"
          >
            Закрыть
          </v-btn>
        </template>
      </v-snackbar>
      <v-overlay :value="appLoading">
        <v-progress-circular indeterminate size="64"></v-progress-circular>
      </v-overlay>
    </v-app>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { mapMutations, mapState } from "vuex";
import NavBar from "./components/NavBar.vue";

export default Vue.extend({
  components: { NavBar },
  name: "app",
  data() {
    return {
      appLoading: true,
    };
  },
  methods: {
    ...mapMutations(["setShowSnackbar", "setShowErrorModal"]),
  },
  async mounted() {
    this.appLoading = false;
  },
  computed: {
    ...mapState([
      "snackbarText",
      "showSnackbar",
      "snackbarColor",
      "showErrorModal",
      "errorModalContent",
    ]),
    showSnackbarLocal: {
      get(): boolean {
        return this.showSnackbar;
      },
      set(value: boolean): void {
        this.setShowSnackbar(value);
      },
    },
    showErrorModalLocal: {
      get(): boolean {
        return this.showErrorModal;
      },
      set(value: boolean): void {
        this.setShowErrorModal(value);
      },
    },
  },
});
</script>

<style>
a {
  text-decoration: none !important;
}
</style>

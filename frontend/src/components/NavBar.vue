<template>
  <v-app-bar app>
    <v-app-bar-title
      ><router-link
        :to="{ name: 'Index' }"
        class="text-decoration-none text-dark text-no-wrap"
        >FoxBench</router-link
      ></v-app-bar-title
    >
    <v-spacer></v-spacer>
    <v-btn v-if="!isAuthenticated" color="primary" text :to="{ name: 'Login' }"
      >Войти</v-btn
    >
    <div v-if="isAuthenticated">
      <v-menu open-on-hover bottom offset-y>
        <template v-slot:activator="{ on, attrs }">
          <v-btn text class="text-dark" dark v-bind="attrs" v-on="on"
            ><v-icon left dark> mdi-account </v-icon>
            {{ user.email }}
          </v-btn>
        </template>
        <v-list>
          <v-list-item link :to="{ name: 'Profile' }">
            <v-list-item-title>Профиль</v-list-item-title>
          </v-list-item>
          <v-list-item link :to="{ name: 'UploadAPI' }">
            <v-list-item-title>Загрузить API</v-list-item-title>
          </v-list-item>
          <v-list-item link :to="{ name: 'Fuzzing' }">
            <v-list-item-title>Fuzzing</v-list-item-title>
          </v-list-item>
          <v-list-item link>
            <v-list-item-title @click="logout">Выйти</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </div>
  </v-app-bar>
</template>

<script lang="ts">
import Vue from "vue";
import { mapActions, mapState } from "vuex";

export default Vue.extend({
  data() {
    return {};
  },
  computed: {
    ...mapState({
      user: (state: any) => state.auth.user,
      isAuthenticated: (state: any) => state.auth.isAuthenticated,
    }),
  },
  methods: {
    async logout() {
      await this.logoutDispatch();
      location.reload();
    },
    ...mapActions({
      logoutDispatch: "logout",
    }),
  },
});
</script>

<style>
.v-app-bar-title__content {
  width: 200px !important;
}
</style>
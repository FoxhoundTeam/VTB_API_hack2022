<template>
  <v-card elevation="0">
    <v-form v-model="valid">
      <v-text-field
        label="Почта"
        :rules="[rules.required, rules.isEmail]"
        v-model="email"
        validate-on-blur
      ></v-text-field>
      <v-text-field
        v-model="password"
        label="Пароль"
        :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
        :rules="[rules.required]"
        :type="showPassword ? 'text' : 'password'"
        validate-on-blur
        @click:append="showPassword = !showPassword"
        @keyup.enter="login"
      ></v-text-field>
      <v-btn @click="login" :disabled="!valid" block color="primary"
        >Войти</v-btn
      >
    </v-form>
  </v-card>
</template>

<script lang="ts">
import { mapActions, mapState } from "vuex";
import { required, isEmail } from "@/validators";
import Vue from "vue";

export default Vue.extend({
  data() {
    return {
      email: "",
      password: "",
      showPassword: false,
      valid: false,
      rules: {
        required,
        isEmail,
      },
    };
  },
  computed: {
    ...mapState(["isAuthenticated"]),
  },
  methods: {
    ...mapActions({ loginDispatch: "login" }),
    async login() {
      await this.loginDispatch({
        email: this.email,
        password: this.password,
      });
      if (this.$route.query.redirect) {
        this.$router.replace({ path: this.$route.query.redirect as string });
      }
      this.$router.replace({ name: "Index" });
    },
  },
  beforeMount() {
    if (this.isAuthenticated) {
      this.$router.replace({ name: "Index" });
    }
  },
});
</script>

<style>
.temp {
  width: 80px;
}
</style>
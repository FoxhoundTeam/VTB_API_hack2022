<template>
  <v-card elevation="0">
    <v-card-title>Настройки профиля</v-card-title>
    <v-container fluid>
      <v-form v-model="emailValid">
        <v-text-field
          label="Почта"
          :rules="[rules.required, rules.isEmail]"
          v-model="email"
          validate-on-blur
        ></v-text-field>

        <v-btn @click="save" :disabled="!emailValid" block color="primary"
          >Сохранить</v-btn
        >
      </v-form>
      <v-form v-model="passwordValid">
        <v-text-field
          v-model="password"
          label="Пароль"
          :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
          :rules="[rules.required]"
          :type="showPassword ? 'text' : 'password'"
          validate-on-blur
          @click:append="showPassword = !showPassword"
        ></v-text-field>
        <v-text-field
          v-model="password2"
          label="Пароль ещё раз"
          :append-icon="showPassword2 ? 'mdi-eye' : 'mdi-eye-off'"
          :rules="[rules.required, rules.matchPassword]"
          :type="showPassword2 ? 'text' : 'password'"
          @click:append="showPassword2 = !showPassword2"
        ></v-text-field>

        <v-btn
          @click="changePassword"
          :disabled="!passwordValid"
          block
          color="primary"
          >Сменить пароль</v-btn
        >
      </v-form>
    </v-container>
  </v-card>
</template>

<script lang="ts">
import Vue from "vue";
import { mapActions, mapState } from "vuex";
import { required, isEmail, passwordsMatches } from "@/validators";

export default Vue.extend({
  data() {
    return {
      email: null,
      loadingEmail: false,
      loadingPassword: false,
      password: "",
      password2: "",
      showPassword: false,
      showPassword2: false,
      emailValid: false,
      passwordValid: false,
    };
  },
  computed: {
    ...mapState(["user"]),
    rules() {
      return {
        matchPassword: (v: string) => passwordsMatches(this.password, v),
        required,
        isEmail,
      };
    },
  },
  beforeMount() {
    this.email = this.user.email;
  },
  methods: {
    ...mapActions(["updateUserInfo", "changeUserPassword"]),
    async save(): Promise<void> {
      this.loadingEmail = true;
      await this.updateUserInfo({
        email: this.email,
      });
      this.loadingEmail = false;
    },
    async changePassword(): Promise<void> {
      this.loadingPassword = true;
      await this.changeUserPassword({
        password: this.password,
        password2: this.password2,
      });
      this.loadingPassword = false;
    },
  },
});
</script>

<style>
</style>
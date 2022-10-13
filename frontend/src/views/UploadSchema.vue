<template>
  <v-card>
    <v-card-title>Загрузка API схемы</v-card-title>
    <v-card-text>
      <v-form v-model="valid" enctype="multipart/form-data">
        <v-file-input
          accept=".yml,.yaml"
          label="Open api файл"
          :rules="rules"
          v-model="file"
        ></v-file-input>
        <v-btn :disabled="!valid" @click="load">Загрузить</v-btn>
      </v-form>
    </v-card-text>
  </v-card>
</template>
<script lang="ts">
import Vue from "vue";
import { required } from "@/validators";
import http from "@/http";
import axios from "axios";
import { mapMutations } from "vuex";
export default Vue.extend({
  data() {
    return {
      valid: false,
      rules: [required],
      file: null,
    };
  },
  methods: {
    ...mapMutations(["showSnackbar"]),
    async load() {
      if (!this.file) return;
      const form = new FormData();
      form.append("file", this.file);
      try {
        await axios.post("/api/api/upload/", form, {
          headers: http.getHeaders(),
        });
        this.showSnackbar({
          text: "API успешно загружено",
        });
      } catch (error: any) {
        this.showSnackbar({
          text: error.response.data.detail || "Что-то пошло не так",
          color: "warning",
        });
      }
    },
  },
});
</script>
<style>
</style>
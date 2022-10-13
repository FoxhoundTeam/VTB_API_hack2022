<template>
  <v-card>
    <v-card-text>
      <v-select
        v-model="language"
        label="Выберите язык"
        :items="languages"
      ></v-select>
      <highlightjs v-if="lang" :lang="lang" :code="code" />
      <v-btn block color="primary" @click="copyToClipboard"
        >Скопировать <v-icon right>mdi-content-copy</v-icon></v-btn
      >
    </v-card-text>
  </v-card>
</template>

<script lang="ts">
import Vue from "vue";
import { CodeGen, Language, MdCodeSupport } from "@/code_gen";
import { mapMutations } from "vuex";
export default Vue.extend({
  props: {
    url: {
      type: String,
    },
    queryParams: {
      type: Object,
      default: undefined,
    },
    pathParams: {
      type: Object,
      default: undefined,
    },
    body: {
      type: Object,
      default: undefined,
    },
    method: {
      type: String,
    },
  },
  data() {
    return {
      language: Language.PYTHON,
      languages: Object.values(Language),
    };
  },
  computed: {
    codeGen(): CodeGen {
      return new CodeGen();
    },
    lang(): string {
      return MdCodeSupport[this.language];
    },
    code(): string {
      return this.codeGen.generateCode({
        urlTemplate: this.url,
        method: this.method,
        language: this.language,
        isMd: false,
        queryParams: this.queryParams,
        body: this.body,
        pathParams: this.pathParams,
      });
    },
  },
  methods: {
    ...mapMutations(["showSnackbar"]),
    async copyToClipboard() {
      await navigator.clipboard.writeText(this.code);
      this.showSnackbar({ text: "Значение успешно скопировано" });
    },
  },
});
</script>

<style>
code {
  border-radius: 0 !important;
  background: #1e1e1e !important;
  color: #dcdcdc !important;
  font-size: 100% !important;
}
</style>
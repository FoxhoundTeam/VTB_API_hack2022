<template>
  <v-card>
    <v-card-text>
      <v-select v-model="language" label="Выберите язык" :items="languages"></v-select>
      <markdown :source="code" />
    </v-card-text>
  </v-card>
</template>

<script lang="ts">
import Vue, { PropType } from "vue";
import Markdown from "@/components/Markdown.vue";
import { CodeGen, Language, Method } from "@/code_gen";
export default Vue.extend({
  props: {
    url: {
      type: String,
    },
    params: {
      type: Object,
    },
    method: {
      type: Object as PropType<Method>,
    },
  },
  data() {
    return {
      language: Language.Python,
      languages: Object.values(Language).filter((v: string | number) => isNaN(Number(v))),
    };
  },
  components: { Markdown },
  computed: {
    codeGen(): CodeGen {
      return new CodeGen(this.url);
    },
    code(): string {
      return this.codeGen.generateCode(
        this.method,
        this.language,
        this.params,
        true
      );
    },
  },
});
</script>

<style>
</style>
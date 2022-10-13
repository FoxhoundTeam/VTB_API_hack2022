<template>
  <v-toolbar flat>
    <v-select
      :items="apis"
      return-object
      v-model="api"
      item-text="name"
      outlined
      dense
      class="api-select"
      label="API"
    ></v-select>
    <v-select
      :items="api.versions"
      return-object
      v-model="version"
      item-text="name"
      outlined
      dense
      :disabled="!Object.keys(api).length"
      class="ml-2 version-select"
      label="Версия"
    ></v-select>

    <v-spacer></v-spacer>
    <!-- <v-text-field label="Поиск" outlined dense /> -->
  </v-toolbar>
</template>

<script lang="ts">
import { Api, ApiVersion } from "@/types";
import Vue from "vue";
import { mapActions, mapGetters, mapMutations, mapState } from "vuex";
export default Vue.extend({
  data() {
    return {
      versions: [] as ApiVersion[],
    };
  },
  computed: {
    ...mapState({
      apis: (state: any): Api[] => state.api.apis,
      selectedApi: (state: any): Api => state.api.selectedApi,
      selectedVersion: (state: any): ApiVersion => state.api.selectedVersion,
    }),
    ...mapGetters(["apiByCode"]),
    api: {
      get(): Api {
        return this.$store.state.api.selectedApi;
      },
      set(value: Api) {
        this.setSelectedApi(value);
      },
    },
    version: {
      get(): ApiVersion {
        return this.selectedVersion;
      },
      set(value: ApiVersion) {
        this.setSelectedVersion(value);
        if (
          this.$route.params.apiCode == this.api.code &&
          this.$route.params.versionCode == value.code
        )
          return;
        this.$router.push({
          name: "IndexWithParams",
          params: { apiCode: this.api.code, versionCode: value.code },
        });
      },
    },
  },
  methods: {
    ...mapMutations(["setSelectedApi", "setSelectedVersion"]),
    ...mapActions(["getPages", "getApis"]),
    setApiAndVersion() {
      if (this.$route.params.apiCode && this.$route.params.versionCode) {
        this.api = this.apiByCode(this.$route.params.apiCode);
        this.version = this.api.versions.find(
          (v) => v.code == this.$route.params.versionCode
        ) as ApiVersion;
      }
    },
  },
  watch: {
    async version() {
      await this.getPages();
    },
    $route() {
      this.setApiAndVersion();
    },
  },
  async mounted() {
    await this.getApis();
    this.setApiAndVersion();
  },
});
</script>

<style>
.version-select {
  max-width: 100px !important;
}
.api-select {
  max-width: 250px !important;
}
</style>
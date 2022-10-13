<template>
  <v-dialog v-model="showDialog" width="400px">
    <v-card>
      <v-text-field
        prepend-inner-icon="mdi-search"
        label="Поиск"
        solo
        v-model="search"
      ></v-text-field>
      <v-card-text>
        <v-list dense v-for="page in filteredPages" :key="page.id">
          <v-list-item-group color="primary">
            <v-subheader v-if="!page.parent">{{ page.name }}</v-subheader>
            <v-list-item v-else selectable @click="setActivePage(page)">
              <v-list-item-content>
                <v-list-item-title v-text="page.name"></v-list-item-title>
              </v-list-item-content>
              <method-badge v-if="page.method" :method="page.method" />
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script lang="ts">
import { Page } from "@/types";
import Vue from "vue";
import { mapState } from "vuex";
import MethodBadge from "../MethodBadge.vue";
export default Vue.extend({
  components: { MethodBadge },
  props: {
    value: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      search: "",
    };
  },
  methods: {
    setActivePage(page: Page) {
      this.showDialog = false;
      this.$router.push({
        name: this.$route.name as string,
        params: this.$route.params,
        query: { ...this.$route.query, page: page.id },
      });
    },
  },
  computed: {
    ...mapState({
      pages: (state: any): Page[] => state.api.pages,
    }),
    showDialog: {
      get(): boolean {
        return this.value;
      },
      set(value: boolean) {
        this.$emit("input", value);
      },
    },
    filteredPages(): Page[] {
      if (this.search === "") return this.pages;
      return this.pages.filter(
        (v: Page) =>
          v.name.toLowerCase().includes(this.search.toLowerCase()) || !v.parent
      );
    },
  },
});
</script>

<style>
</style>
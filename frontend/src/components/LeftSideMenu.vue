<template>
  <div>
    <v-btn @click="showDialog = true" text outlined>Перейти к</v-btn>
    <v-treeview
      ref="tree"
      dense
      :active.sync="activePage"
      :open.sync="open"
      rounded
      hoverable
      activatable
      disable-per-node
      :items="pagesTree"
      open-all
    >
      <template v-slot:append="{ item }">
        <method-badge v-if="item.method" :method="item.method"/>
      </template>
    </v-treeview>
    <flat-sections-modal v-model="showDialog" />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { mapGetters, mapMutations, mapState } from "vuex";
import { Page, PageTree } from "@/types";
import FlatSectionsModal from "@/components/modals/FlatSectionsModal.vue";
import MethodBadge from "./MethodBadge.vue";
export default Vue.extend({
  components: {
    FlatSectionsModal,
    MethodBadge,
  },
  data() {
    return {
      showDialog: false,
      open: [] as string[],
    };
  },
  methods: {
    ...mapMutations(["setSelectedPage"]),
  },
  watch: {
    pagesTree() {
      this.open = this.pagesTree.map(v => v.id);
    },
  },
  computed: {
    ...mapState({
      pagesTree: (state: any): PageTree[] => state.api.pagesTree,
      selectedPage: (state: any): Page => state.api.selectedPage,
    }),
    ...mapGetters(["pageById"]),
    activePage: {
      get(): string[] {
        return this.selectedPage.id ? [this.selectedPage.id] : [];
      },
      set(value: string[]) {
        this.setSelectedPage(this.pageById(value[0]) || {});
      },
    },
  },
});
</script>

<style>
</style>
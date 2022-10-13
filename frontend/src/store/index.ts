import Vuex, { StoreOptions } from "vuex";
import Vue from "vue";
import { authModule } from "./auth";
import { utilsModule } from "./utils";
import { apiModule } from "./api";
import { IRootState } from "./types/rootState";

Vue.use(Vuex);

const store: StoreOptions<IRootState> = {
  modules: {
    auth: authModule,
    utils: utilsModule,
    api: apiModule,
  },
  state: {} as IRootState,
  getters: {},
  mutations: {},
  actions: {},
};

export default new Vuex.Store<IRootState>(store);

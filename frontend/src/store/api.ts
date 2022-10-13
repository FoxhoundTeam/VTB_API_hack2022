import http from "@/http";
import { Api, ApiVersion, Page, PageTree } from "@/types";
import { Module } from "vuex";
import { IRootState, IApiState } from "./types";

export const apiModule: Module<IApiState, IRootState> = {
  state: () => ({
    pages: [],
    apis: [],
    pagesTree: [],
    loadingPages: false,
    selectedApi: {} as Api,
    selectedPage: {} as Page,
    selectedVersion: {} as ApiVersion,
  }),
  getters: {
    pageById: (state) => (id: string) => state.pages.find((v) => v.id == id),
    apiByCode: (state) => (code: string) =>
      state.apis.find((v) => v.code == code),
  },
  mutations: {
    setPages(state, pages: Page[]) {
      state.pages = pages;
    },
    setPagesTree(state, pagesTree: PageTree[]) {
      state.pagesTree = pagesTree;
    },
    setApis(state, apis: Api[]) {
      state.apis = apis;
    },
    setSelectedApi(state, api: Api) {
      state.selectedApi = api;
    },
    setSelectedVersion(state, selectedVersion: ApiVersion) {
      state.selectedVersion = selectedVersion;
    },
    setSelectedPage(state, selectedPage: Page) {
      state.selectedPage = selectedPage;
    },
    setLoadingPages(state, value: boolean) {
      state.loadingPages = value;
    },
  },
  actions: {
    async getApis({ commit }) {
      const response = await http.getList<Api[]>("Api", {
        showSnackbar: true,
      });
      if (response.status != 200) return;
      commit("setApis", response.data);
    },
    async getPages({ commit, state }) {
      if (!state.selectedVersion) return;
      commit("setPages", []);
      commit("setLoadingPages", true);
      const responsePages = await http.getList<Page[]>("Page", {
        filters: { version: state.selectedVersion.id },
        showSnackbar: true,
      });
      if (responsePages.status == 200) commit("setPages", responsePages.data);
      const responsePagesTree = await http.getList<PageTree[]>("PageTree", {
        filters: { version: state.selectedVersion.id },
        showSnackbar: true,
      });
      if (responsePagesTree.status == 200)
        commit("setPagesTree", responsePagesTree.data);
      commit("setLoadingPages", true);
    },
  },
};

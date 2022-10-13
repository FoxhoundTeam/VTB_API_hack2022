import { IShowSnackbar, TErrorModalContent } from "@/types";
import { Module } from "vuex";
import { IRootState, IUtilsState } from "./types";

export const utilsModule: Module<IUtilsState, IRootState> = {
  state: () => ({
    showErrorModal: false,
    showSnackbar: false,
  }),
  mutations: {
    showErrorModal(state, content: TErrorModalContent) {
      state.errorModalContent = content;
      state.showErrorModal = true;
    },
    setShowErrorModal(state, value: boolean) {
      state.showErrorModal = value;
    },
    showSnackbar(state, content: IShowSnackbar) {
      state.snackbarColor = content.color || "success";
      state.snackbarText = content.text;
      state.showSnackbar = true;
    },
    setShowSnackbar(state, value: boolean) {
      state.showSnackbar = value;
    },
  },
};

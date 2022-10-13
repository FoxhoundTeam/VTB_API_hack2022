import {
  User,
  IShowSnackbar,
  ChangeUserPasswordData,
  LoginData,
  RegisterData,
  ILoginResponse,
} from "@/types";
import http from "@/http";
import { Module } from "vuex";
import { IRootState, IAuthModuleState } from "./types";

export const authModule: Module<IAuthModuleState, IRootState> = {
  state: () => ({ user: {} as User, isAuthenticated: false }),
  mutations: {
    setUser(state, user: User) {
      state.user = user;
    },
    setAuthenticated(state, isAuthenticated: boolean) {
      state.isAuthenticated = isAuthenticated;
    },
  },
  actions: {
    async updateUserInfo({ commit }, userData: User) {
      const response = await http.partialUpdateItem<User>("User", {
        data: userData,
        showSnackbar: true,
      });
      if (response.status != 200) return;
      commit("setUser", response.data);
      commit("showSnackbar", {
        text: "Данные успешно сохранены",
      } as IShowSnackbar);
    },
    async changeUserPassword({ commit }, content: ChangeUserPasswordData) {
      const response = await http.createItem("ChangePassword", {
        data: content,
        showSnackbar: true,
      });
      if (response.status != 200) return;
      commit("showSnackbar", {
        text: "Пароль успешно изменен",
      } as IShowSnackbar);
    },
    async login({ dispatch }, credentials: LoginData) {
      const response = await http.createItem<ILoginResponse>("Login", {
        data: credentials,
        showSnackbar: true,
      });
      if (response.status == 200) {
        localStorage.setItem("accessToken", response.data.accessToken);
      }
      await dispatch("checkAuth");
    },
    async logout({ commit }) {
      localStorage.removeItem("accessToken");
      commit("setAuthenticated", false);
      commit("setUser", {});
    },
    async register({ dispatch }, credentials: RegisterData) {
      const response = await http.createItem<ILoginResponse>("Register", {
        data: credentials,
        showSnackbar: true,
      });
      if (response.status == 201) {
        localStorage.setItem("accessToken", response.data.accessToken);
      }
      await dispatch("checkAuth");
    },
    async checkAuth({ commit }) {
      const result = await http.getItem<User>("User");
      if (result.status != 200) {
        commit("setUser", {});
      } else {
        commit("setAuthenticated", true);
        commit("setUser", result.data);
      }
    },
  },
};

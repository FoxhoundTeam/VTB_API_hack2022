import Axios, { AxiosResponse } from "axios";
import Vue from "vue";
import store from "./store";

export type TFilters = Record<string, number | string | object | boolean>;

export type THttpOptions = {
  showModal?: boolean;
  showSnackbar?: boolean;
};
export type THttpGetListOptions = {
  filters?: TFilters;
} & THttpOptions;
export type THttpCreateItemOptions = {
  data?: Record<string, any>;
} & THttpOptions;
export type THttpGetOrDeleteItemOptions = {
  id?: number;
} & THttpOptions;
export type THttpUpdateItemOptions = THttpCreateItemOptions &
  THttpGetOrDeleteItemOptions;

export default {
  urls: {
    User: "/api/users/user/",
    Login: "/api/auth/sign-in/",
    ChangePassword: "/api/auth/change-password/",
    Api: "/api/api/",
    Page: "/api/page/",
    PageTree: "/api/page/tree/",
  } as Record<string, string>,
  getFilterValues: function (filters: TFilters | undefined) {
    if (!filters) return "";
    let filter = "";
    if (Object.keys(filters).length != 0) {
      filter = "?";
      for (const key in filters) {
        const element = filters[key];
        filter += `${key}=${element}&`;
      }
      filter = filter.slice(0, filter.lastIndexOf("&"));
    }
    return filter;
  },
  getUrl(url_name: string, id?: number): string {
    let url = this.urls[url_name] || url_name;
    if (id) {
      url = `${url}${id}/`;
    }
    return url;
  },
  catchError(error: any, options: THttpOptions) {
    const raiseException = options?.showModal || options?.showSnackbar;
    if (raiseException) {
      options?.showModal
        ? store.commit("showErrorModal", error.response.data)
        : store.commit("showSnackbar", {
            text: error.response.data.detail || "Что-то пошло не так",
            color: "warning",
          });
    }
    return raiseException as boolean;
  },
  getHeaders() {
    return {
      Authorization: localStorage.getItem("accessToken") as string,
    };
  },
  getList: async function <T>(
    url_name: string,
    options?: THttpGetListOptions
  ): Promise<AxiosResponse<T>> {
    const filter = this.getFilterValues(options?.filters);
    try {
      return await Axios.get(`${this.getUrl(url_name)}${filter}`, {
        headers: this.getHeaders(),
      });
    } catch (error: any) {
      this.catchError(error, {
        showModal: options?.showModal,
        showSnackbar: options?.showSnackbar,
      });
      return error.response;
    }
  },
  getItem: async function <T>(
    url_name: string,
    options?: THttpGetOrDeleteItemOptions
  ): Promise<AxiosResponse<T>> {
    try {
      return await Axios.get(this.getUrl(url_name, options?.id), {
        headers: this.getHeaders(),
      });
    } catch (error: any) {
      this.catchError(error, {
        showModal: options?.showModal,
        showSnackbar: options?.showSnackbar,
      });
      return error.response;
    }
  },
  createItem: async function <T>(
    url_name: string,
    { data, showModal, showSnackbar }: THttpCreateItemOptions
  ): Promise<AxiosResponse<T>> {
    try {
      return await Axios.post(this.getUrl(url_name), data, {
        headers: this.getHeaders(),
      });
    } catch (error: any) {
      this.catchError(error, {
        showModal,
        showSnackbar,
      });
      return error.response;
    }
  },
  partialUpdateItem: async function <T>(
    url_name: string,
    { id, data, showModal, showSnackbar }: THttpUpdateItemOptions
  ): Promise<AxiosResponse<T>> {
    try {
      return await Axios.patch(this.getUrl(url_name, id), data, {
        headers: this.getHeaders(),
      });
    } catch (error: any) {
      this.catchError(error, {
        showModal,
        showSnackbar,
      });
      return error.response;
    }
  },
  updateItem: async function <T>(
    url_name: string,
    { id, data, showModal, showSnackbar }: THttpUpdateItemOptions
  ): Promise<AxiosResponse<T>> {
    try {
      return await Axios.put(this.getUrl(url_name, id), data, {
        headers: this.getHeaders(),
      });
    } catch (error: any) {
      this.catchError(error, {
        showModal,
        showSnackbar,
      });
      return error.response;
    }
  },
  deleteItem: async function <T>(
    url_name: string,
    { id, showModal, showSnackbar }: THttpGetOrDeleteItemOptions
  ): Promise<AxiosResponse<T>> {
    try {
      return await Axios.delete(this.getUrl(url_name, id), {
        headers: this.getHeaders(),
      });
    } catch (error: any) {
      this.catchError(error, {
        showModal,
        showSnackbar,
      });
      return error.response;
    }
  },
};

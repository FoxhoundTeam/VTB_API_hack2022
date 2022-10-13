import { TErrorModalContent, TSnackbarColor } from "@/types";

export interface IUtilsState {
  showErrorModal: boolean;
  errorModalContent?: TErrorModalContent;
  snackbarColor?: TSnackbarColor;
  showSnackbar: boolean;
  snackbarText?: string;
}

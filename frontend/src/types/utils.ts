export type TErrorModalContent = string | string[] | null;
export type TSnackbarColor = "warning" | "success" | "primary" | "red" | null;
export interface IShowSnackbar {
  text: string;
  color: TSnackbarColor;
}

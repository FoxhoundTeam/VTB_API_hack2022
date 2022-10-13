import { IApiState } from "./api";
import { IAuthModuleState } from "./auth";
import { IUtilsState } from "./utils";

export interface IRootState {
  auth: IAuthModuleState;
  utils: IUtilsState;
  api: IApiState;
}

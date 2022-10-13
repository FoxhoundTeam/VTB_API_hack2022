import { User } from "@/types";

export interface IAuthModuleState {
  user: User;
  isAuthenticated: boolean;
}

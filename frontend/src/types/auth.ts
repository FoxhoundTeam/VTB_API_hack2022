export interface User {
  id: number;
  email: string;
}

export type LoginData = {
  email: string;
  password: string;
};

export type RegisterData = {
  role: string | null;
  password2: string;
} & LoginData;

export type ChangeUserPasswordData = {
  password: string;
  password2: string;
};

export interface ILoginResponse {
  accessToken: string;
}

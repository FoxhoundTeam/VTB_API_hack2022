export const required = (value: any) => !!value || "Данное поле обязательно.";
export const isEmail = (v: string) =>
  !v ||
  /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,4})+$/.test(v) ||
  "Введите корректный email.";
export const passwordsMatches = (password1: string, password2: string) =>
  password1 == password2 || "Пароли не совпадают";

export * from "./auth";
export * from "./utils";
export * from "./api";

export type PaginatedResponse<T> = {
  page: number;
  items: T[];
  next?: boolean;
  total: number;
  size: number;
};

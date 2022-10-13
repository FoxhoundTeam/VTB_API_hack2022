export interface Response {
  description: string;
  body: Record<string, string>;
}

export interface BasePage {
  id: string;
  name: string;
  method?: "GET" | "POST" | "PATCH" | "PUT" | "DELETE" | "OPTIONS" | "HEAD";
  parent: string;
}

export type Page = {
  path: string;
  text_content: string;
  parameters?: Record<string, any>[];
  responses?: Record<string, Response>;
  need_request: boolean;
  order: number;
  produces: string[];
  operation_id?: string;
} & BasePage;

export type PageTree = {
  children?: Page[];
} & BasePage;

export interface ApiVersion {
  id: string;
  name: string;
  code: string;
}
export interface Api {
  id: string;
  name: string;
  code: string;
  versions: ApiVersion[];
}

import { ApiVersion, Api, Page, PageTree } from "@/types";

export interface IApiState {
  apis: Api[];
  pages: Page[];
  pagesTree: PageTree[];
  selectedApi?: Api;
  selectedVersion?: ApiVersion;
  selectedPage?: Page;
  loadingPages: boolean;
}

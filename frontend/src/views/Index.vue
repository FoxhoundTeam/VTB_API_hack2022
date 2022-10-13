<template>
  <v-container fluid>
    <v-row
      ><v-col><api-selector /></v-col
    ></v-row>
    <v-row>
      <v-col cols="3"><left-side-menu /></v-col>
      <v-col cols="6"
        ><v-card flat>
          <v-card-title>{{ page.name }}</v-card-title>
          <v-card-subtitle v-if="page.path"
            ><method-badge :method="page.method" />
            {{ page.path }}</v-card-subtitle
          >
          <v-card-text>
            <markdown :source="page.text_content || ''" />
            <map-view v-if="page.path == '/banks'" />
            <v-slider v-if="page.path == '/banks'" />
            <div v-if="queryParams">
              <v-divider />
              <v-card-title class="text-dark">Параметры запроса</v-card-title>
              <json-forms
                :data="queryForm"
                :schema="queryParams"
                :renderers="renderers"
                @change="setQueryForm"
              />
            </div>
            <div v-if="pathParams">
              <v-divider />
              <v-card-title class="text-dark">Параметры пути</v-card-title>
              <json-forms
                :data="pathForm"
                :schema="pathParams"
                :renderers="renderers"
                @change="setPathForm"
              />
            </div>
            <div v-if="bodySchema">
              <v-divider />
              <v-expansion-panels>
                <v-expansion-panel>
                  <v-expansion-panel-header>
                    Тело запроса
                  </v-expansion-panel-header>
                  <v-expansion-panel-content>
                    <json-forms
                      :data="bodyForm"
                      :schema="bodySchema"
                      :renderers="renderers"
                      @change="setBodyForm"
                    />
                  </v-expansion-panel-content>
                </v-expansion-panel>
              </v-expansion-panels>
            </div>
            <div v-if="page.responses">
              <v-divider />
              <v-card-title class="text-dark">Ответы</v-card-title>
              <v-expansion-panels>
                <v-expansion-panel
                  v-for="(response, status) in page.responses"
                  :key="status"
                >
                  <v-expansion-panel-header>
                    {{ status }}
                  </v-expansion-panel-header>
                  <v-expansion-panel-content>
                    <json-forms
                      :data="exampleGenerator(response.body)"
                      :schema="response.body"
                      :renderers="renderers"
                      :readonly="true"
                      v-if="response.body"
                    />
                    <p v-else>Нет тела ответа</p>
                  </v-expansion-panel-content>
                </v-expansion-panel>
              </v-expansion-panels>
            </div>
          </v-card-text>
        </v-card></v-col
      >
      <v-col cols="3">
        <code-editor
          v-if="page.method"
          :method="page.method"
          :pathParams="pathForm"
          :queryParams="queryForm"
          :body="bodyForm"
          :url="api.url + page.path"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import ApiSelector from "@/components/ApiSelector.vue";
import CodeEditor from "@/components/CodeEditor.vue";
import LeftSideMenu from "@/components/LeftSideMenu.vue";
import { Page } from "@/types";
import { mapState } from "vuex";
import Markdown from "@/components/Markdown.vue";
import { JsonForms, JsonFormsChangeEvent } from "@jsonforms/vue2";
import { vuetifyRenderers } from "@jsonforms/vue2-vuetify";
import { defineComponent } from "vue";
import MethodBadge from "@/components/MethodBadge.vue";
import { exampleGenerator } from "@/examplesGenerator";
import MapView from "@/components/MapView.vue";

const renderers = [...vuetifyRenderers];
export default defineComponent({
  name: "Index",
  components: {
    Markdown,
    ApiSelector,
    CodeEditor,
    LeftSideMenu,
    JsonForms,
    MethodBadge,
    MapView,
  },
  data() {
    return {
      queryForm: {},
      pathForm: {},
      bodyForm: {},
      renderers: Object.freeze(renderers),
      exampleGenerator,
    };
  },
  computed: {
    ...mapState({
      page: (state: any): Page => state.api.selectedPage,
      api: (state: any): Page => state.api.selectedApi,
    }),
    pathParams(): Record<string, any> | null {
      return this.buildParams("path");
    },
    queryParams(): Record<string, any> | null {
      return this.buildParams("query");
    },
    bodySchema(): Record<string, any> | undefined {
      return this.page.parameters?.find((v) => v.in == "body")?.schema;
    },
  },
  methods: {
    buildParams(in_: string): Record<string, any> | null {
      const params = this.page.parameters?.filter((v) => v.in == in_);
      if (!params?.length) return null;
      const properties = {} as Record<string, any>;
      const required = params.filter((v) => v.required).map((v) => v.name);
      for (const param of params) {
        if (param.schema) {
          properties[param.name] = param.schema;
        } else {
          if (param.required !== undefined) delete param.required;
          properties[param.name] = param;
        }
      }
      return {
        title: `${in_.charAt(0).toUpperCase() + in_.slice(1)} params`,
        type: "object",
        required: required,
        properties: properties,
      };
    },
    setQueryForm(event: JsonFormsChangeEvent) {
      this.queryForm = event.data;
    },
    setPathForm(event: JsonFormsChangeEvent) {
      this.pathForm = event.data;
    },
    setBodyForm(event: JsonFormsChangeEvent) {
      console.log(event.data);

      this.bodyForm = event.data;
    },
  },
});
</script>

<style>
</style>
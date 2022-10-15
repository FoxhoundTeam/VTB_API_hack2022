<template>
  <v-row class="ma-1 fill-height">
    <v-col cols="12" sm="3">
      <v-card class="fill-height">
        <v-toolbar>
          <v-toolbar-title>Управление</v-toolbar-title>
        </v-toolbar>
        <!-- начать фаззинг -->
        <v-row class="justify-center ma-1">
          <v-btn
            class="primary ma-1"
            @click="start()"
            :disabled="selected_apis == undefined"
          >
            <v-icon>mdi-play</v-icon>
            Старт
          </v-btn>

          <!-- остановить фаззинг -->
          <v-btn class="error ma-1" disabled>
            <v-icon>mdi-stop</v-icon>
            Стоп
          </v-btn>
        </v-row>

        <v-row class="ma-1">
          <!-- ход фаззинга -->
          <v-progress-linear
            :indeterminate="in_progress"
            height="25">
          </v-progress-linear>
        </v-row>

        <v-row class="ma-1">
          <!-- поле фильтрации и поиска -->
          <v-text-field
            label="Фильтр"
            filled
            rounded
            clearable
            dense
            hide-details="true"
            class="ma-1"
            v-model="searchstring"
          ></v-text-field>

          <!-- список api -->
          <v-list>
            <v-list-item-group
              v-model="selected_apis"
              color="primary"
            >
              <v-list-item
                v-for="(item, i) in api_model.paths"
                :key="i"
                two-line
                :disabled="Object.keys(item)[0]=='not_supported'"
              >
                <v-list-item-content>
                  <v-list-item-title>{{Object.keys(item)[0]}}</v-list-item-title>
                  <v-list-item-subtitle>Secondary text</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-row>
      </v-card>
    </v-col>

    <!-- текущие результаты фаззинга, отчёт -->
    <v-col cols="12" sm="6">
      <v-card class="fill-height">
        <v-toolbar>
          <v-toolbar-title>Результаты</v-toolbar-title>
        </v-toolbar>
        <v-card class="ma-1" height="200px">

        </v-card>
        <v-list>

        </v-list>
      </v-card>
    </v-col>

    <!-- предыдущие отчёты -->
    <v-col cols="12" sm="3">
      <v-card class="fill-height">
        <v-toolbar>
          <v-toolbar-title>История</v-toolbar-title>
        </v-toolbar>

        <v-list>
          <v-list-item-group
          v-model="selected_report"
          color="primary"
        >
          <v-list-item
            v-for="(item, i) in report_model"
            :key="i"
            two-line
            color="primary"
          >
            <v-list-item-icon v-if="item.status==0">
              <v-progress-circular
                
                indeterminate
                color="amber"
              ></v-progress-circular>
            </v-list-item-icon>

            <v-list-item-icon
              v-if="item.status==1">
              <v-icon x-large dark color="teal"> mdi-checkbox-marked-circle
              </v-icon>
            </v-list-item-icon>

            <v-list-item-icon
              v-if="item.status==2">
              <v-icon x-large  color="error">mdi-alert-octagon</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{item.name}}</v-list-item-title>
              <v-list-item-subtitle>{{status_strings[item.status]}}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
        </v-list>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import axios from 'axios';
export default {
  name: "FuzzingView",
  data() {
    return {
      searchstring: "", // строка поиска
      api_model: {
        "servers": [
        {
            "url": "http://158.160.0.127",
            "description": "Staging environment"
        }
        ],
        "paths":[
          {"/api/auth":{}},
          {"not_supported":{}},
          {"not_supported":{}},
          {"not_supported":{}}
      ]}, // список API
      report_model: [
        {
          "id": 1,
          "status": 0,
          "swagger_file": "http://127.0.0.1:8000/media/mnt/c/D/Apps/Hack/2022.10_VTB_API/VTB_API_hack2022/experiment/backend/media/swagger_2022-10-14T20%3A12%3A19.290808.json",
          "result_dir": null,
          "name": "2022-10-14 20:12:19"
        },
        {
          "id": 2,
          "status": 1,
          "swagger_file": "http://127.0.0.1:8000/media/mnt/c/D/Apps/Hack/2022.10_VTB_API/VTB_API_hack2022/experiment/backend/media/swagger_2022-10-14T20%3A12%3A19.290808.json",
          "result_dir": null,
          "name": "2022-10-14 20:12:19"
        },
        {
          "id": 3,
          "status": 2,
          "swagger_file": "http://127.0.0.1:8000/media/mnt/c/D/Apps/Hack/2022.10_VTB_API/VTB_API_hack2022/experiment/backend/media/swagger_2022-10-14T20%3A12%3A19.290808.json",
          "result_dir": null,
          "name": "2022-10-14 20:12:19"
        },
      ], // прошлые отчёты
      selected_apis:null,
      selected_report:null,
      current_id:null,
      in_progress:false,
      status_strings:["в процессе","успешно","ошибка сервера"],
      pollInterval : null,
    };
  },
  methods:{

    start(){
      var apis = Object.keys(this.api_model.paths[this.selected_apis])[0];
      axios.post("/fuzzing/start",
      {"apis":[apis]})
      .then(response => {
        console.log(response.data);
        this.in_progress = true;
      })
      .catch(error => {
        console.log(error);
        this.in_progress = false;
      })
    },

    reports(){
      axios.get("/fuzzing/reports")
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.log(error);
      })
    },

    report(){
      axios.get("/fuzzing/report/"+this.current_id+"/")
      .then(response => {
        console.log(response.data);
        //TODO продолжение или останов полоски прогресса
      })
      .catch(error => {
        console.log(error);
      })
    },

    fetchData(){
      this.reports();
    },
  },

  mounted() {
    this.fetchData();
    this.pollInterval = setInterval(this.fetchData(), 2*1000); //save reference to the interval
  },
  beforeDestroy () {
    clearInterval(this.pollInterval)
  }
};
</script>
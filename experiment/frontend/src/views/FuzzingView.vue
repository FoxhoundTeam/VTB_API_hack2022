<template>
  <v-row class="ma-2 fill-height">
    <v-col cols="12" sm="4">
      <!-- начать фаззинг -->
      <v-row class="justify-center ma-1">
        <v-btn class="primary ma-1">
          <v-icon>mdi-play</v-icon>
          Старт
        </v-btn>

        <!-- остановить фаззинг -->
        <v-btn class="error  ma-1">
          <v-icon>mdi-stop</v-icon>
          Стоп
        </v-btn>
      </v-row>

      <v-row>
        <!-- ход фаззинга -->
        <v-progress-linear v-model="progress" height="25">
          <strong>{{ Math.ceil(progress) }}%</strong>
        </v-progress-linear>
      </v-row>
      <v-row>
        
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
            
        </v-list>
      </v-row>
    </v-col>

    <!-- текущие результаты фаззинга, отчёт -->

    <!-- предыдущие отчёты -->
    <v-list>

    </v-list>
  </v-row>
</template>

<script>
export default {
  name: "FuzzingView",
  data() {
    return {
      searchstring : "", // строка поиска
      api_model: [], // список API
      progress: 10,
      report:null, // текущий отчёт (обновляется в процессе)
      report_model: [], // прошлые отчёты
    };
  },
};
</script>
import Vue from "vue";
import Vuetify from "vuetify";
import en from "vuetify/src/locale/en";
import ru from "vuetify/src/locale/ru";

Vue.use(Vuetify);

export default new Vuetify({
  lang: {
    current: "ru",
    locales: { ru, en },
  },
});

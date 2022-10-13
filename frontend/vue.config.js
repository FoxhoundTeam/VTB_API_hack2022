module.exports = {
  transpileDependencies: [
    "vuetify",
    "@jsonforms/core",
    "@jsonforms/vue2",
    "@jsonforms/vue2-vuetify",
  ],
  devServer: {
    proxy: "http://51.250.82.157",
  },
};

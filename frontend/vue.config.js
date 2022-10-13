module.exports = {
  transpileDependencies: [
    "vuetify",
    "@jsonforms/core",
    "@jsonforms/vue2",
    "@jsonforms/vue2-vuetify",
  ],
  devServer: {
    proxy: "http://localhost:8000",
  },
};

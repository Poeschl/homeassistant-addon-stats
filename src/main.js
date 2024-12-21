import '@/assets/bootstrap-custom.scss';
import '@mdi/font/scss/materialdesignicons.scss';
import "bootstrap"
import {createApp} from 'vue'
import App from './App.vue'
import {Env} from "@/Env.js";
import Plausible from "plausible-tracker";

const app = createApp(App)

if (Env.plausibleDomain !== undefined && Env.plausibleDomain.length > 0) {
  const plausible = Plausible({
    domain: Env.plausibleDomain,
    apiHost: Env.plausibleCustomApiHost,
  });
  plausible.enableAutoPageviews();
  app.provide("plausible", plausible);
}

app.mount('#app')

import Vue from 'vue'
import App from './App.vue'
import { store } from "./store"
import { router } from "./router"

Vue.config.productionTip = false

// React нервно курит в сторонке
new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app')

// Как можно заметить по исходникам...
// Опыт с Python и Vue мне очень зашел!
// Даже из-за увлеченности я перевыполнил задачу и добавил лист психотерапевтов
// ради того чтоб просто попробовать vue-router и vuex.
// React во многом далеко до Vue в некоторых моментах даже фундаментальных,
// но вот не знаю, может дело привычки:
// синтаксис React компонентов все же круче, а Vue выигрывает библиотеками
// Но вот что точно мне понравилось, так это писать бэкенд на Python!
// Так что, надеюсь мы сработаемся и у меня будет гора подобного опыта с вами ;)
import Vue from "vue"
import VueRouter from "vue-router"

import ViewDoctor from "../components/ViewDoctor"
import ListDoctors from "../components/ListDoctors"

Vue.use(VueRouter)

// Роутер может быть настолько прост в использовании???
const routes = [
    { path: "/", component: ListDoctors },
    { path: "/doctor/:id", component: ViewDoctor }
]

export const router = new VueRouter({ routes })
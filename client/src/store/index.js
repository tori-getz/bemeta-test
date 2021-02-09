import Vue from "vue"
import Vuex from "vuex"
import Axios from "axios"

import config from "../../config"

Vue.use(Vuex)

// ЭТО В РАЗЫ КРУЧЕ ЧЕМ REDUX :0
export const store = new Vuex.Store({
    state: {
        doctors: null,
        loaded: false
    },
    getters: {
        DOCTORS: state => {
            return state.doctors
        },
        LOADED: state => {
            return state.loaded
        } 
    },
    mutations: {
        LOAD_DOCTORS: (state, payload) => {
            state.doctors = payload
            state.loaded = true
        }
    },
    actions: {
        GET_DOCTORS: async (context) => {
            let { data } = await Axios.get(`${config.API_URL}/doctors/`);
            
            context.commit("LOAD_DOCTORS", JSON.parse(data))
        }
    }
})
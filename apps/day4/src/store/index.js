import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const baseUri = 'https://ms3bhp4fk018nja0.azure-api.net/25-days-day-4'

export default new Vuex.Store({
  state: {
    tasks: []
  },
  getters: {
    getTasks: (state) => state.tasks
  },
  mutations: {
    setTasks: (state, tasks) => (state.tasks = tasks)
  },
  actions: {
    fetchTaskData: async ({ state, commit }, payload) => {
      let axiosOptions = {
        method: 'post',
        url: `${baseUri}/d4-get`,
        headers: {
          'Content-Type': 'application/json'
        }
      }

      let res = await axios(axiosOptions)
      commit('setTasks', res.data)
    }
  },
  modules: {
  }
})

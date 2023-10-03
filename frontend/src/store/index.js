import { createStore } from 'vuex'

export default createStore({
  state: {
    todos: []
  },
  getters: {
    getTodos (state) {
      return state.todos
    }
  },
  mutations: {
    setTodos (state, todos) {
      state.todos = todos
    },
    done (state, id) {
      state.todos.forEach(todo => {
        if (todo.id === id) {
          todo.is_done = !todo.is_done
        }
      })
    }
  },
  actions: {
  },
  modules: {
  }
})

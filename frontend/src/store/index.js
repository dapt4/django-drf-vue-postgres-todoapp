import { createStore } from 'vuex'

export default createStore({
  state: {
    todos: []
  },
  getters: {
    getTodos (state) {
      return state.todos
    },
    getTodo: state => (id) => {
      const todo = state.todos.find(todo => todo.id === id)
      console.log({ todo })
      return todo
    }
  },
  mutations: {
    delTodo (state, id) {
      state.todos.filter(todo => todo.id !== id)
    },
    setTodos (state, todos) {
      state.todos = todos
    },
    /* editTodo(state, id){
      state.todos.f
    }, */
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

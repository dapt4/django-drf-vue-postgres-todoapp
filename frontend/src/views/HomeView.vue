<template>
  <div class="todos-content">
    <TodoCard
      v-for="todo of todos"
      :key="todo.id"
      :id="todo.id"
      :title="todo.title"
      :description="todo.description"
      :is_done="todo.is_done"
      :date_created="todo.date_created"
      :updateFunc="updateTodosFromApi"
      />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import store from '@/store'
import TodoCard from '@/components/TodoCard.vue'
const todos = ref()

const getTodosFromApi = async () => {
  const url = 'http://localhost:8000/todo'
  const res = await fetch(url, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    }
  })
  return await res.json()
}

const updateTodosFromApi = async () => {
  const todosApi = await getTodosFromApi()
  store.commit('setTodos', todosApi)
  todos.value = store.getters.getTodos
  console.log(store.getters.getTodos)
}

onMounted(() => {
  updateTodosFromApi()
})
</script>

<style scoped>
.todos-content{
  display: block;
  width: 100%;
  height: calc(100vh - 60px);
  padding: 20px;
  /*grid-template-columns: auto;*/
  /*flex-wrap:wrap;*/
  /*flex-direction: row;*/
  /*justify-content: center;*/
  /*align-items: flex-start;*/
  /*gap: 20px;*/
}
</style>

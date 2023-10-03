<template>
  <div class="container p-5">
    <TodoCard
      v-for="todo of todos"
      :key="todo.id"
      :id="todo.id"
      :title="todo.title"
      :description="todo.description"
      :is_done="todo.is_done"
      :date_created="todo.date_created"
      />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import store from '@/store'
import TodoCard from '@/components/TodoCard.vue'
const todos = ref(store.getters.getTodos)

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

onMounted(async () => {
  const todosApi = await getTodosFromApi()
  store.commit('setTodos', todosApi)
  todos.value = store.getters.getTodos
  console.log(todos.value)
})
</script>

<style>

</style>

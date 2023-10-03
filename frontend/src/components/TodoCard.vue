<template>
  <div class="card mb-3" style="width: 18rem;">
    <div class="card-header">Todo</div>
    <div class="card-body">
      <h5 class="card-title">{{props.title}}</h5>
      <p class="card-text">{{props.description}}</p>
      <button @click="done" class="btn" :class="[ props.is_done ? 'btn-success' : 'btn-secondary']">
        Done
      </button>
      <router-link class="btn btn-warning" to="/edit">
        Edit
      </router-link>
      <button @click="deleteOne" class="btn btn-danger">
        Delete
      </button>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'
import store from '@/store'
const props = defineProps({
  id: Number,
  title: String,
  description: String,
  is_done: Boolean,
  date_created: String
})
const done = async () => {
  const url = `http://localhost:8000/todo/done/${props.id}`
  const res = await fetch(url)
  const json = await res.json()
  console.log(json)
  store.commit('done', props.id)
}
const deleteOne = async () => {
  const url = `http://localhost:8000/todo/${props.id}`
  const res = await fetch(url, {
    method: 'DELETE'
  })
  const json = await res.json()
  console.log(json)
  // make a mutation
}
</script>

<style scoped>
/* code... */
</style>

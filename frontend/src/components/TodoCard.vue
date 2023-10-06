<template>
  <div class="card">
    <div class="card-header">Todo</div>
    <div class="card-body">
      <h5 class="card-title">{{ props.title }}</h5>
      <p class="card-text">{{ props.description }}</p>
      <div class="buttons">
        <button @click="done" class="btn" :class="[props.is_done ? 'btn-success' : 'btn-secondary']">
          Done
        </button>
        <button class="btn btn-warning" @click="edit">Edit</button>
        <button @click="deleteOne" class="btn btn-danger">Delete</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'
import store from '@/store'
import router from '@/router'
const props = defineProps({
  id: Number,
  title: String,
  description: String,
  is_done: Boolean,
  date_created: String,
  updateFunc: Function
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
  store.commit('delTodo', props.id)
  props.updateFunc()
}

const edit = () => {
  const url = `/edit/${props.id}`
  router.push(url)
}
</script>

<style scoped>
.card {
  width: 300px;
  height: 200px;
  margin: 20px;
  float: left;
  .card-header {
    text-align: center;
  }
  .card-body {
    .card-title {
      text-align: center;
    }
    .buttons {
      display: flex;
      justify-content: space-between;
      align-items: center;
      button{
        width: 100% ;
      }
    }
  }
}
</style>

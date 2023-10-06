<template>
  <div class="card card-body form-card">
    <h1 class="header">{{ edit ? 'Edit' : 'New' }} todo</h1>
    <form @submit.prevent="sendTodo">
      <div class="mb-3">
        <label for="title" class="form-label">Title</label>
        <input class="form-control" v-model="editedTodo.title" id="title">
      </div>
      <div class="mb-3">
        <label for="description" class="form-label">Description</label>
        <textarea class="form-control" id="description" v-model="editedTodo.description"></textarea>
      </div>
      <button class="btn px-5 button" :class="[edit ? 'btn-warning' : 'btn-primary']">Submit</button>
    </form>
  </div>
</template>

<script setup >
import { ref, onMounted } from 'vue'
import router from '@/router'
import { useRoute } from 'vue-router'
import store from '@/store'
const { params } = useRoute()
const edit = ref(params.id)
const editedTodo = ref({
  title: '',
  description: ''
})
const sendTodo = async () => {
  const isEdit = edit.value ? `/${params.id}` : ''
  const url = `http://localhost:8000/todo${isEdit}`
  const res = await fetch(url, {
    method: edit.value ? 'PUT' : 'POST',
    body: JSON.stringify(editedTodo.value),
    headers: {
      'Content-type': 'application/json'
    }
  })
  const json = await res.json()
  console.log(json)
  router.push('/')
}

onMounted(_ => {
  editedTodo.value = store.getters.getTodo(parseInt(params.id))
  console.log(editedTodo.value)
})

</script>

<style lang="scss" scoped>
.form-card{
  width: 90%;
  margin: 20px auto;
  @media only screen and (min-width: 768px) {
    width: 50%;
  }
  .header{
    display: block;
    width: fit-content;
    margin: 0px auto;
  }
  form{
    .button{
      display: block;
      width: fit-content;
      margin: 20px auto;
    }
  }
}
</style>

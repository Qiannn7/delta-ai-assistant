<template>
  <div class="container">
    <h2>Delta AI Assistant</h2>
    <button @click="fetchHello">请求后端接口</button>
    <div v-if="resData">
      返回消息：{{ resData.msg }}
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const resData = ref(null)

const fetchHello = async ()=>{
  //后端地址
  const resp = await fetch('http://127.0.0.1:5000/api/hello')
  const json = await resp.json()
  resData.value = json
}
</script>

<style>
.container{
  padding:30px;
}
button{
  padding:8px 16px;
  font-size:16px;
}
</style>

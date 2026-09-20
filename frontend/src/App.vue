<template>
  <div class="container">
    <h2>Delta AI Assistant</h2>
    <div class="chat-box">
      <div v-for="(item,idx) in chatList" :key="idx" class="msg">
        <div v-if="item.role==='user'" class="user">用户：{{item.content}}</div>
        <div v-if="item.role==='ai'" class="ai">AI：{{item.content}}</div>
      </div>
    </div>
    <div class="input-area">
      <input v-model="userInput" placeholder="请输入问题"/>
      <button @click="sendChat">发送</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const userInput = ref("")
const chatList = ref([])

const sendChat = async ()=>{
  if(!userInput.value.trim()) return
  //把用户消息加入列表
  chatList.value.push({role:"user",content:userInput.value})
  const resp = await fetch("http://127.0.0.1:5000/api/chat",{
    method:"POST",
    headers:{
      "Content-Type":"application/json"
    },
    body:JSON.stringify({question:userInput.value})
  })
  const json = await resp.json()
  chatList.value.push({role:"ai",content:json.reply})
  userInput.value = ""
}
</script>

<style>
.container{
  width:600px;
  margin:30px auto;
}
.chat-box{
  border:1px solid #444;
  min-height:300px;
  padding:12px;
  margin-bottom:16px;
}
.user{
  text-align:right;
  margin:8px 0;
  color:#42b983;
}
.ai{
  text-align:left;
  margin:8px 0;
  color:#66b1ff;
}
.input-area{
  display:flex;
  gap:8px;
}
input{
  flex:1;
  padding:8px;
}
button{
  padding:8px 16px;
}
</style>

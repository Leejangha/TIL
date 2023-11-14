<template>
    <div>
      <h1>Detail</h1>
      <div v-if="saving">
        <p>제목 : {{ saving.kor_co_nm }}</p>
        <p>내용 : {{ saving.fin_prdt_nm }}</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios'
  import { onMounted, ref } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  import { useRoute } from 'vue-router'
  
  const store = useCounterStore()
  const route = useRoute()
  const saving = ref(null)
  
  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/bank/saving-products/${route.params.id}/`
    })
      .then((res) => {
        saving.value = res.data.response
      })
      .catch((err) => {
        console.log(err)
      })
  })
  
  </script>
  
  <style>
  
  </style>
  
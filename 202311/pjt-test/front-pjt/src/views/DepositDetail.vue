<template>
    <div>
      <h1>Detail</h1>
      <div v-if="deposit">
        <p>제목 : {{ deposit.kor_co_nm }}</p>
        <p>내용 : {{ deposit.fin_prdt_nm }}</p>
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
  const deposit = ref(null)
  
  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/bank/deposit-products/${route.params.id}/`
    })
      .then((res) => {
        deposit.value = res.data.response
      })
      .catch((err) => {
        console.log(err)
      })
  })
  
  </script>
  
  <style>
  
  </style>
  
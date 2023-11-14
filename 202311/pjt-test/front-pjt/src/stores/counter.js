import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const deposits = ref([])
  const savings = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  const getDeposits = function () {
    axios({
      method: 'get',
      url: `${API_URL}/bank/deposit-products/`, 
    })
      .then((res) => {
        deposits.value = res.data.response
      })
      .catch((err) => {
        console.log(err)
      })
  }
  const getSavings = function () {
    axios({
      method: 'get',
      url: `${API_URL}/bank/saving-products/`, 
    })
      .then((res) => {
        savings.value = res.data.response
      })
      .catch((err) => {
        console.log(err)
      })
  }

  return { deposits, savings, getDeposits, getSavings }
})

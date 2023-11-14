<template>
    <div>
        <h5>{{ deposit.id }}</h5>
        <p>{{ deposit.fin_prdt_nm }}</p>
        <p>{{ deposit.kor_co_nm }}</p>
        <RouterLink :to="{ name: 'depositdetail', params: { id: deposit.id }}" >
            [Detail]
        </RouterLink>
        <hr>
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
    deposit: Object
})
</script>
  
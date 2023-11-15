<template>
    <div>
        <h5>{{ saving }}</h5>
        <p>{{ saving.fin_prdt_nm }}</p>
        <p>{{ saving.kor_co_nm }}</p>
        <!-- <RouterLink :to="{ name: 'savingdetail', params: { id: saving.id }}" >
            [Detail]
        </RouterLink> -->
        <hr>
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
    saving: Object
})
</script>
  
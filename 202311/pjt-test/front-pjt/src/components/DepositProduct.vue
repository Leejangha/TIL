<template>
    <div>
        <h5>{{ deposit.id }}</h5>
        <p>{{ deposit.fin_prdt_nm }}</p>
        <p>{{ deposit.kor_co_nm }}</p>
        <DepositDetail
            v-for="deposit_option in deposit.deposit_options"
            :key="deposit_option.id"
            :deposit_option="deposit_option"
            class="container"
        />
        <hr>
    </div>
</template>

<script setup>
import DepositDetail from '@/components/DepositDetail.vue';

defineProps({
    deposit: Object
})
</script>

<style>

</style>
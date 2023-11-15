<template>
    <div>
        <div class="product">
            <p>{{ saving.fin_prdt_nm }}</p>
            <p>{{ saving.kor_co_nm }}</p>
        </div>
        <div>
            <label for="customAmount">월 적금 금액 :</label>
            <input v-model="customAmount" type="number" id="customAmount" />
        </div>
        <div class="saving-options-container">
            <SavingDetail
                v-for="saving_option in saving.saving_options"
                :key="saving_option.id"
                :saving_option="saving_option"
                @click="updateRealTimeValue(saving_option)"
                class="saving-option"
            />
        </div>
        <div class="real-time-value">
            <p>월 {{ customAmount }}만원씩 적금하면 총 세후 이자 : {{ formatNumber(realTimeValue) }}원</p>
        </div>
        <hr>
    </div>
</template>

<script setup>
import SavingDetail from '@/components/SavingDetail.vue'
import { ref } from 'vue'

defineProps({
    saving: Object
})

const realTimeValue = ref('')
const customAmount = ref(100000);

const updateRealTimeValue = (saving_option) => {
    realTimeValue.value = Math.round(customAmount.value * saving_option.intr_rate2 / 100 * saving_option.save_trm / 12 * 0.846)
}

const formatNumber = (number) => {
    return number.toLocaleString()
}

</script>

<style scoped>
.product {
    font-size: 25px;
}
.saving-options-container {
    display: flex;
}

.saving-option {
    border: solid 1px blue;
    margin-right: 10px;
}

.real-time-value {
    margin-top: 10px;
}
</style>
  
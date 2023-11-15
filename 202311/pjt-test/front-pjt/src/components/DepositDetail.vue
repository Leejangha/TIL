<template>
    <div>
      <div v-if="deposit_option" class="container">
        <p>{{ deposit_option.intr_rate_type_nm }}</p>
        <p>금리 : {{ deposit_option.intr_rate }}</p>
        <p>우대금리 : {{ deposit_option.intr_rate2 }}</p>
        <p>기간 : {{ deposit_option.save_trm }}개월</p>
      </div>
    </div>
</template>
  
<script setup>
defineProps({
  deposit_option: Object
})

</script>

<style>
.container {
  border: solid 1px blue;
}
</style>
  
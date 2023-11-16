<template>
  <header>
    <div>
      <b-button>Button</b-button>
      <b-button variant="danger">Button</b-button>
      <b-button variant="success">Button</b-button>
      <b-button variant="outline-primary">Button</b-button>
    </div>
    <nav>
      <RouterLink :to="{ name: 'home' }">
        [Home]
      </RouterLink>
      <RouterLink :to="{ name: 'deposit' }">
        [Deposit]
      </RouterLink>
      <RouterLink :to="{ name: 'saving' }">
        [Saving]
      </RouterLink>
      <RouterLink :to="{ name: 'exchange' }">
        [Exchange]
      </RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>

<style scoped>
</style>

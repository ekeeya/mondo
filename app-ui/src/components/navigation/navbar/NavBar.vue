<template>
  <vs-navbar  target-scroll="#padding-scroll-content" padding-scroll center-collapsed v-model="active">
    <template #left>

    </template>

    <vs-navbar-item :active="active == 'docs'" id="docs">
      <i class="bx bx-book"></i>&nbsp;Docs
    </vs-navbar-item>
    <vs-navbar-item :active="active == 'license'" id="license">
      License
    </vs-navbar-item>
    <template #right>
      <vs-button color="warning"  >Upgrade to Premium</vs-button>
      <vs-button dark >
        <i class="bx bxl-github"></i>&nbsp;GitHub
      </vs-button>
    </template>
  </vs-navbar>
</template>

<script>
export default {
  name: "NavBar"
}
</script>

<style scoped>

</style>
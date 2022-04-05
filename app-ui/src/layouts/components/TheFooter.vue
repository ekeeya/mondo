<template functional>
  <footer class="p-4 h-10  bg-white rounded-lg shadow md:flex md:items-center md:justify-end md:p-6 dark:bg-gray-800">
    <span class="text-sm   text-gray-500 sm:text-center dark:text-gray-400">© {{ new Date().getFullYear() }}  <a href="https://flowbite.com" class="hover:underline">Odd Jobs™</a>. All Rights Reserved. </span>
  </footer>

</template>

<script>

export default {
  name: "the-footer",
  props: {
    classes: {
      type: String,
    },
  },
  inject: {
    components: {
      default: {}
    }
  }
}
</script>
<style scoped>
.the-footer{

}
</style>
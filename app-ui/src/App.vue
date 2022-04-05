<template>
  <div id="app">
    <Main/>
    <router-view/>
  </div>
</template>

<script>
import Main from "@/layouts/main/Main";
export default {
  components:{
    Main,
  }
}
</script>

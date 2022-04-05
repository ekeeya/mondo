<template>
    <div class="flex flex-col h-screen">
      <side-bar/>
      <main class="flex-grow">
        <router-view />
      </main>
      <the-footer/>
    </div>
</template>

<script>
import SideBar from "@/components/navigation/sidebar/SideBar";
import TheFooter from "@/layouts/components/TheFooter";
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Main",
  components:{
    SideBar,
    TheFooter
  }
}
</script>

<style scoped>

</style>
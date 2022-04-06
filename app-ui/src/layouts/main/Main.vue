<template>
  <div class="flex-grow h-screen">
    <the-footer/>
    <side-bar/>
    <nav-bar/>
    <main class="flex-grow">
      <div class="ml-20 mr-10 py-4 w-9/10 bg-white shadow-lg rounded-lg my-10">
        <router-view/>
      </div>
    </main>
  </div>
</template>

<script>
import SideBar from "@/components/navigation/sidebar/SideBar";
import TheFooter from "@/layouts/components/TheFooter";
import NavBar from "@/components/navigation/navbar/NavBar";
export default {

  name: "MainView",
  components: {
    SideBar,
     TheFooter,
    NavBar
  },
  data(){
    return{
      activeItem:true,
      search:""
    }
  }
}
</script>

<style scoped>

</style>
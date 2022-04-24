<template>
  <div>
    <div class="flex-grow h-screen">

      <side-bar/>
      <div id="layout-view" class="py-4 w-12/12 bg-white shadow-lg  rounded-lg my-10">
        <router-view/>

      </div>

    </div>
    <the-footer/>
  </div>

</template>

<script>
import SideBar from "@/components/navigation/sidebar/SideBar";
import TheFooter from "@/layouts/components/TheFooter";
export default {

  name: "MainView",
  components: {
    SideBar,
    TheFooter
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
#layout-view {
  margin-left: 3.5rem !important;
  height: 94% !important;
  max-height: 100% !important;
}
</style>
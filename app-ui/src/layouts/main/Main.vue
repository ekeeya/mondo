<template>
  <div class="flex flex-grow">
    <side-bar/>
  </div>
</template>

<script>
import SideBar from "@/components/navigation/sidebar/SideBar";
//import TheFooter from "@/layouts/components/TheFooter";

export default {

  name: "MainView",
  components: {
    SideBar,
    //  TheFooter
  },
  data(){
    return{
      activeItem:true
    }
  }
}
</script>

<style scoped>

</style>
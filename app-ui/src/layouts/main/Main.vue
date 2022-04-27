<template>
  <div>
    <div class="flex-grow h-screen">

      <side-bar/>
      <div id="layout-view" class="py-4 w-12/12 content-wrapper rounded-lg my-10">
        <div v-if="$route.meta.breadcrumb || $route.meta.pageTitle" class="router-header flex flex-wrap items-center mb-6">
          <div
              class="content-area__heading"
              :class="{'pr-4 border-0 md:border-r border-solid border-grey-light' : $route.meta.breadcrumb}">
            <h2 class="mb-1">{{ routeTitle }}</h2>
          </div>

          <!-- BREADCRUMB -->
          <vx-breadcrumb class="ml-4 md:block hidden" v-if="$route.meta.breadcrumb" :route="$route" :isRTL="$vs.rtl" />

        </div>
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
.content-wrapper{
  background-color: #f9fbfd;
}
</style>
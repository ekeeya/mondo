<template>
  <div >
    <side-bar/>
    <div id="layout-view" class="py-4  content-wrapper rounded-lg my-12">
      <div v-if="$route.meta.breadcrumb || $route.meta.pageTitle"
           class="router-header flex flex-wrap items-center mb-6">
        <div
            :class="{'pr-4 border-0 md:border-r border-solid border-grey-light' : $route.meta.breadcrumb}"
            class="content-area__heading">
          <h2 class="mb-1">{{ routeTitle }}</h2>
        </div>
      </div>
      <router-view/>
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
  data() {
    return {
      activeItem: true,
      search: ""
    }
  }
}
</script>

<style scoped>
#layout-view {
  margin-left: 3.5rem !important;
  height: 87vh !important;
  max-height: 94vh;
  overflow: auto;
}

.content-wrapper {
  background-color: #f9fbfd;
}

</style>
<template>
  <vs-navbar shadow square center-collapsed v-model="active">
    <template v-if="showLeftToggle" #left>
      <vs-button @click="isSidebarActiveLocal = !isSidebarActiveLocal" flat icon>
        <i class='bx bx-menu'></i>
      </vs-button>
    </template>
    <vs-navbar-item :active="active == 'docs'" id="docs">
      Documents
    </vs-navbar-item>
    <vs-navbar-item :active="active == 'license'" id="license">
      license
    </vs-navbar-item>
    <template #right>
      <vs-button
          warn
      >
        <i class="bx bxs-badge-dollar" style="font-size: 16pt"></i>&nbsp;
        Upgrade to Premium
      </vs-button>
      <vs-button dark
                 ><i class="bx bxl-github" style="font-size: 16pt"></i>&nbsp;GitHub</vs-button>
    </template>
  </vs-navbar>
</template>

<script>
export default {
  name: "NavBar",
  props:{
    isSidebarActive: {
      type: Boolean,
      required: true
    },
    showLeftToggle:{
      type: Boolean,
      required: true
    }
  },
  data(){
    return{
      active:'home'
    }
  },
  computed:{
    isSidebarActiveLocal: {
      get() {
        return this.isSidebarActive
      },
      set(val) {
        if(val) {
          this.$emit('showSidebar')
        }
        else{
          this.$emit('closeSidebar')
        }
      }
    },
  }
}
</script>

<style scoped>

</style>
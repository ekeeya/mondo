<template>
  <div>
    <nav-bar  :showLeftToggle="showNavBarToggle" :isSidebarActive="activeSidebar" @showSidebar="toggleSideBar(true)"  @closeSidebar="toggleSideBar(false)" />
    <vs-sidebar
        absolute
        square
        hover-expand
        spacer
        reduce
        v-model="active"
        :open.sync="activeSidebar"
    >
      <template #logo>
        <vs-avatar  size="80px" src="https://randomuser.me/api/portraits/men/85.jpg"/>
      </template>
      <div :key="idx" v-for="(menu, idx) in menuItems">

        <vs-sidebar-group v-if="menu.items" >
          <template #header>
            <vs-sidebar-item arrow>
              <template #icon>
                <i :class='`bx ${menu.icon}`'></i>
              </template>
              <span v-if="menu.items">{{menu.header}}</span>
            </vs-sidebar-item>
          </template>
          <vs-sidebar-item  :key="index" v-for="(item, index) in menu.items" :id="item.slug">
            <template #icon>
              <i :class='`bx ${item.icon}`'></i>
            </template>
            <a @click="navigate(item.url)" href="javascript:void(0)">{{item.name}}</a>
          </vs-sidebar-item>
        </vs-sidebar-group>
        <vs-sidebar-item v-else :id="menu.slug">
          <template #icon>
            <i :class='`bx ${menu.icon}`'></i>
          </template>
          <a @click="navigate(menu.url)" href="javascript:void(0)">{{menu.header}} </a>
        </vs-sidebar-item>
      </div>

      <template #footer>
        <vs-row justify="space-between">
          <vs-avatar ba badge-color="success" badge-position="top-right">
            <i class='bx bx-bell' ></i>
            <template #badge>
              <span style="color:#ffff">28</span>
            </template>
          </vs-avatar>

          <vs-avatar>
            <img src="/avatars/avatar-5.png" alt="">
          </vs-avatar>
        </vs-row>
      </template>
    </vs-sidebar>

  </div>
</template>
<script>
import menuItems from "@/components/navigation/sidebar/menuItems";
import NavBar from "@/components/navigation/navbar/NavBar";
export default {
  name: "SideBar",
  components:{
    NavBar,
  },
  data: () => ({
    active:true,
    notExpand: false,
    reduce: true,
    menuItems:menuItems,
    activeSidebar: true,
    showNavBarToggle:false
  }),
  methods:{
    toggleSideBar(value){
      this.activeSidebar =  value;
    },
    navigate(path){
      console.log(path)
      this.$router.push({path});
    }
  }
};
</script>
<style lang="stylus">

.header-sidebar
  display flex
  align-items center
  justify-content center
  flex-direction column
  width 100%
  h4
    display flex
    align-items center
    justify-content center
    width 100%
    > button
      margin-left 10px

.footer-sidebar
  display flex
  align-items center
  justify-content space-between
  width 100%
  > button
    border 0px solid rgba(0,0,0,0) !important
    border-left 1px solid rgba(0,0,0,.07) !important
    border-radius 0px !important
</style>

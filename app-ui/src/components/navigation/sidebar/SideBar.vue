<template>
  <vs-sidebar
      absolute
      hover-expand
      spacer
      background="dark"
      textWhite
      reduce
      v-model="active"
      open
  >
    <template #logo>
      <vs-avatar  size="80px" src="https://randomuser.me/api/portraits/men/85.jpg"/>
    </template>
    <vs-sidebar-item id="home">
      <template #icon>
        <i class='bx bx-home'></i>
      </template>
      Home
    </vs-sidebar-item>
    <vs-sidebar-group>
      <template #header>
        <vs-sidebar-item arrow>
          <template #icon>
            <i class='bx bx-dialpad'></i>
          </template>
         USSD
        </vs-sidebar-item>
      </template>

      <vs-sidebar-item id="flows">
        <template #icon>
          <i class='bx bx-network-chart'></i>
        </template>
        Flows
      </vs-sidebar-item>
      <vs-sidebar-item id="twitter">
        <template #icon>
          <i class='bx bx-plug' ></i>
        </template>
        Aggregator APIs
      </vs-sidebar-item>
    </vs-sidebar-group>
    <vs-sidebar-item id="market">
      <template #icon>
        <i class='bx bx-chat'></i>
      </template>
      SMS
    </vs-sidebar-item>
    <vs-sidebar-group>
      <template #header>
        <vs-sidebar-item arrow>
          <template #icon>
            <i class='bx bxs-cog' ></i>
          </template>
          Gateway Configs
        </vs-sidebar-item>
      </template>

      <vs-sidebar-item id="github">
        <template #icon>
          <i class='bx bxs-inbox' ></i>
        </template>
        Kannel
      </vs-sidebar-item>
      <vs-sidebar-item id="codepen">
        <template #icon>
          <i class='bx bx-station'></i>
        </template>
        Mbuni
      </vs-sidebar-item>

    </vs-sidebar-group>
    <vs-sidebar-item id="donate">
      <template #icon>
        <i class='bx bxs-donate-heart' ></i>
      </template>
      Donate
    </vs-sidebar-item>
    <vs-sidebar-item id="chat">
      <template #icon>
        <i class='bx bx-user-check' ></i>
      </template>
      Profile
    </vs-sidebar-item>
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
</template>
<script>
import menuItems from "@/components/navigation/sidebar/menuItems";
export default {
  name: "SideBar",
  data: () => ({
    active:true,
    notExpand: false,
    reduce: true,
    menuItems:menuItems
  }),
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

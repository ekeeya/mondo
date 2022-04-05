<template>
  <vs-sidebar hidden-background :parent="$refs.parentSidebar" :reduce="reduce" :reduce-not-hover-expand="notExpand"  default-index="-1"  color="success" class="sidebarx" spacer v-model="active">

    <div class="header-sidebar" slot="header">
      <vs-avatar  size="70px" src="https://randomuser.me/api/portraits/men/85.jpg"/>
    </div>
    <vs-sidebar-group open title="USSD">
      <vs-sidebar-item index="1" icon="account_tree" >
        Flows
      </vs-sidebar-item>
      <vs-sidebar-item index="5" icon="phonelink_setup">
        Aggregator APIs
      </vs-sidebar-item>

    </vs-sidebar-group>
    <vs-sidebar-item index="4" icon="chat">
      SMS
    </vs-sidebar-item>
    <vs-sidebar-group title="SMS GATEWAYS">
      <vs-sidebar-item index="2.1" icon="all_inbox">
        Kannel
      </vs-sidebar-item>
      <vs-sidebar-item index="2.2" icon="nature_people">
        Mbuni
      </vs-sidebar-item>
    </vs-sidebar-group>
    <vs-sidebar-item index="4" icon="help">
      Help
    </vs-sidebar-item>
    <vs-divider icon="person" position="left">
      User
    </vs-divider>


    <vs-sidebar-item index="6" icon="account_box">
      Profile
    </vs-sidebar-item>

    <div class="footer-sidebar" slot="footer">
      <vs-button icon="settings" color="primary" type="border"></vs-button>
    </div>

  </vs-sidebar>
</template>
<script>
export default {
  name: "SideBar",
  data: () => ({
    active:true,
    notExpand: false,
    reduce: true
  }),
};
</script>
<style lang="stylus">
#parentx
  overflow hidden
  height 98%
  position relative

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

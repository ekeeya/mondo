<template>
  <div>
    <vs-sidebar
        absolute
        background="dark"
        textWhite
        hover-expand
        reduce
        v-model="active"
        open
    >
      <template #logo>
        <!-- ...img logo -->
      </template>
      <vs-sidebar-item id="home">
        <template #icon>
          <i class='bx bx-home'></i>
        </template>
        Home
      </vs-sidebar-item>
      <vs-sidebar-item id="Modules">
        MODULES
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

        <vs-sidebar-item id="Network">
          <template #icon>
            <i class='bx bx-network-chart  '></i>
          </template>
          Flows
        </vs-sidebar-item>
        <vs-sidebar-item id="APIs">
          <template #icon>
            <i class='bx bx-link-external' ></i>
          </template>
          Aggregator APIs
        </vs-sidebar-item>
      </vs-sidebar-group>
      <vs-sidebar-item id="SMS">
        <template #icon>
          <i class='bx bxs-message-rounded-detail'></i>
        </template>
        SMS
      </vs-sidebar-item>
      <vs-sidebar-item id="Configurations">
        CONFIGURATIONS
      </vs-sidebar-item>
      <vs-sidebar-group>
        <template #header>
          <vs-sidebar-item arrow>
            <template #icon>
              <i class='bx bx-code-alt' ></i>
            </template>
            SMS Gateways
          </vs-sidebar-item>
        </template>

        <vs-sidebar-item id="Kannel">
          <template #icon>
            <i class='bx bx-comment-dots' ></i>
          </template>
          Kannel
        </vs-sidebar-item>
        <vs-sidebar-item id="Mbuni">
          <template #icon>
            <i class='bx bx-station'></i>
          </template>
          Mbuni
        </vs-sidebar-item>
      </vs-sidebar-group>
      <vs-sidebar-item id="donate">
        <template #icon>
          <i class="bx bxs-donate-heart"></i>
        </template>
        Donate
      </vs-sidebar-item>


      <vs-sidebar-item id="chat">
        <template #icon>
          <i class="bx bx-chat"></i>
        </template>
        Chat
      </vs-sidebar-item>
      <template #footer>
        <vs-row justify="space-between">
          <vs-avatar badge-color="danger" badge-position="top-right">
            <i class="bx bx-bell"></i>

            <template #badge> 28 </template>
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
export default {
  name: "SideBar",
  data: () => ({
    active: "home",
  }),
};
</script>

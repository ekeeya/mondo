<template>
  <div >
    <vs-row w="12">
      <vs-col  w="3" class="p-3 breath bg-white mx-1  rounded-lg">
        <template>
          <div class="vs-row header">
            <div class="icon header-icon-container">
              <i class='bx bx-abacus header-icon' ></i>
            </div>
            <div class="title-text">
              Flow Statistics
            </div>
          </div>
        </template>
        <div class="flex flex-wrap items-center" >
          <div class="center">
            <table class="table">
              <tbody>
                <tr>
                  <td>USSD:</td>
                  <td>0</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </vs-col>
      <vs-col w="8" class="max-width breath p-3 mx-2 shadow-lg bg-white rounded-lg">
        <template>
          <div class="vs-row header">
            <div class="icon header-icon-container">
              <i class='bx bx-list-plus header-icon' ></i>
            </div>
            <div class="title-text ">
              USSD Flows
            </div>
          </div>
        </template>
        <div class="flex flex-wrap items-center" >
          <ag-grid-vue
              ref="agGridTable"
              class="w-full my-4 ag-grid-custom ag-theme-alpine"
              :defaultColDef="defaultColDef"
              :gridOptions="gridOptions"
              :columnDefs="columnDefs"
              :rowData="rowData"
              rowSelection="multiple"
              colResizeDefault="shift"
              :animateRows="true"
              :floatingFilter="false"
              :pagination="true"
              :paginationPageSize="paginationPageSize"
              :suppressPaginationPanel="true"
          >
          </ag-grid-vue>
        </div>
      </vs-col>
    </vs-row>
  </div>


</template>

<script>

import { AgGridVue } from "ag-grid-vue";
export default {
  name: "FlowList",
  components: {
    AgGridVue,
  },
  data(){
    return{
      gridApi: null,
      gridOptions: {},
      defaultColDef: {
        sortable: true,
        editable:true,
        resizable: true,
        suppressMenu: true
      },
      columnDefs: [
        { headerName: 'Name', field: 'name' },
        { headerName: 'Type', field: 'type' },
        { headerName: 'Status', field: 'status' },
        { headerName: 'Owner', field: 'owned_by' },
        { headerName: 'Created at', field: 'created_at' }

      ],
      rowData: [
        { name: 'Virtual Banking', type: 'USSD', owned_by:"Stanbic Bank", status: 'Active' },
        { name: 'Mobile Money', type: 'USSD', owned_by:"MTN UG", status: 'Active' },
        { name: 'Electricity Tokens (*922#)', owned_by:"UMEME", type: 'USSD', status: 'Active' }
      ],
      stats:{
        ussd:2,
        sms:3,
        deleted:0,
        archived:1
      }
    }
  },
  computed:{
    paginationPageSize() {
      if(this.gridApi) return this.gridApi.paginationGetPageSize()
      else return 10
    },
    totalPages() {
      if(this.gridApi) return this.gridApi.paginationGetTotalPages()
      else return 0
    }
  },
  mounted() {
    this.gridApi = this.gridOptions.api;
  }
}
</script>

<style scoped>
.title-text{
  font-size: 20px;
  font-weight: bolder;
}
.icon{
  margin-right: 20px;
}
</style>
<template>
  <div id="page-operator-list" class="col-md-10">

    <div class="vx-card p-6 shadow-lg bg-white mx-10 rounded-lg">
        <template>
          <div class="vs-row">
            <div class="icon">
              a
            </div>
            <div class="title-text">
              USSD Flows
            </div>
          </div>
        </template>
      <div class="flex flex-wrap items-center" >
        <ag-grid-vue
            ref="agGridTable"
            style="width: 100vh; height: 200px"
            class="w-full my-4  ag-theme-alpine"
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
    </div>
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
        { headerName: 'Make', field: 'make' },
        { headerName: 'Model', field: 'model' },
        { headerName: 'Price', field: 'price' }
      ],
      rowData: [
        { make: 'Toyota', model: 'Celica', price: 35000 },
        { make: 'Ford', model: 'Mondeo', price: 32000 },
        { make: 'Porsche', model: 'Boxster', price: 72000 }
      ]
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
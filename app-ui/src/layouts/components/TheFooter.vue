<template functional>
  <div class="grid">
    <vs-row>
      <vs-col  w="11" >
        <footer class="footer bg-white rounded-lg shadow md:flex md:items-center md:justify-end md:p-6 dark:bg-gray-800">
          <span class="text-sm  text-gray-500 sm:text-center dark:text-gray-400">© {{ new Date().getFullYear() }}  <a href="https://flowbite.com" class="hover:underline">Odd Jobs™</a>. All Rights Reserved. </span>
        </footer>
      </vs-col>
      <vs-col  w="1">
        <div class="news-container mx-1 bg-white  shadow">
          <div class="grid">
            <vs-col>
             <div class="logo-container">

             </div>
            </vs-col>
            <vs-col>
              <div class="new-container">
                Did you know you can still get it free of charge! <p>Call +256 755 387533</p>
              </div>
            </vs-col>
          </div>
        </div>

      </vs-col>
    </vs-row>
  </div>


</template>

<script>

export default {
  name: "the-footer",
  props: {
    classes: {
      type: String,
    },
  },
  inject: {
    components: {
      default: {}
    }
  }
}
</script>
<style scoped>
.footer{
  height: 6vh;
  position:absolute;
  bottom:0;
  left: 0;
  width: 100%;
  text-align: center;
}
.news-container{
  height: 25vh;
  position:absolute;
  text-align: center;
  bottom:0;
  left: 0;
  width: 100%;
  border-top-left-radius: 1.5rem;
  transition: var(--transition)
}
.news-container:hover{
  transition:  var(--transition);
  border-radius: 1.5rem;
  width: 95%;
  height: 28vh;
}
.logo-container{
  height: 10vh;
  margin: 10px;
  border-radius: 10px;
}
.new-container{
  font-size: 8px;
  margin: 5px;
  height: 100%;
  color:#ffffff;
}
</style>
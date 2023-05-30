<template>
  <div class="home">
    <div id="moduleCarousel" class="d-flex flex-wrap justify-content-center">
      <router-link to="/upload-csv" class="d-flex align-content-stretch no-decor m-2">
        <div class="card border-0">
          <b-icon-cloud-upload 
          class="row card-img m-0 justify-content-center" 
          width="100" height="100"/>
          <div class="row card-body">
            <h5 class="card-title mx-auto">
              <router-link to="/upload-csv"> Upload *.csv </router-link>
            </h5>
          </div>
        </div>
      </router-link>

      <router-link to="/dashboard" class="d-flex align-content-stretch no-decor m-2">
        <div class="card border-0">
          <b-icon-card-checklist 
          class="row card-img m-0 justify-content-center" 
          width="100" height="100"/>
          <div class="row card-body">
            <h5 class="card-title mx-auto">
              <router-link to="/dashboard"> List *.csv records </router-link>
            </h5>
          </div>
        </div>
      </router-link>

      <router-link to="/about" class="d-flex align-content-stretch no-decor m-2">
        <div class="card border-0">
          <b-icon-info-circle
          class="row card-img m-0 justify-content-center" 
          width="100" height="100"/>
          <div class="row card-body">
            <h5 class="card-title mx-auto">
              <router-link to="/about"> About </router-link>
            </h5>
          </div>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
import { BIconCloudUpload, BIconCardChecklist, BIconInfoCircle } from 'bootstrap-vue'
export default {
  name: "HomePage",
  components: {
    BIconCloudUpload,
    BIconCardChecklist,
    BIconInfoCircle,
  },
  data() {
    return {
      introUpload: "Upload *.csv files",
      introDashboard: "List all *.csv files",
      introAbout: "About the application", //this.$store.getters.intro_about,
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
a {
  list-style-type: none;
  padding: 10px;
}
a {
  color: #42b983;
}
</style>

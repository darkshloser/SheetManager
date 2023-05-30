<template>
    <div>
        <div v-if="!loadingElem.isLoading && documentObject">
          <h3>Document: <u>{{ documentObject.name }}</u></h3>
          <div v-if="validData">
              <div class="row table-border-margin">
                <b-button 
                  variant="outline-info"
                  v-b-tooltip.hover title="Save changes"
                  :disabled="!toUpdate"
                  @click="updateCsv(documentObject.name)"
                >
                  <b-icon-sd-card/>
                </b-button>
                <b-button 
                  variant="outline-danger"
                  v-b-tooltip.hover title="Remove"
                  @click="removeCsv(documentObject.name)"
                >
                  <b-icon-trash/>
                </b-button>
              </div>
              <div class="row table-border-margin">
                  <vue-excel-editor 
                    ref="grid"
                    no-header-edit
                    :free-select="false"
                    filter-row
                    v-model="jsondata"
                    @update="onUpdate"
                  >
                      <vue-excel-column 
                        v-for="[index, col] in documentColumns.entries()" 
                        :key="index" 
                        :field="col" 
                        type="string" 
                        :width="col=='$id' ? '0px' : '100px'" 
                      />
                  </vue-excel-editor>
              </div>
          </div>
        </div>
        <div v-else-if="!loadingElem.isLoading && !documentObject">
          <p class="my-4 text-center">
            <i>
              There are no such document uploaded. Please
              <b-link :to="{ name: 'upload' }">upload</b-link> a *csv file.
            </i>
          </p>
        </div>

        <loading
          :active.sync="loadingElem.isLoading"
          :can-cancel="loadingElem.canCancel"
          :is-full-page="loadingElem.fullPage"
          :opacity="loadingElem.opacity"
        >
          <br/>
          <p><i>Loading ...</i></p>
        </loading>

    </div>
</template>

<script>
import { BIconSdCard, BIconTrash } from 'bootstrap-vue'
import Loading from 'vue-loading-overlay';
import _ from 'lodash';
export default {
  name: "DetailsPage",
  components: {
    BIconSdCard,
    BIconTrash,
    Loading,
  },
  data() {
    return {
      loadingElem: {
        isLoading: true,
        canCancel: false,
        fullPage: true,
        opacity: 0.7,
      },
      documentName: this.$route.params.name,
      jsondata: [],
      toUpdate: false
    };
  },
  computed: {
    documentObject() {
      return this.$store.getters.getAllCsvs.find(
        csvItem => csvItem.name === this.documentName
      )
    },
    documentColumns() {
      return (typeof this.jsondata === 'object' && Array.isArray(this.jsondata) && this.jsondata.length > 0) ? Object.keys(this.jsondata[0]) : []
    },
    validData() {
      return (Array.isArray(this.jsondata) && this.jsondata.length > 0)
    }
  },
  created() {
    Promise.all([this.$store.getters.getCsvByName(this.$route.params.name)])
    .then((result) => {
      if (result[0].json_data) {
        this.jsondata = result[0].json_data.filter((obj) => Object.values(obj).some(val => val !== ''));
      } else {
        this.$store.dispatch('getActiveCsv', this.$route.params.name)
        .then((response) => {
          this.jsondata = response.filter((obj) => Object.values(obj).some(val => val !== ''));
        })
      }
    })
    .finally(() => this.loadingElem.isLoading=false)
  },
  methods: {
    removeCsv(name) {
      this.$store.dispatch('removeCsv', name)
      .then(() => this.$router.push({ name: 'dashboard' }))
    },
    onUpdate() {
      this.toUpdate = true
    },
    prepareNewData() {
      return this.jsondata.map(obj => {
        return _.omit(obj, ['$id']);
      });
    },
    updateCsv(name) {
      Promise.all([this.prepareNewData()])
      .then((result) => {
        return this.$store.dispatch('updateCsv', {name:name, json_data: result[0]})
      })
      .then(() => this.toUpdate = false)
      .catch(() => {
        this.$store.dispatch('sendNotification', {
            heading: `Error while saving the decument`,
            status: 'error'
        });
      })
    }
  }
};
</script>


<style scoped>
.table-border-margin {
  margin-left: 10px;
  margin-right: 10px;
}
button {
  margin-right: 5px;
  margin-bottom: 5px;
}
</style>

<template>
  <div>
    <b-table :items="allItems" :fields="visibleFields" striped show-empty responsive="sm">
      
      <template #table-busy>
        <p class="my-4 text-center">
          <b-spinner class="align-middle"></b-spinner>
        </p>
      </template>

      <template #empty>
        <p class="my-4 text-center">
          <i>
            There are no *.csv files uploaded. Please
            <b-link :to="{ name: 'upload' }">upload</b-link> a *csv file.
          </i>
        </p>
      </template>

      <template #cell(created_at)="row">
        {{ dateToStr(row.item.created_at) }}
      </template>
      
      <template #cell(actions)="row">
        <b-button 
          variant="info"
          size="sm"
          class="mr-2"
          @click="$router.push({ name: 'details', params: { name: row.item.name } });">
            Open
        </b-button>
        <b-button 
          variant="info"
          size="sm"
          class="mr-2"
          @click="row.toggleDetails">
            Enrich *.csv
        </b-button>
        <b-button 
          variant="danger"
          size="sm"
          class="mr-2"
          @click="removeCsv(row.item.name)">
            Delete
        </b-button>
      </template>

      <template #row-details="row">
        <b-card id="enrich-csv">
          <b-row class="mb-2">
            <b-col sm="6" class="text-sm-right" style="vertical-align: bottom;">
              <label style="vertical-align: middle;">URL for external data:</label>
            </b-col>
            <b-col sm="3" class="text-sm-left">
              <b-form-input 
                :id="row.item.name" 
                type="url"
                v-model="urls[row.item.name]"
                :state="isValidUrl(row.item.name)"
                placeholder="https://example.com/posts/"
              ></b-form-input>
            </b-col>
          </b-row>

          <b-button 
            size="sm"
            variant="outline-primary" 
            :disabled="!isValidUrl(row.item.name)"
            @click.stop="loadEnrichModal(row)"
          >
            New merged *.csv
          </b-button>
          <b-button 
            size="sm"
            variant="outline-danger"
            @click="row.toggleDetails"
          >
            Cancel
          </b-button>
        
        </b-card>
      </template>
    </b-table>

    <enrich-csv-modal 
      :apiKeys="apiKeys" 
      :srcKeys="sourceKeys" 
      :apiJson="apiJson"
      :enrichName="enrichName" 
    />

  </div>
</template>

<script>
import EnrichCsvModal from '../components/Modals/EnrichCsvModal.vue';
// import axios from 'axios';

  export default {
    name: "DashboardPage",
    components: {
      EnrichCsvModal,
    },
    data() {
      return {
        visibleFields: ['name', 'created_at', 'actions'],
        items: [],
        urls: {},
        apiKeys: [],
        sourceKeys: [],
        apiJson: [],
        enrichName: '',
        allItems: this.$store.getters.getAllCsvs
      }
    },
    methods: {
      isValidUrl(key) {
        return this.URLValidator(this.urls[key]) ? true : null
      },
      URLValidator(inputUrl) {
        try {
          new URL(inputUrl);
          return true;
        } catch (err) {
          return false;
        }
      },
      removeCsv(name) {
        this.$store.dispatch('removeCsv', name);
      },
      dateToStr(str) {
        try {
          const date = new Date(str);
          return date.toLocaleString() 
        } catch (error) {
          return ''
        }
      },
      loadEnrichModal(row) {
        Promise.all([
          this.$store.dispatch('getApiData', this.urls[row.item.name]),
          this.$store.dispatch('getActiveCsv', row.item.name)
        ])
        .then((results) => {
          if (Object.keys(results[0]).length > 0 && Object.keys(results[0]).length > 0) {
            this.apiKeys = Object.keys(results[0][0])
            this.sourceKeys = Object.keys(results[1][0])
            this.apiJson = results[0]
            this.enrichName = row.item.name
            this.$bvModal.show(
              'modal-prevent-closing', {
                 apiKeys: this.apiKeys,
                 srcKeys: this.sourceKeys,
                 apiJson: this.apiJson,
                 enrichName: this.enrichName
            })
            // reset enrich *.csv option
            this.urls[row.item.name] = ''
            row.toggleDetails()
          } else { throw new Error('No keys available'); }
        })
        .catch(() => {
            this.$store.dispatch('sendNotification', {
                heading: 'Error during external data retrieval',
                status: 'error'
            });
        });
      },
    }
  }
</script>

<style scoped>
button {
  margin-left: 10px;
}
</style>

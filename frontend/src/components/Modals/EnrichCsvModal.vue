<template>
    <b-modal
      id="modal-prevent-closing"
      ref="modal"
      :title="'Enrich record ('+enrichName+') with external data'"
      size="lg"
      body-class="p-0"
      no-close-on-backdrop
      no-close-on-esc
      hide-header-close
      :ok-disabled="!canSubmit"
      @hidden="resetModal"
      @ok="handleSubmit"
    >
      <form ref="form" class="padding-0">
        
            <table class="table table-sm">
                <thead>
                  <tr class="align-center">
                    <th scope="col">Key Pairs</th>
                    <th scope="col">Source key field</th>
                    <th scope="col">API key field</th>
                  </tr>
                </thead>
                <tbody class="padding-0">
                  
                  <tr v-for="keyPair in keyPairOptions" :key="keyPair.value" class="align-center">
                    <th class="vertical-align" scope="row">
                      <b-form-radio
                        v-model="selKeyPairMode"
                        :aria-describedby="ariaDescribedby"
                        name="radios-stacked"
                        :value="keyPair.value"
                        > {{ keyPair.text }}</b-form-radio
                      >
                    </th>
                    <td>
                      <b-dropdown
                        v-model="keyPairValues[keyPair.value].source"
                        :text="srcKeyField(keyPairValues[keyPair.value].source)"
                        :variant="styleDropDown(keyPairValues[keyPair.value].source)"
                        :disabled="keyDisabled(keyPair.value)"
                        class="key-field-style padding-10"
                      >
                        <b-dropdown-item
                          v-for="option in srcKeys"
                          :key="option"
                          :value="option"
                          :disabled="selectableSourceKey(option)"
                          @click="
                            keyPairValues[keyPair.value].source = srcKeys.indexOf(option)
                          "
                        >
                          {{ option }}
                        </b-dropdown-item>
                      </b-dropdown>
                    </td>
                    <td>

                      <b-dropdown
                        v-model="keyPairValues[keyPair.value].api"
                        :text="apiKeyField(keyPairValues[keyPair.value].api)"
                        :variant="styleDropDown(keyPairValues[keyPair.value].api)"
                        :disabled="keyDisabled(keyPair.value)"
                        class="key-field-style padding-10"
                      >
                        <b-dropdown-item
                          v-for="option in apiKeys"
                          :key="option"
                          :value="option"
                          :disabled="selectableApiKey(option)"
                          @click="keyPairValues[keyPair.value].api = apiKeys.indexOf(option)"
                        >
                          {{ option }}
                        </b-dropdown-item>
                      </b-dropdown>
                      
                    </td>
                  </tr>
                </tbody>
            </table>
        
      </form>


    </b-modal>
</template>

<script>

  export default {
    name: 'EnrichCsvModal',
    components: {},
    props: {
      enrichName: {
        type: String,
        default: ''
      },
      apiKeys: {
        type: Array,
        default: null
      },
      srcKeys: {
        type: Array,
        default: null
      },
      apiJson: {
        type: Array,
        default: null
      }
    },
    data() {
      return {
        selKeyPairMode: 0,
        keyPairOptions: [
          {text: 'One', value: 0},
          {text: 'Two', value: 1}
        ],
        keyPairValues: [
          { source: 0, api: 0 },
          { source: null, api: null },
        ]
      }
    },
    computed: {
      canSubmit() {
        return (
          Object.values(this.keyPairValues[0]).filter((x) => x == null).length === 0 &&
          (
            Object.values(this.keyPairValues[1]).filter((x) => x == null).length === 0 ||
            Object.values(this.keyPairValues[1]).filter((x) => x == null).length === 2
          )
        );
      }
    },
    methods: {
      srcKeyField(fieldIdx) {
        return fieldIdx == null ? "Key field" : this.srcKeys[fieldIdx];
      },
      apiKeyField(fieldIdx) {
        return fieldIdx == null ? "Key field" : this.apiKeys[fieldIdx];
      },
      defaultKeys(idxKeys) {
        if (idxKeys == 0) {
          this.keyPairValues[idxKeys].source = idxKeys
          this.keyPairValues[idxKeys].api = idxKeys
        } else {
          this.keyPairValues[idxKeys].source = null
          this.keyPairValues[idxKeys].api = null
        }
      },
      keyDisabled(idxKeyPair) {
          if (idxKeyPair > this.selKeyPairMode) {
            this.defaultKeys(idxKeyPair)
            return true
          } else { 
            return false
          }
      },
      selectableSourceKey(key) {
        return (
          this.srcKeys.indexOf(key) === this.keyPairValues[0].source ||
          this.srcKeys.indexOf(key) === this.keyPairValues[1].source
        );
      },
      selectableApiKey(key) {
        return (
          this.apiKeys.indexOf(key) === this.keyPairValues[0].api ||
          this.apiKeys.indexOf(key) === this.keyPairValues[1].api
        );
      },
      styleDropDown(val) {
        return val !== null ? "outline-info" : "outline-dark";
      },
      resetModal() {
        for (let i = 0; i < this.keyPairOptions.length; i++) {
          this.defaultKeys(i)
        }
        this.selKeyPairMode = 0
        this.$refs.modal.hide();
      },
      handleSubmit() {
        this.$store.dispatch(
          'enrichCsv', 
          {
            enrichName: this.enrichName,
            externalJson: this.apiJson,
            source_key: this.srcKeys[this.keyPairValues[0].source],
            api_key: this.apiKeys[this.keyPairValues[0].api],
            second_src_key: this.srcKeys[this.keyPairValues[1].source],
            second_api_key: this.apiKeys[this.keyPairValues[1].api]
          }
        )
        .then(() => {
          setTimeout(() => { 
            this.$router.push({ name: 'dashboard' }) 
          }, 100)
        })
        .catch(() => {
          this.$store.dispatch('sendNotification', {
            heading: `Error during enrichment of "${this.formData.name}" record`,
            duration: 7000,
            status: 'error'
          });
        });
        
      }
    }
  }
</script>

<style scoped>
.padding-0 {
  padding: 0;
}
.padding-10 {
    padding: 10px;
}
.key-field-style {
  width: 250px;
}
.align-center {
  text-align: center;
}
tr td{
  padding-top: 5px !important;
  padding-bottom: 5px !important;
  margin-top: 5px !important;
  margin-bottom: 5px !important;
}
.vertical-align {
  text-align: center;
  vertical-align: middle;
}
</style>
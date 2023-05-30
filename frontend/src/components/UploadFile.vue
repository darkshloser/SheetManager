<template>
    <b-container fluid>
      <b-form @submit="onSubmit" >
      <b-row class="my-1" v-for="item in inputElements" :key="item.name">
        <b-col sm="3">
          <label>{{ item.name }}</label>
        </b-col>
        <b-col sm="6">
          <b-form-input 
            v-if="item.type != 'file'" 
            :id="`type-${item.type}`" 
            :type="item.type"
            v-model="formData.name"
          ></b-form-input>

          <b-form-file 
            v-else 
            single 
            accept=".csv" 
            v-model="formData.file"
          ></b-form-file>
        </b-col>
      </b-row>
      <br/>
      <b-button type="submit" variant="primary">Submit</b-button>
      </b-form>
    </b-container>
</template>

<script>
export default {
      data() {
        return {
          inputElements: [
            {name: 'Name', type: 'text'},
            {name: 'File (*.csv)', type: 'file'}
          ],
          formData: {
            name: '',
            file: null
          }
        }
      },
      methods: {
        onSubmit(event) {
            event.preventDefault()
            this.$store.dispatch('uploadCsv', this.formData)
            .then(() => {
              setTimeout(() => { 
                this.$router.push({ name: 'dashboard' }) 
              }, 100)
            })
            .catch(() => {
              this.$store.dispatch('sendNotification', {
                heading: `Error during upload of "${this.formData.name}" record`,
                duration: 7000,
                status: 'error'
              });
            });
            
        },
      }
    }
</script>
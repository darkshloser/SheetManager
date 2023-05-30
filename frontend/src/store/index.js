import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import Toasted from 'vue-toasted';


Vue.use(Vuex);
Vue.use(Toasted);


export default new Vuex.Store({
    state: {
        dataInSync: false,
        allCsvs: [],
    },
    mutations: {
        setDataInSync(state) {
            state.dataInSync = true;
        },
        getAllCsvs(state, data) {
            state.allCsvs = data
        },
        removeCsv(state, nameCsv) {
            let selCsvIdx = state.allCsvs.findIndex(csvItem => csvItem.name === nameCsv);
            if (selCsvIdx > -1) {
                state.allCsvs.splice(selCsvIdx, 1)
            }
        },
        updateActiveCsvJson(state, activeCsv) {
            state.allCsvs.forEach((csv) => {
                if (csv.name == activeCsv.name && activeCsv.json_data) {
                        csv.json_data = activeCsv.json_data;
                }
            })
        },
        uploadCsv(state, uploadedCsv) {
            state.allCsvs.push({
                name: uploadedCsv.name,
                file: uploadedCsv.file,
                created_at: uploadedCsv.created_at
            })
        },
    },
    actions: {
        getAllCsvs(context) {
            return new Promise((resolve, reject) => {
                axios
                  .get(`http://localhost:8000/api/v1/file/`)
                  .then(({ data }) => {
                    resolve(context.commit('getAllCsvs', data))
                  })
                  .then(() => {
                    resolve(context.commit('setDataInSync'))
                  })
                  .catch(() => {
                    context.dispatch('sendNotification', {
                       heading: 'Error to fetch uploaded *.csv files',
                       status: 'error'
                    });
                    reject(new Error('Failed to retrieve all the records'));
                  });
            });
        },
        getActiveCsv(context, csvName) {
            return axios.get(`http://localhost:8000/api/v1/file?name=${csvName}`)
                .then((response) => {
                    return JSON.parse(response.data[0].json_data)
                })
                .then((data) => {
                    if (data.constructor == Object) { 
                        context.commit('updateActiveCsvJson', {name: csvName, json_data: [data]} )    
                    } else {
                        context.commit('updateActiveCsvJson', {name: csvName, json_data: data} )
                    }
                    return data.constructor === Object ? [data] : data
                })
                .catch(() => {
                    context.dispatch('sendNotification', {
                        heading: `Error during retrieval of ${csvName}`,
                        status: 'error'
                    });
                });
        },
        removeCsv({commit, dispatch}, csvName ) {
            return axios.delete(`http://localhost:8000/api/v1/file?name=${csvName}`)
                .then((response) => {
                    if (response.status === 204 || response.status === 410) {
                        commit('removeCsv', csvName)
                        dispatch('sendNotification', {
                            heading: `File "${csvName}" was successfully removed`,
                        });
                    } else {
                        throw new Error("Backend is not able to complete this operation")
                    }
                })
                .catch(() => {
                    dispatch('sendNotification', {
                        heading: `Error during removal of "${csvName}"`,
                        status: 'error'
                    });
                });
        },
        uploadCsv({commit, dispatch}, fileData) {
            const formData = new FormData();
            formData.append('file', fileData.file);
            formData.append('name', fileData.name);
            return axios({
                method: 'post',
                url: `http://localhost:8000/api/v1/file/`,
                data: formData,
                headers: {
                    'Content-Type': 'multipart/form-data; boundary=${formSerializer._boundary}'
                },
            })
            .then((response) => {
                if (response.status === 201) { 
                    commit('uploadCsv', response.data)
                    dispatch('sendNotification', {
                        heading: `File "${fileData.name}" was successfully uploaded`,
                        duration: 7000,
                        status: 'success'
                    })
                } else { 
                    throw false 
                }
            })
        },
        updateCsv({commit, dispatch}, data) {
            return axios({
                method: 'put',
                url: `http://localhost:8000/api/v1/file/?name=${data.name}`,
                data: {
                    json_data: JSON.stringify(data.json_data)
                },
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then((response) => {
                if (response.status === 200) {
                    commit('updateActiveCsvJson', {name: data.name, json_data: data.json_data} ) 
                    dispatch('sendNotification', {
                        heading: `${data.name} saved`,
                        duration: 1000,
                        status: 'success'
                    })
                } else { 
                    throw false 
                }
            })
        },
        enrichCsv({commit, dispatch}, enrichData) {
            return axios({
                method: 'post',
                url: `http://localhost:8000/api/v1/enrich/`,
                data: {
                    name: enrichData.enrichName,
                    additional_api_json: JSON.stringify(enrichData.externalJson),
                    key_column_stored: enrichData.source_key,
                    key_column_api: enrichData.api_key,
                    second_src_key: ('second_src_key' in enrichData) ? enrichData.second_src_key : null,
                    second_api_key: ('second_api_key' in enrichData) ? enrichData.second_api_key : null
                },
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then((response) => {
                if (response.status === 201) { 
                    commit('uploadCsv', response.data)
                    dispatch('sendNotification', {
                        heading: `Enriched data was stored in "${response.data.name}" successfully`,
                        duration: 7000,
                        status: 'success'
                    })
                } else { 
                    throw false 
                }
            })
        },
        getApiData(context, url) {
            return axios({
                method: 'get',
                url: `${url}`,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then((response) => {
                if ((!!response.data) && (response.data.constructor === Array)) {
                    return response.data
                } else if ((!!response.data) && (response.data.constructor === Object)) {
                    return [response.data]
                } else {
                    throw new Error('Wrong response type');
                }
            })
        },
        sendNotification(context, description) {
            let props = {
                position: 'bottom-center',
                duration: description.duration ? description.duration : 4000,
                className: 'auto-test-toast',
                status: ('status' in description) ? description.status : 'info'
            }
            if (description.status == 'success') { Vue.toasted.success(`${description.heading}`, props); } 
            else if (description.status == 'error') { Vue.toasted.error(`${description.heading}`, props); }
            else { Vue.toasted.show(`${description.heading}`, props); }
        },
    },
    getters: {
        isDataInSync(state) {
            return state.dataInSync
        },
        getAllCsvs (state) {
            return state.allCsvs
        },
        getCsvByName: state => (name) => {
            return state.allCsvs.find(csv_item => csv_item.name === name);
        }
    }

})
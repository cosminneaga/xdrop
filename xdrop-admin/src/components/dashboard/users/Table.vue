<template>
  <v-card>

    <v-card-title>
      XDrop Licences
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>

    <v-data-table
      :headers="headers"
      :items="licences"
      :search="search"
      item-key="licence"
      :items-per-page="tableOptions.itemsPerPage"
      :mobile-breakpoint="tableOptions.mobileBreakpoint"
      class="elevation-3"
      loading-text="Loading... Please wait"
      :loading="loadingState"
      :single-expand="true"
      :expanded.sync="expanded"
      show-expand>

    <template v-slot:item.plan="{item}">
        <v-chip dark :color="getPlanColor(item.plan)">{{item.plan}}</v-chip>
    </template>
    
    <template v-slot:expanded-item="{ headers, item }">
      <td :colspan="headers.length">
        
        
        <v-container fluid class="my-3">
            <p class="text-h6">Extend <span class="blue--text darken--3">{{item.licence}}</span> datetime frame</p>
            <v-container class="d-inline-block align-content-center py-5">
                <v-slider
                  v-model="sliderDays.val"
                  :label="sliderDays.label"
                  :thumb-color="sliderDays.color"
                  :min="sliderDays.min"
                  :max="sliderDays.max"
                  thumb-label="always"
                ></v-slider>

                <v-slider
                  v-model="sliderHours.val"
                  :label="sliderHours.label"
                  :thumb-color="sliderHours.color"
                  :min="sliderHours.min"
                  :max="sliderHours.max"
                  thumb-label="always"
                ></v-slider>
            </v-container>
            <v-row>
                <v-btn depressed color="primary" @click="getExtendedLicence(item.licence, sliderDays.val, sliderHours.val)">Extend licence</v-btn>
            </v-row>
        </v-container>

      </td>
    </template>
    

    </v-data-table>

  </v-card>
</template>

<script>
import {state} from '../../../store'

  export default {
    data () {
      return {
        loadingState: false,
        search: '',
        expanded: [],
        tableOptions: {
          itemsPerPage: 15,
          mobileBreakpoint: 800
        },
        sliderDays: { label: 'Days', val: 0, color: 'red', min: 0, max: 30 },
        sliderHours: { label: 'Hours', val: 12, color: 'blue', min: 0, max: 23 },
        headers: [
          { text: 'Licence', align: 'start', sortable: true, value: 'licence', class: 'red--text', cellClass:'blue--text'},
          { text: 'Validity', value: 'validity', width: '200px' },
          { text: 'Plan', value:'plan'},
          { text: 'Created On', value: 'created_on', width: '200px' }
        ],
        licences: [],
      }
    },
    methods: {
        async fetchLicences(){
            this.loadingState = true
            try{
              const response = await this.$axios.get('xdropadmin/admin/get/licences')
              return response.data
            }catch(e){
              console.log(e)
            }
        },
        async getExtendedLicence(licence, days, hours){
            const confirmed = confirm(`Please confirm to extend the licence: ${licence} to this amount of days: ${days}`)
            if (confirmed){
                try{
                  const obj = { licence: licence, days: days, hours: hours }
                  await this.$axios.post('xdropadmin/admin/update/length/licence', obj)
                  this.$router.go(0)
                }catch(e){
                  console.log(e)
                }
            }
        },
        getPlanColor(item){
            switch(item){
                case 'free':
                    return 'red'
                case 'regular':
                    return 'blue'
                default:
                    return 'green'
            }
        }
    },
    async created(){
        const response = await this.fetchLicences()
        setTimeout(() => {
            this.loadingState = false
        }, 500)
        state.licences = response.licences.length
        this.licences = response.licences
    }
  }
</script>

<style scoped>
*{
  word-break: break-all!important;
  text-overflow: ellipsis!important;
}
</style>
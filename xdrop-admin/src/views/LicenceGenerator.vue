<template>
    <div>
<Navigation />
<v-container class="mt-10">

        <v-form
    ref="form"
    v-model="valid"
    lazy-validation
  >
    <p class="text-body-1 mb-10">Set Validity</p>
    
    <v-slider
      v-model="sliderDays.val"
      :color="sliderDays.color"
      :label="sliderDays.label"
      :min="sliderDays.min"
      :max="sliderDays.max"
      :thumb-color="sliderDays.color"
      thumb-label="always"
    ></v-slider>

    <v-slider
      v-model="sliderHours.val"
      :color="sliderHours.color"
      :label="sliderHours.label"
      :min="sliderHours.min"
      :max="sliderHours.max"
      :thumb-color="sliderHours.color"
      thumb-label="always"
    ></v-slider>


    <v-select
      v-model="select"
      :items="items"
      :rules="[v => !!v || 'Plan is required']"
      label="Set Payment Plan"
      required
    ></v-select>

    <v-checkbox
      v-model="checkbox"
      :rules="[v => !!v || 'You must be sure to continue!']"
      label="Are you sure?"
      required
    ></v-checkbox>

    <v-alert
      prominent
      :type="alert.type"
      border="left"
      transition="scale-transition"
      :value="alert.show"
      dismissible
      close-icon="mdi-close-circle-multiple-outline"
      shaped
    >
      <v-row align="center">
        <v-col class="grow">

          <p class="text-body-1">{{alert.message}}</p>
          <v-container v-if="alert.type === 'success' ? true : false">
              <v-text-field
                label="Licence"
                outlined
                dark
                color="purple"
                background-color="blue darken-1"
                v-model="alert.inputValue"
                ref="licenceText"></v-text-field>
                
                <v-btn @click="copyLicenceToClipboard()">Copy to clipboard</v-btn>
          </v-container>

        </v-col>
      </v-row>
    </v-alert>

    <v-btn
      :disabled="!valid"
      color="success"
      class="mr-4"
      @click="validate"
    >Create Licence</v-btn>

  </v-form>
    </v-container>
    <Footer />
    </div>
</template>


<script>
import Navigation from '@/components/Navigation.vue'
import Footer from '@/components/Footer.vue'

  export default {
    name: 'LicenceGenerator',
    components: {Navigation, Footer},
    data: () => ({
      alert:{
          show: false,
          type: 'success',
          message: '',
          inputValue: '',
      },
      valid: true,
      sliderDays: { label: 'Days', val: 0, color: 'red darken-1', min: 0, max: 30 },
      sliderHours: { label: 'Hours', val: 12, color: 'blue darken-1', min: 0, max: 30 },
      select: null,
      items: [
        'premium',
        'regular',
        'free',
      ],
      checkbox: false,
    }),

    methods: {
      async validate () {
        const validate = this.$refs.form.validate()
        if(validate){
            await this.createLicenceRequest()
        }
      },
      reset () {
        this.$refs.form.reset()
      },
      unblockFormSubmission(){
          this.valid = true
          this.alert.show = false
      },
      blockFormSubmission(){
          this.valid = false
      },
      async createLicenceRequest(){
          const obj = {
              days: this.sliderDays.val,
              hours: this.sliderHours.val,
              plan: this.select
          }
          try{
            const response = await this.$axios.post('xdropadmin/admin/admin-create/new-licence', obj)
            this.alert.message = 'A new licence has been created successfully.'
            this.alert.show = true;
            this.alert.inputValue = response.data.message;
          }catch(e){
              this.alert.message = 'An error occured please check the licences table to make sure the licence has been issued... Otherwise please contact the administrator.'
              this.alert.type = 'error';
              this.alert.show = true;
          }
      },
      copyLicenceToClipboard(){
          this.$refs.licenceText.focus()
          navigator.clipboard.writeText(this.$refs.licenceText.value)
      }
    },
  }
</script>
<template>
    <PanelNavigation>
        
        <v-alert
        proeminent
        type="info">
            <strong>Useful links: </strong>            
            <a href="/how-to#obtain-api_id" target="_blank" rel="noopener noreferrer" style="color: #fff;">How to obtain api_id</a>
            <a href="/how-to#deregister" target="_blank" rel="noopener noreferrer" style="color: #fff;">How to deregister</a>
        </v-alert>
        
<v-sheet class="form-container" elevation="15" rounded>
    <v-container v-if="!formState.completed">
      <p class="text-h5">You must register your Telegram App before commence shilling.</p>
    </v-container>
    <v-container v-if="formState.completed">
      <span class="text-h4 blue--text">Telegram App Registered</span>
    </v-container>

    <v-form @submit.prevent="submit(formState.case)">
    <v-container>
      <v-row>
        <v-col
          cols="12"
          md="4">
          <v-text-field
            v-model="fields.id"
            label="API ID"
            name="id"
            placeholder="123456"
            outlined
            :disabled="formState.completed"
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="fields.hash"
            label="API HASH"
            name="hash"
            placeholder="dasgh43242hgh"
            outlined
            :disabled="formState.completed"
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4">
          <v-text-field
            v-model="fields.phone"
            label="PHONE"
            name="phone"
            type="phone"
            placeholder="+112223334455"
            outlined
            :disabled="formState.completed"
          ></v-text-field>
        </v-col>
      </v-row>

      <v-row v-if="formState.code">
        <v-col cols="12" md="6">
          <v-alert
            border="left"
            dense
            type="info"
          >Please check your Telegram chat for any code received by Telegram.</v-alert>
          <v-text-field
          v-model="fields.code"
          label="PHONE CODE"
          name="phone_code"
          type="text"
          outlined
          color="red"></v-text-field>
        </v-col>
      </v-row>

      <v-row v-if="formState.password">
        <v-col cols="12" md="6">
          <v-alert
            border="left"
            dense
            type="info"
          >The password field is required if you have two-steps verification password activated.</v-alert>
          <v-text-field
          v-model="fields.password"
          label="PASSWORD"
          name="password"
          :type="formState.passwordShow ? 'text' : 'password'"
          outlined
          color="red"></v-text-field>

          <v-switch
          v-model="formState.passwordShow"
          label="Show password"></v-switch>
        </v-col>
      </v-row>

      <v-row>
          <v-col cols="12">
              <v-btn
              type="submit"
              x-large
              :loading="formState.loading"
              :color="formState.code ? 'info' : formState.password ? 'primary' : formState.completed ? 'red' : 'success'"
              dark>
              {{formState.code ? 'register' : formState.password ? 'register with password' : formState.completed ? 'deregister' : 'get request code'}}
            </v-btn>

            <v-btn
            v-if="formState.code || formState.password"
            x-large
            color="red"
            dark
            @click="resetForm">
              reset
            </v-btn>

            <NuxtLink to="/panel/message" style="text-decoration: none;" v-show="formState.completed">
              <v-btn
              x-large
              color="success"
              dark
              elevation="10"
              outlined>
                go to shill page
              </v-btn>
            </NuxtLink>

          </v-col>
      </v-row>
    </v-container>
</v-form>
</v-sheet>

    </PanelNavigation>
</template>

<script>
export default {
    middleware: 'auth',
    data(){
      return {
        fields: {
          id: this.retrieveDataObjectFromSessionStorage('TelegramCredentials', 'id'),
          hash: this.retrieveDataObjectFromSessionStorage('TelegramCredentials', 'hash'),
          phone: this.retrieveDataObjectFromSessionStorage('TelegramCredentials', 'phone'),
          code: '',
          password: ''
        },
        formState: {
          code: false,
          password: false,
          case: 'send_code_request',
          completed: false,
          loading: false,
          passwordShow: false
        },
      }
    },
    beforeCreate(){
      sessionStorage.getItem('registerFormState') ? sessionStorage.getItem('registerFormState') : sessionStorage.setItem('registerFormState', 'send_code_request')
    },
    created() {
      let formState = sessionStorage.getItem('registerFormState')
      switch(formState){
        case 'register_with_password':
          this.formState.case = 'register_with_password'
          this.formState.code = false
          this.formState.password = true
          break;
        case 'register_with_code':
          this.formState.case = 'register_with_code'
          this.formState.code = true
          this.formState.password = false
          break;
        case 'completed':
          this.formState.case = 'deregister'
          this.formState.code = false
          this.formState.password = false
          this.formState.completed = true
          break;
        default:
          this.formState.case = 'send_code_request'
          this.formState.code = false
          this.formState.password = false
          break;
      }
    },
    watch: {
        '$store.state.theme.dark': function () {
            this.$vuetify.theme.isDark = this.$store.state.theme.dark
            // console.log(this.$store.state.theme.dark);
        }
    },
    methods: {
      async submit(urlParams){        
          let res
          switch(urlParams){

            case 'send_code_request':
              res = await this.request({
                  id: this.fields.id,
                  hash: this.fields.hash,
                  phone: this.fields.phone
                }, 'send_code_request')
              if (res.success === false) return alert(res.data.message)
              this.formState.code = true
              this.formState.case = 'register_with_code'
              sessionStorage.setItem('registerFormState', 'register_with_code')
              sessionStorage.setItem('TelegramCredentials', JSON.stringify(res.data))
              break;


            case 'register_with_code':
              res = await this.request({
                ...JSON.parse(sessionStorage.getItem('TelegramCredentials')),
                phone_code: this.fields.code
              }, 'register_with_code')
              
              if (res.success === true) {
                sessionStorage.setItem('registerFormState', 'completed')
                this.formState.case = 'deregister'
                this.formState.code = false
                this.formState.password = false
                this.formState.completed = true 

                this.$store.commit('setRegisteredStatus', true)
              }
              else if (res.success === false && res.data.passwordNeeded){
                this.formState.code = false
                this.formState.password = true
                this.formState.case = 'register_with_password'
                sessionStorage.setItem('registerFormState', 'register_with_password')
              }else if (res.success === false){
                alert(res.data.message)
              }
              break;


            case 'register_with_password':
              res = await this.request({
                  ...JSON.parse(sessionStorage.getItem('TelegramCredentials')),
                  password: this.fields.password
                }, 'register_with_password')
              if (res.success === false) return alert(res.data.message)
              if (res.success === true) {
                sessionStorage.setItem('registerFormState', 'completed')
                this.formState.case = 'deregister'
                this.formState.code = false
                this.formState.password = false
                this.formState.completed = true  

                this.$store.commit('setRegisteredStatus', true)
              }
              break;

            case 'deregister':
              res = await this.request({
                ...JSON.parse(sessionStorage.getItem('TelegramCredentials'))
              }, 'deregister')
              if(res.success === true){
                sessionStorage.removeItem('TelegramCredentials')
                sessionStorage.setItem('registerFormState', 'send_code_request')
                this.formState.case = 'send_code_request'
                this.formState.code = false
                this.formState.password = false
                this.formState.completed = false
                for (const item in this.fields) this.fields[item] = ''

                this.$store.commit('setRegisteredStatus', false)
              }
              break;
          }

          /* console.log('submit(): ');
          console.log(res); */
                    
      },
      async request(object, queryStep){

        this.formState.loading = true

        try{

          const res = await this.$axios.$post(this.$axios.defaults.baseURL + '/register-deregister', object, {params: {step: queryStep}})
          this.formState.loading = false

          // console.log('axios: ', res);

          return res

        }catch(err){
          
          console.log('REQUEST ERROR: ' + err);
          alert('network_error - please contact the site administrator.')
          this.formState.loading = false
          return false

        }
      },
      resetForm(){
        if (sessionStorage.getItem('TelegramCredentials')) sessionStorage.removeItem('TelegramCredentials')
        if (sessionStorage.getItem('registerFormState')) sessionStorage.setItem('registerFormState', 'send_code_request')
        this.formState.case = 'send_code_request'
        this.formState.password = false
        this.formState.code = false
        this.formState.loading = false
        this.fields.code = ''
        this.fields.password = ''
      },
      retrieveDataObjectFromSessionStorage(item, field){
        if (sessionStorage.getItem(item)) return JSON.parse(sessionStorage.getItem(item))[field]
      }
    }
}
</script>

<style lang="scss" scoped>
    .form-container{
        padding: 50px 20px;
    }
</style>
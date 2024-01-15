<template>
    <v-container fluid align="center" style="position: relative; height: 95vh; display: flex; align-items: center; justify-content: center;"> 

            <Logo style="position: absolute; top: 0; width: 100%; height: 90vh; z-index: 0;"/>

            

            <v-container style="max-width: 800px; padding:0; margin:0; z-index: 5;">
                <v-alert
                border="left"
                dismissible
                elevation="8"
                type="warning">
                Please make yourself aware of Telegram rules as your account may be banned if you don't interact with Telegram in a good manner way.
                <br>
                <a href="https://telegram.org/tos" target="_blank" rel="noopener noreferrer" style="color: #fff;">Telegram TOS</a>
                </v-alert>
                <v-container style="background: rgb(2,0,36, 0.9); background: linear-gradient(90deg, rgba(2,0,36, 0.9) 0%, rgba(9,9,121, 0.9) 22%, rgba(0,212,255, 0.9) 100%);  color: #fff;" rounded-lg class="py-15 elevation-12">

                    <v-form @submit.prevent="formSubmitFunction">

                    <h2 class="text--success">Enter your XDropPro licence</h2>
                    <v-text-field
                    v-model="licence.value"
                    :error-messages="licence.error"
                    label="Licence"
                    hint="If you don't have a licence please go to our Telegram group and ask our administrator for one."
                    persistent-hint
                    filled
                    outlined
                    dark
                    name="licence"></v-text-field>

                    <v-alert
                    v-show="responseStatusOnline"
                    border="left"
                    type="warning"
                    colored-border
                    elevation="12"
                    >The licence you are trying to use has a open session, if you wish to continue using this licence on this tab, press <span class="red--text">LOGOUT</span> button to logout from the previous session, and then log back again.</v-alert>

                    <v-btn
                    type="submit"
                    x-large
                    :color="responseStatusOnline ? 'red' : 'success'"
                    dark
                    :loading="loading"> {{responseStatusOnline ? 'LOGOUT' : 'LOGIN'}} </v-btn>

                    </v-form>
                    <br><br>
                    <NuxtLink to="/" style="color: #fff;">Go back to main page</NuxtLink>
                </v-container>
            </v-container>



    </v-container>
</template>

<script>
export default {
    data() {
        return {
            licence: {
                value: '',
                error: ''
            },
            loading: false,
            responseStatusOnline: false,
            formSubmitFunction: this.submit
        }
    },
    methods: {
        async submit(e){
            try {

                this.loading = true
                const res = await this.$axios.$post(this.$axios.defaults.baseURL + '/login', {licence: e.target.elements.licence.value})
                // console.log(res);
                
                this.loading = false
                if (res.data) {
                    if (res.data.online) {
                        this.responseStatusOnline = res.data.online
                        this.formSubmitFunction = this.logout
                    }
                }
                if (res.success === false) return this.licence.error = res.data.message

                this.licence.value = ''
                this.licence.error = ''
                sessionStorage.setItem('token', res.token)
                this.$store.commit('setAuth', res.token)
                
                await this.$router.push({path: '/panel'})

            }catch(err){

                this.licence.error = err
                this.loading = false

            }
        },
        async logout(e){
            try{
                const res = await this.$axios.$post(this.$axios.defaults.baseURL + '/delete_session', {licence: e.target.elements.licence.value})
                if (res.success === true){
                    this.licence.value = ''
                    this.licence.error = ''
                    this.responseStatusOnline = false
                    this.formSubmitFunction = this.submit
                    return
                }

                this.licence.error = res.data.message
            }catch(err){
                console.log(err)
            }
        }
    }
}
</script>

<template>
    
    <v-container class="mt-16" style="position: relative; max-width: 600px;">
        
        <p class="text-h3">Login.</p>
        <v-form
        ref="form"
        v-model="formValid"
        lazy-validation
        @submit.prevent="validate">
                <v-row>
                    <v-col xs="6">
                        <v-text-field
                        v-model="data.id"
                        label="ID"
                        required
                        :rules="[v => !!v || 'ID is required.']"
                        ></v-text-field>
                    </v-col>
                    <v-col xs="6">
                        <v-text-field
                        v-model="data.password"
                        label="Password"
                        required
                        type="password"
                        :rules="[v => !!v || 'Password is required.']"
                        ></v-text-field>
                    </v-col>
                </v-row>
                <v-row>
                    <v-alert
                    prominent
                    type="error"
                    border="left"
                    transition="scale-transition"
                    :value="alert.show"
                    dismissible
                    close-icon="mdi-close-circle-multiple-outline"
                    shaped
                    >
                        <v-row align="center">
                            <v-col class="grow">
                                <p class="text-body-1" style="word-break: break-all;">{{alert.message}}</p>
                            </v-col>
                        </v-row>
                    </v-alert>
                </v-row>
                <v-row>
                    <v-btn
                    color="primary"
                    dark
                    large
                    absolute
                    right
                    :loading="btn.loading"
                    elevation="12"
                    :disabled="!formValid"
                    type="submit">Login.</v-btn>
                </v-row>
        </v-form>
    </v-container>
    
</template>

<script>
export default {
    name: 'Login',
    data: () => ({
        formValid: true,
        data: {
            id: '',
            password: ''
        },
        btn: {
            loading: false
        },
        alert: {
            show: false,
            message: ''
        }
    }),

    methods: {
      async validate () {
        const validate = this.$refs.form.validate()
        if(validate){
            const obj = {
                id: this.data.id,
                password: this.data.password
            }
            
            try{
                const response = await this.$axios.post(`xdropadmin/login/admin-login`, obj)
                sessionStorage.setItem('logged', true)
                sessionStorage.setItem('sessionKey', response.data.token)
                this.$router.push({
                    path: '/licences'
                })
                console.log(response);
            }catch(e){
                this.alert.message = `${e.response.data.message} \n ${e.response.data.error_type}`
                this.alert.show = true
                console.log(e.response);
            }
        }
      },
    },
}
</script>
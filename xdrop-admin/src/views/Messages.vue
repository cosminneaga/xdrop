<template>
    <div>
        <Navigation />
        <v-container class="container-sm">
            <v-snackbar
            v-model="snackbar.show"
            :vertical="snackbar.vertical"
            absolute
            centered
            elevation="24"
            color="success"
            >
            {{snackbar.text}}
            <template v-slot:action="{ attrs }">
                <v-btn
                color="indigo"
                text
                v-bind="attrs"
                @click="snackbar.show = false"
                >
                Close
                </v-btn>
            </template>
            </v-snackbar>

            <v-container class="mb-4">
                <v-textarea
                outlined
                v-model="textarea.regular.value"
                label="Regular"
                rows="10"></v-textarea>

                <v-btn
                type="button"
                elevation="2"
                class="mx-2"
                fab
                dark
                color="purple"
                large
                @click="emoji.regular.show = !emoji.regular.show">
                <v-icon>mdi-emoticon</v-icon></v-btn>
                <VEmojiPicker v-if="emoji.regular.show" @select="insertEmojiRegularField" />
            </v-container>

            <v-container class="mb-4">
                <v-textarea
                outlined
                v-model="textarea.free.value"
                label="Free"
                rows="10"></v-textarea>

                <v-btn
                type="button"
                elevation="2"
                class="mx-2"
                fab
                dark
                color="blue"
                large
                @click="emoji.free.show = !emoji.free.show">
                <v-icon>mdi-emoticon</v-icon></v-btn>
                <VEmojiPicker v-if="emoji.free.show" @select="insertEmojiFreeField" />
            </v-container>

            

            <v-btn
            class="ma-2"
            :loading="button.loading"
            :disabled="button.loading"
            color="info"
            @click="setDefaultMessages"
            type="submit"
            >
            Set default text
            <template v-slot:loader>
                <span class="custom-loader">
                <v-icon light>mdi-cached</v-icon>
                </span>
            </template>
            </v-btn>
        
    </v-container>
    <Footer />
    </div>
</template>

<script>
import {state} from '../store'
import { VEmojiPicker } from 'v-emoji-picker';
import Navigation from '@/components/Navigation.vue'
import Footer from '@/components/Footer.vue'

export default {
    name: 'Messages',
    components: {VEmojiPicker, Navigation, Footer},
    data() {
        return {
            snackbar: {
                show: false,
                text: 'Lorem ipsum dolor sit amet.',
                vertical: true
            },
            emoji: {
                regular: { show: false },
                free: { show: false }
            },
            button: {
                loading: false,
            },
            textarea: {
                regular: { value: '' },
                free: { value: '' }
            }
        }
    },
    methods: {
        insertEmojiFreeField(emoji){
            this.textarea.free.value += emoji.data
        },
        insertEmojiRegularField(emoji){
            this.textarea.regular.value += emoji.data
        },
        loader(){
            this.button.loading = !this.button.loading
            setTimeout(() => {this.button.loading = false}, 3000)
        },
        async setDefaultMessages(){
            try{
                this.button.loading = true
                const response = await this.$axios.post('xdropadmin/admin/set-all/default-messages', {
                    free: this.textarea.free.value,
                    regular: this.textarea.regular.value
                })
                this.snackbar.show = true
                this.snackbar.text = response.data.message
                this.button.loading = false
            }catch(e){
                console.log(e)
            }
        }
    },
    async created(){
        try{
            const response = await this.$axios.get('xdropadmin/admin/get-all/default/messages')
            
            this.textarea.regular.value = response.data.regular
            this.textarea.free.value = response.data.free
        }catch(e){
            console.log(e)
        }
    },
}
</script>

<style scoped>
.emoji-picker{
    position: absolute;
    z-index: 99;
}
</style>
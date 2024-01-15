<template>
    <PanelNavigation>

        <PanelMessageOverlayProgress :data="shillingProgress" />

        <PanelMessageStatistics :propData="shillingData" />
        
        <v-form @submit.prevent="mainShill" ref="form" v-model="formValid">

            <v-row class="mt-4" v-show="!botIsWorking">
            <v-col cols="12" md="4">
                <h4>Set the delay interval</h4>
                <br>
                <v-slider
                v-model="fields.interval.value"
                :thumb-size="60"
                thumb-label
                :step="fields.interval.step"
                ticks
                :min="fields.interval.min"
                :max="fields.interval.max"
                persistent-hint
                hint="Set the shilling delay interval.">
                    <template v-slot:thumb-label="{value}">
                        {{value}} min
                    </template>
                </v-slider>

                <v-row>
                    <v-col cols="12">
                        <span class="text-h5 blue--text">every {{fields.interval.value}} minutes</span>
                    </v-col>
                </v-row>
            </v-col>

            <v-col cols="12" md="8" style="position: relative;">
                
                <h4>Channels</h4>

                <v-textarea
                v-model="fields.channels"
                label="Telegram Channels"
                :rules="[v => !!v || 'Channels are required.']"
                auto-grow
                outlined
                rows="4"
                row-height="25"
                shaped
                placeholder="@channel@username"
                persistent-hint
                hint="Enter your Telegram channels in which you are a member only, in the following format: @channel@channel. Do not use any whitepaces and always add '@' between the channels."></v-textarea>
                
                <PanelGiftChannels />
                    
                <!-- <PanelChannelCard /> -->

            </v-col>
        </v-row>

        <v-row class="mt-5" v-show="!botIsWorking">
            <v-col cols="12">
                <h4>Message Area</h4>
                <br>
                <v-textarea
                v-model="fields.message"
                label="Shill Message"
                :rules="[v => !!v || 'Message are required.']"
                auto-grow
                outlined
                rows="10"
                row-height="25"
                shaped
                persistent-hint
                hint="Enter you shilling message."
                placeholder="Hey 😀

This placeholder has **bold**, `code`, __italics__ and
a [nice website](https://example.com)!

https://www.xdroppro.com"></v-textarea>
            </v-col>

            <v-col cols="12">
                <div class="emoji-container">
                    <v-btn @click="emoji.show = !emoji.show" color="primary" dark x-large icon elevation="3" outlined>
                        <v-icon>mdi-emoticon-cool-outline</v-icon>
                    </v-btn>
                    <VEmojiPicker v-if="emoji.show" @select="insertEmoji"  />
                </div>
            </v-col>
        </v-row>

        <v-row class="mt-10">
            <v-col cols="12">
                <v-btn
                type="submit"
                x-large
                color="success"
                :disabled="botIsWorking || !formValid"
                elevation="10">
                Start Shilling

                    <template v-slot v-if="botIsWorking">
                        <span>xdroppro working...</span>
                    </template>
                </v-btn>

                <v-btn
                v-if="botIsWorking"
                x-large
                color="red"
                elevation="10"
                dark
                @click="stopShill">
                    Stop Shilling
                </v-btn>

                <v-btn
                x-large
                color="info"
                elevation="10"
                :disabled="!formValid"
                v-if="!botIsWorking"
                @click="saveData">
                    save data
                </v-btn>

                <v-btn
                v-if="(fields.channels || fields.message) && !botIsWorking"
                x-large
                color="red"
                elevation="10"
                dark
                @click="resetFormData">
                    Reset Form
                </v-btn>
            </v-col>
        </v-row>
        </v-form>
    </PanelNavigation>
</template>

<script>
export default {
    middleware: ['auth', 'registered'],
    data(){
        return {
            fields: {
                interval: { 
                    value: this.retrieveDataObjectFromLocalStorage('shillSetup', 'interval'), 
                    min: 1, 
                    max: 60, 
                    step: 1 
                },
                message: this.retrieveDataObjectFromLocalStorage('shillSetup', 'message'),
                channels: this.retrieveDataObjectFromLocalStorage('shillSetup', 'channels'),
                successCounter: this.retrieveDataObjectFromLocalStorage('shillSetup', 'successCounter'),
                errorCounter: this.retrieveDataObjectFromLocalStorage('shillSetup', 'errorCounter')
            },
            defaultFormData: {
                interval: 5,
                message: '',
                channels: '',
                shillingData: {
                    timer: 0,
                    overall: {
                        sent: {
                            success: 0,
                            unsuccess: 0
                        }
                    },
                    shill: {
                        sent: {
                            success: [],
                            unsuccess: []
                        }
                    }
                }
            },
            emoji: {
                show: false
            },
            timeIntervalVariable: undefined,
            formValid: false,
            botIsWorking: false,
            shillingProgress: {
                status: false,
                title: 'XDropPro is warming up...',
                progress: 0,
                current: 0,
                total: 0,
                sent: {
                    success: 0,
                    unsuccess: 0
                }
            },
            shillingData: {
                timer: {
                    shilling: false,
                    stopped: true,
                    lapse: 0
                },
                overall: {
                    sent: {
                        success: this.retrieveShillingDataObjectFromLocalStorage('overallSentSuccess'),
                        unsuccess:  this.retrieveShillingDataObjectFromLocalStorage('overallSentUnsuccess')
                    }
                },
                shill: {
                    sent: {
                        success:  this.retrieveShillingDataObjectFromLocalStorage('shillSentSuccess'),
                        unsuccess:  this.retrieveShillingDataObjectFromLocalStorage('shillSentUnsuccess'),
                    }
                }
            },
        }
    },
    methods: {
        async mainShill(){

            console.log('Shilling...');
            this.shillingProgress.status = true
            this.botIsWorking = true
            const channels = this.returnChannelsStringAsArray(this.fields.channels)            
            this.shillingProgress.total = channels.length
            this.shillingData.shill.sent.success = []
            this.shillingData.shill.sent.unsuccess = []

            // set timer state
            this.shillingData.timer = {
                lapse: 0,
                shilling: true,
                stopped: false
            }

            let arrayCounter = 0;
            while(arrayCounter < channels.length){
                
                if (this.botIsWorking === false) break;
                const status = await this.mainRequestAndResponseErrorCapture({
                    channel: channels[arrayCounter],
                    message: this.fields.message
                })
                if (status === false) break;
                arrayCounter++ 
                this.shillingProgress.progress = Math.round(arrayCounter / channels.length * 100)
                               
            }
            
            this.shillingProgress = {
                status: false,
                title: 'Shilling in progress...',
                progress: 0,
                current: 0,
                total: 0,
                sent: {
                    success: 0,
                    unsuccess: 0
                }
            }

            // set timer state
            this.shillingData.timer = {
                lapse: this.fields.interval.value,
                shilling: false,
                stopped: false
            }

            if (this.botIsWorking === false) return
            let run;
            this.timeIntervalVariable = setTimeout(run = async () => {
                
                this.shillingProgress.status = true
                const channels = this.returnChannelsStringAsArray(this.fields.channels)            
                this.shillingProgress.total = channels.length
                this.shillingData.shill.sent.success = []
                this.shillingData.shill.sent.unsuccess = []

                // set timer state
                this.shillingData.timer = {
                    lapse: 0,
                    shilling: true,
                    stopped: false
                }

                let arrayCounter = 0;
                while(arrayCounter < channels.length){
                
                    if (this.botIsWorking === false) break;
                    const status = await this.mainRequestAndResponseErrorCapture({
                        channel: channels[arrayCounter],
                        message: this.fields.message
                    })
                    if (status === false) break;
                    arrayCounter++ 
                    this.shillingProgress.progress = Math.round(arrayCounter / channels.length * 100)
                               
                }

                this.shillingProgress.status = false
                this.shillingProgress = {
                    status: false,
                    title: 'Shilling in progress...',
                    progress: 0,
                    current: 0,
                    total: 0,
                    sent: {
                        success: 0,
                        unsuccess: 0
                    }
                }

                // set timer state
                this.shillingData.timer = {
                    lapse: this.fields.interval.value,
                    shilling: false,
                    stopped: false
                }

                setTimeout(run, (this.fields.interval.value) * 60000)

            }, (this.fields.interval.value) * 60000)

        },
        async mainRequestAndResponseErrorCapture(data){

            try{
                const res = await this.$axios.$post(this.$axios.defaults.baseURL + '/shill', {
                    channel: data.channel,
                    message: data.message,
                    id: this.retrieveDataObjectFromSessionStorage('TelegramCredentials', 'id'),
                    hash: this.retrieveDataObjectFromSessionStorage('TelegramCredentials', 'hash')
                })

                // console.log(res)

                if (res.success){
                    this.shillingProgress.sent.success++
                    this.shillingData.overall.sent.success++
                    (this.shillingData.shill.sent.success).push(res.data.message.channel)
                }else{
                    this.shillingProgress.sent.unsuccess++
                    this.shillingData.overall.sent.unsuccess++
                    (this.shillingData.shill.sent.unsuccess).push(res.data.message)
                }

                
                this.setShillSetupStatsToLocalStorage(res.success, this.shillingData.shill.sent)

            }catch(err){
                console.log(err)
                return false
            }

        },
        returnChannelsStringAsArray(string){
            return (string.split('@')).slice(1,string.split('@').length)
        },
        setShillSetupStatsToLocalStorage(success, shill){
            if (success) {
                localStorage.setItem('shillSetup', JSON.stringify({
                    ...JSON.parse(localStorage.getItem('shillSetup')),
                    shillingData: {
                        overall: {
                            sent: {
                                ...JSON.parse(localStorage.getItem('shillSetup')).shillingData.overall.sent,
                                success: this.shillingData.overall.sent.success
                            }
                        },
                        shill: {
                            sent: {
                                ...JSON.parse(localStorage.getItem('shillSetup')).shillingData.shill.sent,
                                success: shill.success
                            }
                        }                        
                    }
                }))
            }
            else {
                localStorage.setItem('shillSetup', JSON.stringify({
                    ...JSON.parse(localStorage.getItem('shillSetup')),
                    shillingData: {
                        ...JSON.parse(localStorage.getItem('shillSetup')).shillingData,
                        overall: {
                            sent: {
                                ...JSON.parse(localStorage.getItem('shillSetup')).shillingData.overall.sent,
                                unsuccess: this.shillingData.overall.sent.unsuccess
                            }
                        },
                        shill: {
                            sent: {
                                ...JSON.parse(localStorage.getItem('shillSetup')).shillingData.shill.sent,
                                unsuccess: shill.unsuccess
                            }
                        }                       
                    }
                }))
            }
        },
        stopShill(){
            if (this.timeIntervalVariable !== undefined) clearTimeout(this.timeIntervalVariable)
            this.shillingProgress = {
                status: false,
                progress: 0,
                current: 0,
                total: 0,
                sent: {
                    success: 0,
                    unsuccess: 0
                }
            }

            setTimeout(() => {
                // set timer state
                this.shillingData.timer = {
                    lapse: 0,
                    shilling: false,
                    stopped: true
                }
            }, 1000)
            
            this.botIsWorking = false
            console.log('Shilling stopped...');
        },
        saveData(){
            localStorage.setItem('shillSetup', JSON.stringify({
                interval: this.fields.interval.value,
                message: this.fields.message,
                channels: this.fields.channels,
                shillingData: this.shillingData
            }))
        },
        resetFormData(){
            const confirmed = confirm('Are you sure you want to clear the message data?')
            if (confirmed){
                localStorage.setItem('shillSetup', JSON.stringify(this.defaultFormData))
                this.fields.message = ''
                this.fields.channels = ''
                this.fields.interval.value = 5,
                this.fields.successCounter = 0,
                this.fields.errorCounter = 0
                
                console.log('Form data resetted...');
            }
        },
        insertEmoji(emoji){
            this.fields.message += emoji.data
        },
        retrieveShillingDataObjectFromLocalStorage(key){
            if (!localStorage.getItem('shillSetup')) return null

            switch (key){
                case 'overallSentSuccess':
                    return JSON.parse(localStorage.getItem('shillSetup')).shillingData.overall.sent.success
                case 'overallSentUnsuccess':
                    return JSON.parse(localStorage.getItem('shillSetup')).shillingData.overall.sent.unsuccess
                case 'shillSentSuccess':
                    return JSON.parse(localStorage.getItem('shillSetup')).shillingData.shill.sent.success
                case 'shillSentUnsuccess':
                    return JSON.parse(localStorage.getItem('shillSetup')).shillingData.shill.sent.unsuccess
            }
        },
        retrieveDataObjectFromLocalStorage(item, field){
            if (localStorage.getItem(item)) return JSON.parse(localStorage.getItem(item))[field] 
            switch (field){
                case 'interval':
                    return 5
                case 'successCounter':
                case 'errorCounter':
                    return 0
                default:
                    return ''              
            }
        },
        retrieveDataObjectFromSessionStorage(item, field){
            if (sessionStorage.getItem(item)) return JSON.parse(sessionStorage.getItem(item))[field]
        }
    },
    
    beforeCreate(){
        let shillSetup = localStorage.getItem('shillSetup')
        if (shillSetup === null || shillSetup === undefined) localStorage.setItem('shillSetup', JSON.stringify(
        {
            interval: 5,
            message: '',
            channels: '',
            shillingData: {
                overall: {
                    sent: {
                        success: 0,
                        unsuccess: 0
                    }
                },
                shill: {
                    sent: {
                        success: [],
                        unsuccess: []
                    }
                }
            }
        }))
    },
    created() {
        this.$nuxt.$on('gift-channels', (value) => {
            this.fields.channels += value
        })
    },
    watch: {
        '$store.state.theme.dark': function () {
            this.$vuetify.theme.isDark = this.$store.state.theme.dark
        }
    },
}
</script>

<style lang="scss" scoped>
    .emoji-container {
        position: relative;
        & .emoji-picker {
            position: absolute;
            bottom: 110%;
            left: 0%;
        }
    }

    .chat-alert-container, .general-alert-container {
        position: absolute;
        & * {
            z-index: 10;
        }
    }
    .chat-alert-container {
        right: 5px;
        top: 0;
    }
    .general-alert-container {
        left: 5px;
        bottom: 0;
    }
</style>
<template>
    <div>

        <v-item-group>

            <v-container>

                <v-row>

                    <v-col cols="12" sm="4">
                        
                        <v-item>
                            <v-card color="primary" dark raised>
                                <v-card-title>Status</v-card-title>
                                <v-card-text class="white--text text-h5">

                                    <div v-if="propData.timer.stopped">
                                        <span>Stopped...</span>
                                    </div>

                                    <div v-if="!propData.timer.shilling && !propData.timer.stopped">
                                        <vac ref="countdown" 
                                        :left-time="propData.timer.lapse * 60000" 
                                        :start-countdown="!propData.timer.shilling" 
                                        :stop-countdown="propData.timer.shilling || propData.timer.stopped">
                                            
                                            <span
                                            slot="process"
                                            slot-scope="{ timeObj }"
                                            class="success--text">{{ `Next Shill in: ${timeObj.m}:${timeObj.s}` }}</span>

                                            <span slot="finish">End!</span>

                                        </vac>
                                    </div>

                                    <div v-if="propData.timer.shilling">
                                        <span class="error--text">Shilling...</span>
                                    </div>

                                </v-card-text>
                            </v-card>
                        </v-item>

                        <br>

                        <v-item>
                            <v-card color="primary" dark raised>
                                <v-card-title>Overall</v-card-title>
                                <v-card-subtitle>Overall activity per user.</v-card-subtitle>

                                <v-card-text>
                                    <div class="white--text text-subtitle-1">
                                        <span>Sent & Received: {{propData.overall.sent.success}}</span>
                                        <br>
                                        <span>Sent but Not Received: {{propData.overall.sent.unsuccess}}</span>
                                    </div>
                                </v-card-text>
                            </v-card>
                        </v-item>
                        
                    </v-col>

                    <v-col cols="12" sm="8">
                        <v-item>
                            <v-card color="info" dark raised>
                                <v-card-title>Per Shill</v-card-title>
                                <v-card-subtitle>Overall activity per each shill.</v-card-subtitle>

                                <v-card-text>
                                    <div class="white--text text-subtitle-1">
                                        <span>Sent & Received: {{propData.shill.sent.success.length}}</span>
                                        <br>
                                        <span>Sent but Not Received: {{propData.shill.sent.unsuccess.length}}</span>
                                        
                                        <v-list rounded v-if="propData.shill.sent.unsuccess.length !== 0">
                                            <v-list-item-group color="error">

                                                <v-list-item v-for="(item, index) in propData.shill.sent.unsuccess" :key="index">
                                                    <span :class="item.type === 'slowmode' ? 'info--text' : 'error--text'">{{item.channel}} - {{item.reason}} - {{item.error}}</span>
                                                </v-list-item>

                                            </v-list-item-group>
                                        </v-list>

                                    </div>
                                </v-card-text>
                            </v-card>
                        </v-item>
                    </v-col>

                    <!-- <v-col
                    v-for="n in 3"
                    :key="n"
                    cols="12"
                    md="4"
                    >
                    <v-item v-slot="{ toggle }">
                        <v-card
                        class="d-flex align-center"
                        height="200"
                        @click="toggle">

                        <v-card-title>Overall</v-card-title>

                        <v-scroll-y-transition>
                            <div
                            v-if="active"
                            class="text-h2 flex-grow-1 text-center"
                            >
                            Active
                            </div>
                        </v-scroll-y-transition>

                        </v-card>
                    </v-item>
                    </v-col> -->

                </v-row>

            </v-container>

        </v-item-group>

    </div>
</template>

<script>
export default {
    props: {
        propData: Object
    },
    methods: {
        startCountdown () {
            this.$refs.countdown.startCountdown(true)
        }
    }
}
</script>
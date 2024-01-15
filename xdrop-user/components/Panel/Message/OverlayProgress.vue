<template>
    
    <v-overlay :value="data.status" zIndex="99" style="text-align: center;" opacity="0.9" dark>
        <v-tooltip left>

            <template v-slot:activator="{ on, attrs }">
                <v-icon 
                class="close" 
                size="60" 
                v-bind="attrs"
                v-on="on"
                @click="data.status = false">
                    mdi-close-outline
                </v-icon>
            </template>

            <span class="text-h6 text-sm-h5">Close progress window, will open on next shill!</span>

        </v-tooltip>

        <p class="text-h4 text-sm-h2 text-md-h1">{{ data.title }}</p>
        <br>
        <v-progress-circular
        :rotate="-90"
        :size="150"
        :width="20"
        :value="data.progress"
        dark
        :color="data.progress <= 35 ? 'white' : data.progress > 35 && data.progress <= 65 ? 'info' : 'success'">
            {{ data.progress }} %
        </v-progress-circular>
        <br><br>
        <p class="text-body-1 success--text">{{data.sent.success}} of {{data.total}} sent & received</p>
        <p class="text-body-1 error--text">{{data.sent.unsuccess}} of {{data.total}} sent but not received</p>
    </v-overlay>

</template>

<script>
export default {
    props: ['data']
}
</script>

<style lang="scss" scoped>
    .close {
        position: fixed;
        top: 20px;
        right: 20px;
    }
</style>
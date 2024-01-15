<template>

        <div class="main-ul-how-to">

            <HowToObtainApiId />
            <v-spacer class="py-5"></v-spacer>
            <HowToRegister />
            <v-spacer class="py-5"></v-spacer>
            <HowToDeregister />
            <v-spacer class="py-5"></v-spacer>
            <HowToSendMessage />
            <v-spacer class="py-5"></v-spacer>
            <HowToStyleMessage />
            <v-spacer class="py-5"></v-spacer>

        </div>

</template>

<script>
export default {
    watch: {
        '$store.state.theme.dark': function () {
            this.$vuetify.theme.isDark = this.$store.state.theme.dark
        }
    }
}
</script>

<style lang="scss">
    .main-ul-how-to{
        padding: 0!important;
        margin: 0!important;

        & .image {
            width: auto;
            max-width: 100%;
            height: auto;
        }
    }
</style>
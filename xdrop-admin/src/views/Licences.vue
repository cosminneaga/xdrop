<template>
    <div>
        <Navigation />

        <v-container fluid>
            <h1>XDrop Licences</h1>

            <Table />
        </v-container>

        <Footer />
    </div>
</template>

<script>
import Table from '@/components/dashboard/users/Table.vue'
import Navigation from '@/components/Navigation.vue'
import Footer from '@/components/Footer.vue'

export default {
    name: 'Licences',
    components: {
        Table, Navigation, Footer   
    }
}
</script>
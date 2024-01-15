<template>
  <v-row>
    <v-card
    class="mx-auto"
    width="100%"
    max-height="400px"
    style="display: flex!important; flex-direction: column;">

    <v-toolbar
      flat
      color="primary"
      dark>
      <v-toolbar-title>Select Channels</v-toolbar-title>
    </v-toolbar>

    <v-card-text style="flex-grow: 1; overflow: auto;">

      <v-chip-group
        v-model="amenities"
        column
        multiple>

        <v-chip filter outlined v-for="i in 100" :key="i">
          @Channel
        </v-chip>

      </v-chip-group>

    </v-card-text>

    
  </v-card>
  </v-row>
</template>

<script>
  export default {
    data: () => ({
      amenities: [1, 4],
    }),
  }
</script>
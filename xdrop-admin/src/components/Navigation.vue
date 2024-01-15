<template>
  <div>
    <v-app-bar
      color="indigo darken-1"
      dark
    >
      <v-app-bar-nav-icon v-on:click="drawerState = !drawerState"></v-app-bar-nav-icon>

      <v-toolbar-title>XDrop</v-toolbar-title>

      <v-spacer></v-spacer>

      <!-- <v-toolbar-items>
          <v-btn 
          v-for="link in links"
          :to="link.url"
          :key="link.id"
          text
          href="link.url"
          >{{link.text}}</v-btn>
          <v-divider vertical></v-divider>
      </v-toolbar-items> -->
          <v-divider vertical></v-divider>

      <v-chip 
      active 
      color="success" 
      dark 
      class="ml-3">
        {{licencesNumber}} issued licences
      </v-chip>

    </v-app-bar>

    
    

    <v-navigation-drawer
      class="indigo darken-1 py-4"
      dark
      v-model="drawerState"
      app
    >
        <!-- <p class="text-h2 pb-7 text-center pt-5">XDrop</p> -->
        <v-img
        contain 
        lazy-src="@/assets/logo.png"
        class="align-self-stretch mx-auto"
        max-height="100"
        max-width="140"
        src="@/assets/logo.png"></v-img>
        <p class="text-h6 text-center blue--text text--lighten-2">Admin Tools {{new Date().getFullYear()}}</p>
      <v-divider></v-divider>
      <v-list>
        <v-list-item
          v-for="link in links"
          :to="link.url"
          :key="link.id"
          link
          href="link.url"
        >
          <v-list-item-icon>
            <v-icon>{{ link.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>{{ link.text }}</v-list-item-title>
          </v-list-item-content>

        </v-list-item>
      </v-list>

      <template v-slot:append>
        <div class="pa-2">
          <v-btn block @click="logout">
            Logout
          </v-btn>
        </div>
      </template>
    </v-navigation-drawer>
    

  </div>
</template>

<script>
import {state} from '../store'


export default {
    name: 'Navigation',
    components: {},
    data(){
      return {
        // licences: state.licences,
        drawerState: false,
        licencesNumber: 0,
        links: [
            {
                text: 'Licences',
                url: '/licences',
                icon: 'mdi-key-chain'
            },{
                text: 'Generator',
                url: '/generator',
                icon: 'mdi-folder-plus'
            },{
              text: 'Messages',
              url: '/default-messages',
              icon: 'mdi-card-text'
            }
        ],
      }
    },
    methods: {
      logout(){
        sessionStorage.removeItem('logged')
        sessionStorage.removeItem('sessionKey')
        this.$router.push({path: '/'})
      }
    },
    async created(){
      try{
        const response = await this.$axios.get('xdropadmin/get-all/licences/number')
        this.licencesNumber = response.data.no
      }catch(e){
        console.log(e);
      }
    }
}
</script>
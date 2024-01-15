<template>
    <div>
        <v-navigation-drawer
        v-model="drawer"
        :mini-variant="miniVariant"
        :clipped="clipped"
        fixed
        color="info"
        app
        dark>

        <v-list>
          <a href="/how-to" target="_blank" rel="noopener noreferrer" style="color: #fff; text-decoration: none;">
            <v-list-item router>
              <v-list-item-action>
                <v-icon>mdi-help</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <!-- <v-list-item-title v-text="'How To'" /> -->
                How To
              </v-list-item-content>
            </v-list-item>
          </a>
          <!-- <v-list-item router exact to="/panel/how-to">
            <v-list-item-action>
              <v-icon>mdi-help</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title v-text="'How To'" />
            </v-list-item-content>
          </v-list-item> -->


          <v-list-item router exact to="/panel">
            <v-list-item-action>
              <v-icon>mdi-account</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title v-text="'Register'" />
            </v-list-item-content>
          </v-list-item>


          <v-list-item :key="messageLinkDisabled" :disabled="messageLinkDisabled" router exact to="/panel/message">
            <v-list-item-action>
              <v-icon>mdi-message-text</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title v-text="'Message'" />
            </v-list-item-content>
          </v-list-item>

        </v-list>

        <template v-slot:append>
        <div class="pa-2">
          <v-btn block color="red" @click="logout">
            Logout
          </v-btn>
        </div>
      </template>

      </v-navigation-drawer>

    <v-app-bar
      :clipped-left="clipped"
      color="info"
      app
      dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      
      <v-toolbar-title v-text="title" />

      <v-spacer />

      <!-- <v-chip 
      v-show="messagesCounter === 0 ? false : true"
      color="green"
      style="margin-right: 20px;">
      {{counter}}
      <v-avatar right>
        <v-icon>mdi-checkbox-marked-circle</v-icon>
      </v-avatar></v-chip> -->

      <v-switch
      hide-details
      inset
      dark
      :value="$store.state.theme.dark"
      @click="toggleTheme"
      color="purple">
        <template v-slot:label>
          <v-icon>{{$store.state.theme.dark ? 'mdi-weather-night' : 'mdi-white-balance-sunny'}}</v-icon>
        </template>
      </v-switch>

      <a href="/how-to" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">
        <v-icon size="30" style="margin-left: 20px;">mdi-help-box</v-icon>
      </a>

    </v-app-bar>

    <v-container>
        <slot></slot>
    </v-container>
</div>
</template>

<script>
export default {
  data () {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      // messageLinkDisabled: !this.$store.getters.getRegisteredStatus,
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'XDropPro',
      messagesCounter: this.retrieveDataObjectFromLocalStorage('shillSetup', 'counter')
    }
  },
  computed: {
    messageLinkDisabled(){
      return !this.$store.getters.getRegisteredStatus
    },
    counter(){
      return this.retrieveDataObjectFromLocalStorage('shillSetup', 'counter')
    }
  },
  methods: {
    async logout(){
      await this.$axios.$post(this.$axios.defaults.baseURL + '/logout')
      
      sessionStorage.removeItem('token')
      sessionStorage.removeItem('TelegramCredentials')
      sessionStorage.removeItem('registerFormState')
      this.$store.commit('setAuth', false)
      this.$router.go({
        path: '/login'
      })
    },
    toggleTheme (){
      this.$store.commit('togglePanelTheme')
    },
    retrieveDataObjectFromLocalStorage(item, field){
        if (localStorage.getItem(item)) return JSON.parse(localStorage.getItem(item))[field] 
        switch (field){
            case 'interval':
                return 5
            case 'counter':
                return 0
            default:
                return ''              
        }
    }
  }
}
</script>
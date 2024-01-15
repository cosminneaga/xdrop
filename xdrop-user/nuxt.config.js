import colors from 'vuetify/es5/util/colors'

export default {

  target: 'static',
  ssr: false,
  loading: false,

  head: {
    // titleTemplate: '%s - xdrop-user',
    title: 'XDropPro Automatic Shill Bot',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { hid: 'language', name: 'language', content: 'EN' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { name: 'format-detection', content: 'telephone=no' },
      { hid: 'Cache-Control', name: 'Cache-Control', content: 'no-cache' },

      // SEO
      { hid: 'description', name: 'description', content: 'XDropPro sends messages from your telegram account to unlimited telegram groups 24/7 automatically.' },
      { hid: 'summary', name: 'summary', content: 'XDropPro sends messages from your telegram account to unlimited telegram groups 24/7 automatically.' },
      { hid: 'author', name: 'author', content: 'xdropro.com' },
      { hid: 'Classification', name: 'Classification', content: 'Information Technology' },
      { hid: 'designer', name: 'designer', content: 'Cosmin Neaga' },
      { hid: 'url', name: 'url', content: 'xdroppro.com' },
      { hid: 'identifier-URL', name: 'identifier-URL', content: 'xdroppro.com' },
      { hid: 'coverage', name: 'coverage', content: 'Worldwide' },
      { hid: 'distribution', name: 'distribution', content: 'Global' },

      { hid: 'keywords', name: 'keywords', content: 'xdroppro, xdroppro.com, telegram, shill, bot, automatic, tool, message, automatic, chat, channels, 24/7, automatic shilling tool, telegram shill, telegram shill bot, telegram shill tool, shill bot, telegram shill 24/7 tool' },

      // and more to come... as OpenGraph Meta Tags https://gist.github.com/lancejpollard/1978404

      // FACEBOOK
      { hid: 'og:title', property: 'og:title', content: 'XDropPro Automatic Shill Bot' },
      { hid: 'og:type', property: 'og:type', content: 'shill' },
      { hid: 'og:url', property: 'og:url', content: 'xdroppro.com' },
      { hid: 'og:image', property: 'og:image', content: 'https://xdroppro.com/logo.png' },
      { hid: 'og:site_name', property: 'og:site_name', content: 'XDropPro' },
      { hid: 'og:description', property: 'og:description', content: 'XDropPro sends messages from your telegram account to unlimited telegram groups 24/7 automatically.' },

      // TWITTER
      { hid: 'twitter:title', name: 'twitter:title', content: 'XDropPro Automatic Shill Bot' },
      { hid: 'twitter:type', name: 'twitter:type', content: 'shill' },
      { hid: 'twitter:url', name: 'twitter:url', content: 'xdroppro.com' },
      { hid: 'twitter:image', name: 'twitter:image', content: 'https://xdroppro.com/logo.png' },
      { hid: 'twitter:site_name', name: 'twitter:site_name', content: 'XDropPro' },
      { hid: 'twitter:description', name: 'twitter:description', content: 'XDropPro sends messages from your telegram account to unlimited telegram groups 24/7 automatically.' },

      // APPLE TAGS
      { hid: 'apple-mobile-web-app-capable', name: 'apple-mobile-web-app-capable', content: 'yes' },
      // { hid: 'apple-touch-fullscreen', name: 'apple-touch-fullscreen', content: 'yes' },
      { hid: 'apple-mobile-web-app-status-bar-style', name: 'apple-mobile-web-app-status-bar-style', content: 'black' },
      // { name: 'viewport', content: 'width = 320, initial-scale = 2.3, user-scalable = no' },

      // INTERNET EXPLORER TAGS
      { hid: 'Page-Enter', name: 'Page-Enter', content: 'RevealTrans(Duration=2.0,Transition=2)' },
      { hid: 'Page-Exit', name: 'Page-Exit', content: 'RevealTrans(Duration=3.0,Transition=12)' },
      { hid: 'application-name', name: 'application-name', content: 'XDropPro' },

      // { hid: '', name: '', content: '' },
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: 'logo.ico' }
    ]
  },
  css: [
    '@/assets/global.scss'
  ],
  plugins: [
    '~/plugins/Main.client.js',
    '~/plugins/axios.js',
  ],
  components: true,
  buildModules: [
    '@nuxtjs/vuetify'
  ],
  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/dotenv',
    '@nuxtjs/google-gtag',
    'nuxt-compress'
  ],
  'google-gtag': {
    id: 'G-KNCW7FRVGS',
    config: {
      send_page_view: true,
      linker: {
        domains: ['xdroppro.com']
      }
    },
    debug: true,
    disableAutoPageTrack: false
  },
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: false,
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3
        }
      }
    }
  },

  build: {
  },
  server: {
    host: '192.168.0.15',
    port: '3000'
  }
}

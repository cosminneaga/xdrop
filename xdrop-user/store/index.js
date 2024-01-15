export const state = () => ({
    theme: {
        dark: false,
    },
    registered: sessionStorage.getItem('TelegramCredentials') ? true : false,
    auth: sessionStorage.getItem('token') ? sessionStorage.getItem('token') : false
})

export const mutations = {
    togglePanelTheme(state) {
        state.theme.dark = !state.theme.dark
    },
    setRegisteredStatus(state, value) {
        state.registered = value
    },
    setAuth(state, value) {
        state.auth = value
    }
}

export const getters = {
    getRegisteredStatus: state => state.registered,
    getAuth: state => state.auth
}
import Vue from 'vue'

export const state = Vue.observable({
    licences: 0,
    isAuthenticated: false
})
export const mutations = {
    setLicences(newValue) {
        state.licences = newValue
    },
    login() {
        state.isAuthenticated = true
        console.log('user authenticated');
    },
    logout() {
        state.isAuthenticated = false
        console.log('logged out');
    }
}

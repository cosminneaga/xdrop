export default function ({ $axios, redirect, store }) {
    $axios.onRequest(() => {
        $axios.defaults.headers.common = {
            Authorization: `Bearer ${store.getters.getAuth}`
        }
    })

    $axios.onError(error => {
        const code = parseInt(error.response && error.response.status)
        if (code === 400) {
            // redirect('/400')
            return alert('You are offline.')
        }
    })

    let mainUrl
    if (process.env.ENV === 'prod'){
        mainUrl = process.env.REQUEST_URL_PROD
    }else if (process.env.ENV === 'dev'){
        mainUrl = process.env.REQUEST_URL_DEV
    }else if (process.env.ENV === 'local'){
        mainUrl = process.env.REQUEST_URL_LOCAL
    }

    $axios.setBaseURL(mainUrl)
}
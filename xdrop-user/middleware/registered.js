export default function ({ store, redirect }) {
    // If the user is not registered with telegram credentials
    if (!store.state.registered) {
        return redirect('/panel')
    }
}
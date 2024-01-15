<template>
    <div id="obtain-api_id">

        <v-sheet elevation="5" class="pa-8" shaped>
            
            <p class="text-h5 font-weight-black">### How to obtain your api_id ###</p>

            <ol>
                <li class="font-weight-black">Go to <a href="https://my.telegram.org/" target="_blank" rel="noopener noreferrer">my.telegram.org</a> and enter your updated phone number and the confirmation code you have received on your Telegram chat.</li>
                <v-container>
                  <img class="image" src="~/assets/how-to/images/obtain-id/enter-code.png" alt="">
                </v-container>

                <li class="font-weight-black">Select first option as '<span class="blue--text">API development tools</span>'.</li>
                <v-container>
                  <img class="image" src="~/assets/how-to/images/obtain-id/select-api-tools.png" alt="">
                </v-container>

                <li class="font-weight-black">Enter details about your Telegram application.</li>
                <v-spacer class="mt-4"></v-spacer>
                <ol>
                    <li><strong class="blue--text">App title: </strong>enter your prefered app title</li>
                    <li><strong class="blue--text">Short name: </strong>enter a short name of your app</li>
                    <li><strong class="blue--text">URL: </strong>can be left empty</li>
                    <li><strong class="blue--text">PLATFORM: </strong>choose '<strong>Web</strong>'</li>
                    <li><strong class="blue--text">Description: </strong>can be left empty</li>
                </ol>
                <v-container>
                  <img class="image" src="~/assets/how-to/images/obtain-id/create-new-application.png" alt="">
                </v-container>

                <li class="font-weight-black">After the steps above are done you should get a screen where your <span class="blue--text">api_id</span> and <span class="blue--text">api_hash</span> are visible.</li>
                <v-container>
                  <img class="image" src="~/assets/how-to/images/obtain-id/api_id.png" alt="">
                </v-container>

                <li class="font-weight-black">In case you already have an application created all you have to do is the following:</li>
                <v-spacer class="mt-4"></v-spacer>
                <ol>
                    <li>Log in to your Telegram core: <a href="https://my.telegram.org" target="_blank" rel="noopener noreferrer">https://my.telegram.  org</a>.</li>
                    <li>Go to '<a href="https://my.telegram.org/apps" target="_blank" rel="noopener noreferrer">API development tools</a>'.</li>
                    <li>You will get basic addresses as well as the api_id and api_hash parameters required for user authorization.</li>
                    <li>For the moment each number can only have one api_id connected to it.</li>
                </ol>
            </ol>
            
        </v-sheet>
    </div>
</template>
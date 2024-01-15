<template>
    <div id="send-message">

        <v-sheet elevation="5" class="pa-8" shaped>

            
            <p class="text-h5 font-weight-black">### How to send a message ###</p>

            <v-alert
            border="left"
            colored-border
            type="warning"
            elevation="10">
                In order to send messages to Telegram users/channels/groups it is required for you Telegram App to be successfully registered to XDropPro tool, otherwise you will not be able to access the messages page.
            </v-alert>
            <v-spacer class="py-3"></v-spacer>

            <ul>
                <li class="font-weight-black">
                    Set the time interval by sliding right to left and viceversa the interval slider.
                </li>
                <v-container>
                    <img class="image" src="~/assets/how-to/images/message/interval.png" alt="">
                </v-container>

                <li class="font-weight-black">
                    Enter the required channels in same format as following: @username@username2 without any whitespaces.
                </li>
                <v-container>
                    <img class="image" src="~/assets/how-to/images/message/channels.png" alt="">
                    <v-alert
                    border="left"
                    colored-border
                    type="warning"
                    elevation="10">
                        Please make sure the channels you will be entering in the channels field are channels your are member of otherwise your shilling will be stopped.
                    </v-alert>
                </v-container>

                <li class="font-weight-black">
                    Type your desired message.
                </li>
                <v-container>
                    <img class="image" src="~/assets/how-to/images/message/message.png" alt="">
                </v-container>

                <li class="font-weight-black">
                    Once you have added your desired channels and message you will be able to start sending message, you can do that by clicking <span class="green--text">START SHILLING</span> button.
                </li>
                <v-container>
                    <img class="image" src="~/assets/how-to/images/message/shill.png" alt="">
                    <v-alert
                    border="left"
                    colored-border
                    type="warning"
                    elevation="10">
                        <span class="red--text">RESET FORM</span> button will reset the form fields to default values.
                    </v-alert>
                </v-container>

                <li class="font-weight-black">
                    While the tool is shilling you will see these two sections becoming reactive in relation to the shilling loading process.
                </li>
                <v-container>
                    <img class="image" src="~/assets/how-to/images/message/shilling-interval.png" alt="">
                    <img class="image" src="~/assets/how-to/images/message/shilling-button.png" alt="">
                    <v-alert
                    border="left"
                    colored-border
                    type="warning"
                    elevation="10">
                        <span class="red--text">STOP SHILLING</span> button will stop the shilling loop.
                    </v-alert>
                </v-container>
            </ul>
            
        </v-sheet>
    </div>
</template>
<template>
<div id="register">
    

    <v-sheet elevation="5" class="pa-8" shaped>

        <p class="text-h5 font-weight-black">### How to register your Telegram App to XDropPro ###</p>

        <v-alert
        border="left"
        colored-border
        type="warning"
        elevation="10">
            In order to complete the steps in this section it is imperative to have access to your api_id and api_hash, if you don't know where to get these please follow the steps in the 'How to obtain your api_id' section.
        </v-alert>

        <v-spacer class="py-3"></v-spacer>
        <ul>
            <li class="font-weight-black">Enter api_id, api_hash, and your phone number</li>
            <v-container>
                <v-alert
                type="info"
                dark
                border="left"
                dense
                width="fit-content">
                Make sure you'll use an updated phone number in relation with your Telegram account
                </v-alert>

                <img class="image" src="~/assets/how-to/images/register/one.png" alt="">

                <v-alert
                border="left"
                colored-border
                type="warning"
                elevation="10">
                    If any of these fields are entered wrong data you will be prompted with accordingly errors, if this becomes persistent for unknown reasons please contact us on our Telegram group.
                </v-alert>
            </v-container>

            <li class="font-weight-black">Enter the code received to your Telegram chat and click <span class="blue--text">REGISTER</span> button.</li>
            <v-container>
                <img class="image" src="~/assets/how-to/images/register/two.png" alt="">

                <v-alert
                border="left"
                colored-border
                type="warning"
                elevation="10">
                    If you have entered your code wrong for the first time or you have waited for too long before entering the code and clicking the <span class="blue--text">REGISTER</span> button, you will need to click <span class="red--text">RESET</span> button and then click again <span class="green--text">GET REQUEST CODE</span> button to get another code.
                </v-alert>
            </v-container>
            

            <li class="font-weight-black">You should be registered after the second step, however in case you have two-steps authentication activated on your Telegram account you will be prompted with another field where you will need to enter your password. After the password has been entered click <span class="blue--text font-weight-regular">REGISTER WITH PASSWORD</span> button to completed registration.</li>
            <v-container>
                <img class="image" src="~/assets/how-to/images/register/three.png" alt="">

                <v-alert
                border="left"
                colored-border
                type="warning"
                elevation="10">
                    If you have entered your password wrong, you will need to click the <span class="red--text">RESET</span> button in order to receive another code again, and after the code step please make sure you will enter the password correctly.
                </v-alert>
            </v-container>

            <li class="font-weight-black">After all steps are completed the completed form should look as it does in the picture below.</li>
            <v-container>
                <img class="image" src="~/assets/how-to/images/register/completed.png" alt="">
            </v-container>
        </ul>
    </v-sheet>
</div>
</template>
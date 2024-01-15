<template>
    <!-- ***** Features Big Item Start ***** -->
    <section class="section" id="setup">
        <div class="container">
            <div class="row">
                <div class="left-image col-lg-5 col-md-12 col-sm-12 mobile-bottom-fix-big"
                    data-scroll-reveal="enter left move 30px over 0.6s after 0.4s" style="display: flex; justify-content: center;">
                    
                    <img src="~/assets/landing/images/webp/logo.webp" alt="Logo" style="margin:auto; width: 95%; height: auto;">
                    
                </div>
                <div class="right-text offset-lg-1 col-lg-6 col-md-12 col-sm-12 mobile-bottom-fix">
                    <h3 class="font-weight-bold">Quick and easy steps to shill with XDropPro</h3>
                    <br>
                    <ul>
                        <li data-scroll-reveal="enter right move 30px over 0.6s after 0.4s">
                            <!-- <img src="landing/images/about-icon-01.png" alt=""> -->
                            <div class="text">
                                <h4>1. Register With Your Existing Telegram Account</h4>
                                <p>You don’t need to create a new account. You can use any existing telegram account. Simply go to Telegram's  <a href="https://my.telegram.org/" target="_blank" rel="noopener noreferrer">application page</a> and grab api_id and api_hash to register these with XDropPro.</p>
                            </div>
                        </li>
                        <li data-scroll-reveal="enter right move 30px over 0.6s after 0.6s">
                            <!-- <img src="landing/images/about-icon-03.png" alt=""> -->
                            <div class="text">
                                <h4>3. Set The Time Interval (minutes)</h4>
                                <p>XDropPro has different options for different needs, so YOU want to send it every x minutes? You decide the frequency. (carefull at group rules).</p>
                            </div>
                        </li>
                        <li data-scroll-reveal="enter right move 30px over 0.6s after 0.6s">
                            <!-- <img src="landing/images/about-icon-03.png" alt=""> -->
                            <div class="text">
                                <h4>4. Customize The Message</h4>
                                <p>Aside from text, XDropPro supports Emoji too. As long as you can send the message manually on Telegram, XDropPro can automate it for you. We are continuously working to add new features so Gifs, Photo and video are coming soon.</p>
                            </div>
                        </li>
                        <li data-scroll-reveal="enter right move 30px over 0.6s after 0.6s">
                            <!-- <img src="landing/images/about-icon-03.png" alt=""> -->
                            <div class="text">
                                <h4>5. Hit the SEND button</h4>
                                <p>Once you finish these steps, XDropPro will send your messages to your selected groups 24/7 non stop, until you decide to stop it.</p>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
    <!-- ***** Features Big Item End ***** -->
</template>

<style lang="scss" scoped>
.section{
    & ul {
        margin: 0;
        padding: 0;
        & li{
            display: flex;
            flex-direction: row;
            align-items: flex-start;
            gap: 10px;
            margin: 30px 0;
        }
    }
}    
</style>
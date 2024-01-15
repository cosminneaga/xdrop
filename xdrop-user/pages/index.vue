<template>
  <div class="main-app-wrapper">


    <!-- ***** Preloader Start ***** -->
    <!-- <div id="preloader">
        <div class="jumper">
            <div></div>
            <div></div>
            <div></div>
        </div>
    </div> -->
    <!-- ***** Preloader End ***** -->


    <LandingHeader />

    <LandingWelcome />

    <div class="left-image-decor"></div>

    <LandingPricing />
    
    <div class="right-image-decor"></div>

    <LandingSetup />

    <LandingFooter />

    


  </div>
</template>



<style lang="scss">
  @import '~/assets/landing/css/bootstrap.min.css';
  @import '~/assets/landing/css/templatemo-lava.css';
  .main-app-wrapper {
    & section {
    margin-top: 50px;
  }
}
</style>

<template>
    <!-- ***** Header Area Start ***** -->
    <header class="header-area header-sticky">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <nav class="main-nav">
                        <!-- ***** Logo Start ***** -->
                        <NuxtLink to="/" class="logo">
                           {{envState === 'dev' ? 'dev -' : envState === 'local' ? 'local -' : ''}} XdropPro
                        </NuxtLink>
                        <!-- ***** Logo End ***** -->
                        <!-- ***** Menu Start ***** -->
                        <ul 
                        ref="nav" 
                        class="nav"
                        :style="{display: mobile.nav ? 'block' : 'none'}">
                            <li class="scroll-to-section"><NuxtLink to="#welcome" class="menu-item">Home</NuxtLink></li>
                            <li class="scroll-to-section"><NuxtLink to="#pricing" class="menu-item">Pricing</NuxtLink></li>
                            <li class="scroll-to-section"><NuxtLink to="#setup" class="menu-item">Setup</NuxtLink></li>
                            <li class="scroll-to-section"><NuxtLink to="/login" class="menu-item">Login</NuxtLink></li>
                            <li class="scroll-to-section"><NuxtLink to="/how-to" class="menu-item">How To</NuxtLink></li>

                            <!-- <li class="submenu">
                                <a href="javascript:;">Drop Down</a>
                                <ul>
                                    <li><a href="" class="menu-item">About Us</a></li>
                                    <li><a href="" class="menu-item">Features</a></li>
                                    <li><a href="" class="menu-item">FAQ's</a></li>
                                    <li><a href="" class="menu-item">Blog</a></li>
                                </ul>
                            </li> -->

                        </ul>
                        <button 
                        ref="menu" 
                        :class="mobile.menu ? 'menu-trigger active' : 'menu-trigger'" 
                        @click="toggleMobileNav"
                        style='outline: 0;'>
                            <span>Menu</span>
                        </button>
                        <!-- ***** Menu End ***** -->
                    </nav>
                </div>
            </div>
        </div>
    </header>
    <!-- ***** Header Area End ***** -->
</template>

<script>
export default {
    data(){
        return{
            mobile: {
                nav: false,
                menu: false
            },
            envState: 'prod'
        }
    },
    methods: {
        toggleMobileNav(){
            this.mobile.nav = !this.mobile.nav
            this.mobile.menu = !this.mobile.menu
        }
    },
    created(){
        this.envState = process.env.ENV
    }
}
</script>

<style lang="scss" scoped>
    .main-nav{
        box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;   
        padding: 0 15px;
        & .logo {
            text-align: left!important;
        }
        & ul.nav {
            background: orange;
            display: block;
            & a {
                color: #fff;
            }
        }
    }
</style>
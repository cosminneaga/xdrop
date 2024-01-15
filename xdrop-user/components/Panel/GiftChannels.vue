<template>
  <v-row justify="start">
    <v-dialog
      v-model="dialog"
      max-width="600"
      hide-overlay>

      <template v-slot:activator="{ on, attrs }">

        <v-scroll-x-transition>
            <v-btn
            class="mt-3"
            color="primary"
            elevation="5"
            large
            v-show="button"
            v-on="on"
            v-bind="attrs">
                
                Gift Channels
                &nbsp;<v-icon>mdi-gift-outline</v-icon>

            </v-btn>
        </v-scroll-x-transition>

      </template>
      <v-card tile>
        <v-card-title class="text-h6 text-sm-h5">
          A shilling gift from us.
        </v-card-title>
        
        <v-card-text>
            BSC NEW SHILLING LIST -- NO BAN -- Everything is FREE
            <v-spacer class="py-2"></v-spacer>
            <v-textarea
            v-model="giftChannels"
            label="Gift Channels"
            auto-grow
            outlined
            rows="10"
            row-height="25"
            shaped></v-textarea>

            <v-btn
            color="green darken-1"
            text
            @click="emitGiftChannels">
            Copy Channels
            </v-btn>     

            
          <v-alert
            border="left"
            colored-border
            type="warning"
            elevation="2">
            Please be aware about the fact that you will need to be a member of these channels in order to shill into these.
            </v-alert>       

        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="red darken-1"
            text
            @click="dialog = false">
            Close
          </v-btn>
          
        </v-card-actions>

        
        
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
  export default {
    data () {
      return {
        dialog: false,
        button: false,
        giftChannels: '@BSC_Shilll_USA@BSC_Shilll_CANADA@BSC_Shilll_RUSSIA@BSC_Shilll_CHINA@BSC_Shilll_JAPAN@BSC_Shilll_AUSTRALIA@BSC_Shill_New_ZEALAND@BSC_Shill_ARGENTINA@BSC_Shilll_BRAZIL@BSC_Shill_MEXICO@BSC_Shilll_CUBA@BSC_Shill_SOUTHKOREA@BSC_Shill_SCOTLAND@BSC_Shill_INDONESIA@BSC_Shilll_INDIA@BSC_Shill_PAKISTAN@BSC_Shill_NIGERIA@BSC_Shill_IRANIAN@CryptoGermanyy@CryptoSwitzerlandd@CryptoSpainn@CryptoUnitedK@CryptoSweden@CryptoNorwayy@CryptoFrancee@CryptoItalyy@CryptoAustriaa@CryptoFinlandd@CryptoNetherlandss@CryptoIrelandd@CryptoIcelandd@CryptoBelgiumm@CryptoPortugall@CryptoDenmarkk@CryptoHungaryy@CryptooSanMarino@CryptoSerbiaa@CryptoTurkeyy@CryptoMacedoniaa@CryptoUkrainee@CryptoBosnia@CryptoGreecee@CryptoPolandd@CryptooRomania@CryptooMoldova@CryptooCzech@CryptooBelarus@CryptooMonaco@CryptooSlovenia@CryptooSlovakia@CryptooMalta@CryptooLithuania@CryptooMontenegro@CryptooEstonia@CryptooBulgaria@CryptooCroatia@CryptooAndorra@CryptooAlbania@CryptooLatvia@CryptooLiechtenstein@Cryptohardshill@PowerShill@LightShill@TheShillRoom@ShillUp@OutShill@LegacyShill@AestheticShill@OpenShilling@InfiniteShill@MetaShill'
      }
    },
    mounted(){
        setTimeout(() => {
            this.button = true
        }, 1000)
    },
    methods: {
        emitGiftChannels(){
            $nuxt.$emit('gift-channels', this.giftChannels)
            this.dialog = false
        }
    }
  }
</script>
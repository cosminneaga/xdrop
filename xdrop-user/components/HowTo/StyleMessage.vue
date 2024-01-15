<template>
    <v-container id="style-message">
        
        <v-sheet elevation="5" class="pa-8" shaped>

          <p class="text-h5 font-weight-black">### How to style your message. ###</p>

          <p>XDropPro uses <a href="https://en.wikipedia.org/wiki/Markdown" target="_blank" rel="noopener noreferrer">markdown</a> to format your messages, thus you will be able to apply some of the markdown methods to your text message.</p>
            
            <ul>
                <li>Make a <span class="blue--text text-decoration-underline">link</span> text</li>
                <v-container>
                  <code>
                    [My favourite shilling tool](https://xdroppro.com)
                  </code>
                </v-container>

                <li>Make a <span class="font-weight-bold">bold</span> text</li>
                <v-container>
                  <code>
                      **your text**
                  </code>
                </v-container>

                <li>Make an <span class="font-italic">italic</span> text.</li>
                <v-container>
                  <code>
                      __your text__
                  </code>
                </v-container>

                <li>Make an <code>code</code> section.</li>
                <v-container>
                  <code>
                      `your text`
                  </code>
                </v-container>
            </ul>

        </v-sheet>

    </v-container>
</template>
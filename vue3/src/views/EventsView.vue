<script setup>
import { ref } from 'vue'
let contador_doble_click = ref(0)
let contador_click = ref(0)
let mouse = ref(true)
let mensaje = ref("")
</script>

<template>
    <v-container>
        <h2> Eventos con botones</h2>
        <v-row>
            <v-col cols="4">
                <v-btn variant="tonal" color="primary" @click="contador_click++">
                    Click ({{ contador_click }})
                </v-btn>
            </v-col>
            <v-col cols="4">
                <v-btn variant="tonal" color="success" @dblclick="contador_doble_click++">
                    Doble click ({{ contador_doble_click }})
                </v-btn>
            </v-col>
            <v-col cols="4">
                <v-btn variant="tonal" :color="mouse ? 'yellow-darken-1' : 'deep-purple-lighten-1'"
                    @mouseover="mouse = true" @mouseleave="mouse = false">

                    Pasa el mouse por aqui! {{ mouse }}
                </v-btn>
            </v-col>

            <h2> Eventos de teclado</h2>

        </v-row>
        <v-row>
            <v-col cols="4">
                <v-text-field v-model="mensaje" label="Guarda al escribir:">

                </v-text-field>
            </v-col>
            <v-col cols="4">
                <v-text-field label="Guarda al presionar enter" @keyup.enter="mensaje = $event.target.value"
                    @keyup.esc="mensaje = ''" />
            </v-col>
            <v-col cols="4">
                <v-text-field v-model="mensaje" label="Guarda al escribir y esc para limpiar"
                    @keyup.esc="mensaje = ''" />
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="4"> Texto escrito {{ mensaje }} </v-col>
        </v-row>
    </v-container>
</template>

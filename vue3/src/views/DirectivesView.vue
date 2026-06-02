<script setup>
import { ref } from 'vue'
let nombre = ref('')
let aceptaTerminos = ref(true)
let color = ref("#f5fe4e")
let habilitado = ref(false)

let usuarios = ref([
    { id: 1, nombre: "Ana", habilitada: true },
    { id: 2, nombre: "Luis", habilitada: true },
    { id: 3, nombre: "Juana", habilitada: false }
])
const cambiarTerminos = () => aceptaTerminos.value = !aceptaTerminos.value
</script>

<template>
    <h1> Directivas</h1>
    <div>
        <input v-model="nombre">
        <p> El usuario esta escribiendo {{ nombre }}</p>

        <input type="checkbox" v-model="aceptaTerminos"> Acepta los términos y condiciones?</input>
        <p> ¿Aceptó los términos? {{ aceptaTerminos ? "Si" : "No" }}</p>

        <v-btn variant="tonal" color="#f5fe4e" @click="cambiarTerminos">
            {{ aceptaTerminos ? "Desactivar" : "Activar" }}</v-btn>
        <br>
        <v-btn variant="tonal" v-bind:color="color" @click="cambiarTerminos">
            {{ aceptaTerminos ? "Desactivar" : "Activar" }}</v-btn>
        <br>
        <v-btn variant="tonal" :color="color" @click="cambiarTerminos">
            {{ aceptaTerminos ? "Desactivar" : "Activar" }}</v-btn>
        <br>
        <v-btn :disabled="habilitado"> Botón</v-btn>

        <div v-if="habilitado">
            Esta inactivo
        </div>
        <div v-else>
            Esta activo
        </div>

        <div v-show="habilitado">
            Esta inactivo
        </div>
        <div v-show="!habilitado">
            Esta activo
        </div>
    </div>

    <div>
        <ul>
            <li v-for="usuario in usuarios" :key="usuario.id">
                {{ usuario.nombre }} </li>
        </ul>

    </div>
    <v-row>
        <v-col cols="4" v-for="usuario in usuarios" :key="usuario.id">
            <div v-if="usuario.habilitada">{{ usuario.nombre }} </div>
        </v-col>
    </v-row>
    <br> <br> <br> <br> <br> <br>

    <div class="mt-4 mx-3 mb-16" style="margin-bottom: 80vh;">
        <h3>Ejercicio: Lista de tareas </h3>
        Crear una vista donde el usuario pueda ingresar una tarea y la agregue a una lista mediante un botón.
        Las tareas deben desplegarse como una lista y si no hay tareas ingresadas debe mostrarse un mensaje de error.
        Utiliza v-text-fild y v-list, junto con v-for y v-if

    </div>


</template>
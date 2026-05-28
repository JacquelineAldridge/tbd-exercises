<script setup>
import { ref } from 'vue'

let nombreAsignatura = ref("Taller de Base de datos")
const num1 = 5
const num2 = 4
const activo = true

let contador = ref(0)

// Funciones normales
// function sumar() {
//   contador.value++
// }

// function restar() {
//   contador.value--
// }
console.log(nombreAsignatura)

// Arrow functions
const sumar = () => contador.value++
const restar = () => contador.value--

function cambiarDeAsignatura() {
  console.log(nombreAsignatura.value)
  nombreAsignatura.value = "Base de datos"
  console.log(nombreAsignatura.value)
}

</script>

<template>
  <main>
    <h1> HOLA </h1>

    <div> Bienvenidos a la asignatura de {{ nombreAsignatura }} </div>
    <div> Bienvenidos a la asignatura de {{ nombreAsignatura.toLowerCase() }} </div>

    <p> La multiplicación de {{ num1 }} y {{ num2 }} es {{ num1 * num2 }}</p>
    <p> {{ nombreAsignatura == "Taller de base de datos" }}</p>

    El usuario {{ activo ? "SI" : "NO" }} se encuentra activo

    <!-- {{ cambiarDeAsignatura() }} -->
    <br>
    <button @click="cambiarDeAsignatura()">
      Cambiar asignatura a base de datos
    </button>
    <br>

    <button @click="nombreAsignatura = 'Compiladores'">
      Cambiar asignatura a compiladores
    </button>
    <br>

    <v-btn> Botón por defecto</v-btn>
    <br>
    <v-btn variant="outlined"> Botón outlined </v-btn> <br>
    <p> TONAL</p>
    <v-btn variant="tonal" color="#f5f34e"> Botón tonal #f5f34e </v-btn> <br>
    <v-btn variant="tonal" color="primary"> Botón tonal primary </v-btn> <br>
    <v-btn variant="tonal" color="success"> Botón tonal success</v-btn> <br>
    <v-btn variant="tonal" color="warning"> Botón tonal warning </v-btn> <br>
    <v-btn variant="tonal" color="error"> Botón tonal error </v-btn> <br>
    <v-btn variant="tonal" color="secondary"> Botón tonal secondary </v-btn> <br>
    <p> OUTLINED</p>
    <v-btn variant="outlined" color="info"> Botón outlined info </v-btn> <br>
    <v-btn variant="outlined" color="primary"> Botón outlined primary </v-btn> <br>

    <v-btn variant="outlined" color="teal-lighten-3"> Botón outlined teal-lighten-3 </v-btn> <br>
    <v-btn variant="outlined" color="teal-lighten-1"> Botón outlined teal-lighten-1 </v-btn> <br>
    <v-btn variant="outlined" color="teal-darken-1"> Botón outlined teal-darken-1 </v-btn> <br>

    <p> Botones deshabilitados</p>
    <v-btn variant="outlined" color="teal-darken-1" disabled> Botón outlined teal-darken-1 deshabilitados</v-btn> <br>
    <v-btn variant="tonal" color="primary" disabled> Botón tonal primary </v-btn> <br>

    <p> Tamaños de botones</p>
    <v-btn variant="outlined" color="teal-darken-1" size="small"> Botón outlined teal-darken-1 </v-btn> <br>
    <v-btn variant="tonal" color="primary" size="x-large"> Botón tonal primary </v-btn> <br>

    <p>Densidad</p>
    <v-btn variant="outlined" color="teal-darken-1" density="compact"> Botón outlined teal-darken-1 </v-btn> <br>
    <v-btn variant="outlined" color="teal-darken-1" density="comfortable"> Botón outlined teal-darken-1 </v-btn> <br>

    <p>Botón con evento</p>
    <v-btn variant="outlined" @click="cambiarDeAsignatura"> Botón con evento </v-btn> <br>

  </main>

  <!--  Actividad
  Implementen un contador: Mostrar un número en pantalla que empiece en 0,
  y dos botones: uno que sume 1 y otro que reste 1.
  Usar `ref` para el contador y `@click` para los botones.
  functions o arrows functions o poniendo la logica en el evento 
  -->
  <!-- <div> Actividad contador</div>
  <h3> {{ contador }}</h3>
  <v-btn color="success" @click="sumar" class="mx-5"> Sumar </v-btn>
  <v-btn color="warning" @click="restar" class="pa-10"> Restar </v-btn> -->

  <div> Actividad contador</div>
  <h3> {{ contador }}</h3>
  <v-btn color="success" @click="sumar" class="mx-5"> Sumar </v-btn>
  <v-btn color="warning" @click="restar" class="pa-10"> Restar </v-btn>
  <div>
    <v-btn color="success" @click="contador++" class="mx-5"> Sumar </v-btn>
    <v-btn color="warning" @click="contador--" class="pa-10"> Restar </v-btn>
  </div>
</template>

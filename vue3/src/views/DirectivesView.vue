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
let tarea = ref('')
let tareas = ref([])
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

    <v-container>
        <div class=" mt-4 mx-3 mb-16" style="margin-bottom: 80vh;">
            <h3>Ejercicio: Lista de tareas </h3>
            <p>
                Implemente una funcionalidad que permita ingresar una tarea y agregarla automaticamente a una lista
                mediante un botón.
                Las tareas deben mostrarse como una lista y, si no hay tareas ingresadas debe mostrarse un mensaje de
                error.
            </p>
            <p>
                Utiliza <i>v-text-field, v-list</i>, junto con <i>v-for</i> y <i>v-if</i>.
            </p>

            <!-- Forma 1 -->
            <div>
                <v-text-field v-model="tarea" label="Nueva tarea" @keyup.enter="tareas.push(tarea)"
                    @keyup.esc="tarea = ''" />

                <v-btn color="primary" class="mt-2" @click="tareas.push(tarea); tarea = ''">Agregar</v-btn>
                <p v-if="tareas.length === 0" class="text-deep-purple">No hay tareas aún.</p>

                <v-list v-else :items="tareas" />

            </div>



            <!--Forma 2 -->
            <div>
                <v-text-field v-model="tarea" label="Nueva tarea" />

                <v-btn color="primary" class="mt-2" @dblclick="tareas.push(tarea); tarea = ''">Agregar</v-btn>
                <p v-if="tareas.length === 0" class="text-error">No hay tareas aún.</p>

                <v-list v-else>
                    <v-list-subheader color="purple" class="bg-grey-lighten-2">
                        Mis tareas
                    </v-list-subheader>
                    <v-list-item v-for="tarea in tareas" :key="tarea" :title="tarea" class="bg-grey-lighten-4" />
                </v-list>
            </div>

            <!-- Forma 3, con card -->
            <div>
                <v-text-field v-model="tarea" label="Nueva tarea" />

                <v-btn color="primary" class="mt-2" @click="tareas.push(tarea); tarea = ''">Agregar</v-btn>
                <p v-if="tareas.length === 0" class="text-error">No hay tareas aún.</p>

                <v-card v-else max-width="300">
                    <v-card-title> Mis tareas
                    </v-card-title>
                    <v-list>
                        <v-list-item v-for="tarea in tareas" :key="tarea" :title="tarea" />
                    </v-list>
                </v-card>
            </div>

            <!-- Forma 4, con personalizaciones  -->
            <div>
                <v-text-field v-model="tarea" label="Nueva tarea" />

                <v-btn color="primary" class="mt-2" @dblclick="tareas.push(tarea); tarea = ''">Agregar</v-btn>
                <p v-if="tareas.length === 0" class="text-error">No hay tareas aún.</p>

                <v-card v-else max-width="300" color="teal-darken-2">
                    <v-card-title class="text-white"> Mis tareas
                    </v-card-title>
                    <v-list bg-color="blue-grey-lighten-4">
                        <v-list-item v-for="tarea in tareas" :key="tarea" :title="tarea" />
                        <v-divider color="black" thickness="2" />
                    </v-list>
                </v-card>
            </div>


        </div>



    </v-container>

</template>

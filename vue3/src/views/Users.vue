<script setup>
import { ref, computed } from 'vue'
import Card from '@/components/Card.vue';

const usuarios = ref([
    { id: 1, sueldo: 600000, username: 'Ana', email: 'ana@gmail.com', activo: true, description: 'Encargada de ventas con 5 años de experiencia en atención al cliente, gestión de cuentas y coordinación de campañas comerciales. Especializada en fidelización y métricas de rendimiento.' },
    { id: 2, sueldo: 7500000, username: 'Luis', email: 'luis@gmail.com', activo: false, description: 'Desarrollador frontend con 4 años de experiencia en Vue.js y Node.js. Implementa funcionalidades, optimiza rendimiento y corrige errores en la interfaz. Trabaja con APIs REST y participa en revisiones de código para asegurar despliegues fiables.' },
    { id: 3, sueldo: 690000, username: 'Maria', email: 'maria@hotmail.com', activo: true, description: 'Diseñadora UX/UI con 5 años de experiencia en investigación de usuarios. Realiza pruebas de usabilidad, define guías de estilo y colabora con producto y desarrollo para iterar en flujos, mejorar accesibilidad y aumentar métricas de conversión.' },
])

const sueldoMinimo = ref(0)

function eliminar(id) {
    console.log("Funcion para eliminar usuarios")
    usuarios.value = usuarios.value.filter(u => u.id !== id)
}

const usuariosFiltrados = computed(() =>
    usuarios.value.filter(u => u.sueldo >= sueldoMinimo.value)
)
</script>

<template>
    <v-container>

        <h2 class="text-h5 mb-4">Usuarios</h2>
        <v-text-field v-model="sueldoMinimo" type="number" label="Sueldo mínimo">

        </v-text-field>
        <v-row>
            <v-col v-for="u in usuariosFiltrados" :key="u.id" cols="4">
                <Card :id="u.id" :title="u.username" :email="u.email" :activo="u.activo" :description="u.description"
                    :sueldo="u.sueldo" @eliminar="eliminar" />
            </v-col>
        </v-row>

    </v-container>
</template>
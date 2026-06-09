<script setup>
import { ref } from 'vue'
import Card from '@/components/Card.vue';

const productos = ref([
    { id: 1, name: 'Laptop', price: 1200, descuento: true, description: 'Laptop de alta gama con procesador Intel i7, 16GB RAM y 512GB SSD. Ideal para profesionales y gamers.' },
    { id: 2, name: 'Smartphone', price: 800, descuento: false, description: 'Smartphone con pantalla AMOLED de 6.5 pulgadas, cámara de 48MP y batería de larga duración.' },
    { id: 3, name: 'Auriculares', price: 150, descuento: true, description: 'Auriculares inalámbricos con cancelación de ruido activa y sonido envolvente para una experiencia auditiva inmersiva.' },
    { id: 4, name: 'Monitor', price: 300, descuento: false, description: 'Monitor de 27 pulgadas con resolución 4K, panel IPS y frecuencia de actualización de 144Hz para una visualización nítida y fluida.' },
    { id: 5, name: 'Teclado mecánico', price: 100, descuento: true, description: 'Teclado mecánico con retroiluminación RGB, switches táctiles y diseño ergonómico para una escritura cómoda y precisa.' },
    { id: 6, name: 'Ratón gaming', price: 80, descuento: false, description: 'Ratón gaming con sensor óptico de alta precisión, botones programables y diseño ergonómico para sesiones de juego prolongadas.' },

])

function eliminarProducto(id) {
    productos.value = productos.value.filter(p => p.id !== id)
}
</script>

<template>
    <v-container>

        <h2 class="text-h5 mb-4">Productos</h2>
        <v-row>
            <v-col v-for="p in productos" :key="p.id" cols="4">
                <Card :id="p.id" :title="p.name" :description="p.description" :sueldo="p.price" :activo="p.descuento"
                    @eliminar="eliminarProducto(p.id)" />
            </v-col>
        </v-row>
    </v-container>
</template>
<script setup>
import { ref, onMounted } from 'vue'
import { useAuthStore } from '@/stores/auth';
import Card from '@/components/Card.vue';

const auth = useAuthStore()
const productos = ref([])
const nuevoProducto = ref({
    nombre: '',
    descripcion: '',
    precio: 0,
    stock: 0
})
async function cargarProdutos() {
    const response = await fetch('http://127.0.0.1:8000/products')
    if (!response.ok) {
        console.log("Error al recuperar la información: ", response.status)
        return
    }
    console.log(response)
    productos.value = await response.json()
}


async function eliminarProducto(id) {
    const response = await fetch(`http://127.0.0.1:8000/products/${id}`,
        {
            method: 'DELETE'
        })
    if (!response.ok) {
        console.log("Error al eliminar: ", response.status)
        return
    }
    console.log(response)
    await cargarProdutos()

}

async function añadirProducto() {
    const response = await fetch("http://127.0.0.1:8000/products",
        {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(nuevoProducto.value)

        }
    )
    if (!response.ok) {
        console.log("Error al crear el producto: ", response.status)
        return
    }
    await cargarProdutos()
    nuevoProducto.value = { nombre: '', descripcion: '', precio: 0, stock: 0 }
    console.log(JSON.stringify(nuevoProducto.value))
}
// cargarProdutos()


onMounted(() => {
    cargarProdutos()
})
</script>

<template>
    <v-container>
{{ auth }}
        <h2 class="text-h5 mb-4">Listado de productos</h2>
        <v-row>
            <v-col v-for="p in productos" :key="p.id" cols="4">
                <Card :id="p.id" :title="p.nombre" :description="p.descripcion" :sueldo="p.precio"
                    @eliminar="eliminarProducto(p.id)" />
            </v-col>
        </v-row>
        <h2> Ingresar producto </h2>
        <v-row>
            <v-col cols="6">
                <v-text-field v-model="nuevoProducto.nombre" label="Nombre" variant="outlined">
                </v-text-field>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="6">
                <v-textarea v-model="nuevoProducto.descripcion" label="Descripción" variant="outlined">
                </v-textarea>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="3">
                <v-text-field v-model="nuevoProducto.precio" label="Precio" variant="outlined"></v-text-field>
            </v-col>
            <v-col cols="3">
                <v-text-field v-model="nuevoProducto.stock" label="Stock" variant="outlined"></v-text-field>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="3">
                <v-btn color="teal" @click="añadirProducto"> Guardar producto</v-btn>
            </v-col>
        </v-row>
        {{ nuevoProducto }}
        <br><br><br><br><br><br><br><br><br><br><br><br>
    </v-container>
</template>
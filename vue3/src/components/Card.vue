<script setup>
defineProps({
    id: { type: Number, requiered: true },
    title: { type: String, requiered: true },
    email: { type: String, requiered: false },
    description: { type: String, requiered: false },
    activo: { type: Boolean, default: true },
    sueldo: { type: Number, requiered: true }
})

const emit = defineEmits(['eliminar'])
</script>

<template>
    <v-card :color="activo ? 'teal-lighten-2' : 'red-lighten-2'">
        <v-card-title>{{ title }}</v-card-title>
        <v-card-subtitle>{{ email }}</v-card-subtitle>
        <v-card-text class="text-body-1">{{ description }} <br> <br> $ {{ sueldo }}</v-card-text>
        <v-card-actions>
            <v-spacer />
            <v-btn color="white" variant="tonal" @click="emit('eliminar', id)"> Eliminar</v-btn>
        </v-card-actions>
    </v-card>
</template>
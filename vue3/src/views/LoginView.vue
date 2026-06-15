<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
const router = useRouter()

const credenciales = ref({
    username: '',
    password: ''
})

const error = ref(null)
async function login() {
    const body = new URLSearchParams()
    body.append("username", credenciales.value.username)
    body.append("password", credenciales.value.password)
    error.value = null
    try {
        const response = await fetch("http://127.0.0.1:8000/users/login", {
            method: "POST",
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: body
        })
        if (!response.ok) {
            console.log("Problemas")
            error.value = "Usuario o contraseña incorrecta"
        }
        const data = await response.json()
        console.log(data)
        if (response.ok) {
            router.push({ name: 'products' })
            localStorage.setItem('token', data.access_token)
        }
    } catch (e) {
        console.log(e)
        error.value = e
    }
}

</script>

<template>
    <v-container>
        <v-row justify="center">
            <v-col cols="4">
                <v-card title="Iniciar sesión" rounded="lg">
                    <v-alert v-if="error" type="error" variant="tonal">
                        {{ error }}
                    </v-alert>
                    <v-card-text class="pa-6">
                        <v-text-field label="Usuario" variant="outlined" v-model="credenciales.username">
                        </v-text-field>
                        <v-text-field type="password" label="Contraseña" variant="outlined"
                            v-model="credenciales.password"></v-text-field>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer />
                        <v-btn color="teal" @click="login"> Ingresar</v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>
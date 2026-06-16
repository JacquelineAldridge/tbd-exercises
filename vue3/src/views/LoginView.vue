<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const auth = useAuthStore()

const credenciales = ref({
    username: '',
    password: ''
})

const error = ref(null)

async function login() {
    const ok = await auth.login(credenciales.value.username, credenciales.value.password)
    if(ok){
        console.log(ok)
        router.push({ name: 'products' })

    }
}

</script>

<template>
    <v-container>
        <v-row justify="center">
            <v-col cols="4">
                <v-card title="Iniciar sesión" rounded="lg">
                    <v-alert v-if="auth.error" type="error" variant="tonal">
                        {{ auth.error }}
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
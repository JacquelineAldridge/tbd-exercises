import {ref, computed} from 'vue'
import {defineStore} from 'pinia'
import {jwtDecode} from 'jwt-decode'

const BASE_URL = 'http://127.0.0.1:8000'

function tokenEsValido(token){
    if(!token) return false
    try{
        const payload = jwtDecode(token)
        return payload.exp * 1000 > Date.now()
    }catch(e){
        return false
    }
}

export const useAuthStore = defineStore('auth', ()=>{
    const tokenGuardado = localStorage.getItem('token')
    if(tokenGuardado && !tokenEsValido(tokenGuardado)){
        localStorage.removeItem('token')
    }
    const token = ref(tokenEsValido(tokenGuardado) ? tokenGuardado: null)
    const usuario = ref(null)
    const error = ref(null)
    const estaLogueado = computed(()=> tokenEsValido(token.value))

    async function login(username, password) {
    const body = new URLSearchParams()
    body.append("username", username)
    body.append("password", password)
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
        if (response.ok) {
            localStorage.setItem('token', data.access_token)
            token.value = data.access_token
            cargarUsuario()
            return true
        }
    } catch (e) {
        console.log(e)
        error.value = e
    }
}
async function cargarUsuario() {
    if (!estaLogueado.value) return
    const response = await fetch(`${BASE_URL}/users/me`, {
      headers: { Authorization: `Bearer ${token.value}` }
    })
    if (!response.ok) {
      logout()
      return
    }
    usuario.value = await response.json()
  }

  function logout() {
    token.value = null
    usuario.value = null
    localStorage.removeItem('token')
  }

return {token, usuario, error, estaLogueado, login, cargarUsuario, logout}
})


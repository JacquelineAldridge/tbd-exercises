# Ejercicios de Python básico

**1.** Crea una función `analizar_ventas(ventas_mensuales)` que reciba un diccionario de ventas:

```python
ventas_mensuales = {
    "Enero": [120000, 85000, 95000, 110000],
    "Febrero": [130000, 90000, 88000, 125000],
    "Marzo": [140000, 95000, 105000, 135000]
}
```

La función debe retornar un diccionario con el total de cada mes y cuál fue el mejor mes.

**2.** Crea una función `crear_perfil(nombre, edad, altura, es_estudiante)` que reciba los datos de una persona y retorne un string formateado con toda la información usando f-strings.

**3.** Crea una función `analizar_productos(productos)` que reciba una lista de productos:
```python
productos = [
    {"nombre": "Laptop", "precio": 800000, "categoria": "Tecnología"},
    {"nombre": "Mouse", "precio": 15000, "categoria": "Tecnología"},
    {"nombre": "Escritorio", "precio": 120000, "categoria": "Muebles"},
    {"nombre": "Silla", "precio": 80000, "categoria": "Muebles"}
]
```

La función debe retornar el precio promedio y el producto más caro.

**4.** Crea una función `contar_hasta(limite, parar_en)` que imprima números del 1 hasta `limite`, pero se detenga si encuentra el número `parar_en`.

**5.** Crea una función `calcular_total_compra(lista_compras)` que reciba una lista de productos con precios y retorne el costo total. También crea `agregar_producto(lista, nombre, precio)` para agregar productos a la lista.

**6.** Crea una función `limpiar_nombres(nombres)` que reciba una lista como:
```python
nombres = ["ana maría", "CARLOS PÉREZ", "  luis  ", "María José"]
```

Debe retornar los nombres limpios (sin espacios extra, primera letra mayúscula) y contar cuántos tienen más de una palabra.

**7.** Crea una función `crear_libro(titulo, autor, año, paginas)` que retorne un diccionario con la información del libro, y otra función `mostrar_libro(libro)` que imprima la información de forma ordenada.

**8.** Crea una función `filtrar_numeros(lista_numeros)` que reciba una lista de números del 1 al 20 y retorne tres listas: números pares, cuadrados de números impares, y números divisibles por 3.

**9.** Crea una función `comparar_temperaturas(temperaturas)` que reciba un diccionario:

```python
temperaturas = {
    "Santiago": [22, 25, 28, 26, 24, 20, 18, 21, 23, 27],
    "Valparaíso": [18, 20, 22, 21, 19, 17, 16, 18, 20, 23]
}
```

Debe retornar cuál ciudad tiene mayor temperatura promedio y cuál tiene mayor variación.

**10.** Crea una función `evaluar_nota(nota)` que reciba una nota entre 1.0 y 7.0 y retorne si está "Aprobado", "Reprobado", o "Aprobado con distinción".

**11.** Crea una función `calcular_gasto_promedio(gastos)` que reciba una lista de gastos diarios y retorne el promedio. Luego crea `analizar_gastos_semanales(semanas)` que use la función anterior para analizar múltiples semanas.

**12.** Crea funciones para manejar una lista de frutas: `obtener_primera_y_ultima(frutas)`, `agregar_fruta(frutas, nueva_fruta)`, y `mostrar_frutas(frutas)` que muestren toda la lista.

**13.** Crea funciones para calcular estadísticas de un equipo de fútbol:

```python
partidos = [
    {"rival": "Equipo A", "goles_favor": 2, "goles_contra": 1},
    {"rival": "Equipo B", "goles_favor": 0, "goles_contra": 3},
    {"rival": "Equipo C", "goles_favor": 4, "goles_contra": 2},
    {"rival": "Equipo D", "goles_favor": 1, "goles_contra": 1}
]
```

Implementa `calcular_puntos(partidos)` (3 puntos por victoria, 1 por empate), `goles_totales(partidos)` y `mejor_resultado(partidos)`.

**14.** Crea una función `procesar_mensajes(mensajes)` que reciba una lista como:

```python
mensajes = [
    "2024-01-15 10:30:45 Usuario conectado correctamente",
    "2024-01-15 10:31:12 Error al conectar usuario",
    "2024-01-15 10:31:45 Usuario desconectado",
    "2024-01-15 10:32:01 Error de sistema crítico"
]
```

Debe separar cada mensaje en fecha, hora y descripción, y contar cuántos errores hay.

**15.** Crea una función `analizar_texto(texto)` que retorne un diccionario con el número total de palabras, palabras únicas, y la palabra más larga. Prueba con: "Python es un lenguaje de programación. Python es fácil de aprender."
# Ejercicios de Programación Orientada a Objetos en Python

## 1. Producto

Crea una clase `Producto` con los siguientes atributos:
- `nombre` (string)
- `precio` (float) 
- `stock` (int)

Implementa los métodos:
- `__init__(self, nombre, precio, stock)`
- `mostrar_info(self)` - imprime la información del producto
- `aplicar_descuento(self, porcentaje)` - reduce el precio según el porcentaje
- `vender(self, cantidad)` - reduce el stock si hay suficiente, sino imprime error

```python
# Ejemplo de uso:
producto = Producto("Laptop", 800000, 5)
producto.mostrar_info()
producto.aplicar_descuento(10)
producto.vender(2)
```

## 2. CuentaBancaria

Crea una clase `CuentaBancaria` con:
- `titular` (string)
- `_saldo` (float, protegido)
- `_numero_cuenta` (string, protegido)

Métodos:
- `__init__(self, titular, numero_cuenta, saldo_inicial=0)`
- `depositar(self, monto)` - agrega dinero al saldo
- `retirar(self, monto)` - quita dinero si hay suficiente saldo
- `obtener_saldo(self)` - retorna el saldo actual
- `transferir(self, cuenta_destino, monto)` - transfiere dinero a otra cuenta
- `__str__(self)` - retorna información de la cuenta en formato legible

```python
# Ejemplo:
cuenta1 = CuentaBancaria("Ana García", "123456789", 100000)
cuenta2 = CuentaBancaria("Carlos López", "987654321", 50000)
cuenta1.transferir(cuenta2, 25000)
print(cuenta1)
```

## 3. Sistema de Empleados

Crea una clase base `Empleado` con:
- `nombre`, `apellido`, `rut`, `sueldo_base`
- Método `calcular_sueldo()` que retorna el sueldo base
- Método `__str__()` que muestra información del empleado

Crea las siguientes clases que deben funcionar como `Empleado` pero con características adicionales:

**`Vendedor`**:
- Atributo adicional: `comisiones` (lista de montos)
- Su `calcular_sueldo()` debe incluir: sueldo base + suma de comisiones
- Método `agregar_comision(self, monto)` para añadir comisiones

**`Gerente`**:
- Atributo adicional: `bono_gerencial` (porcentaje)
- Su `calcular_sueldo()` debe incluir: sueldo base + (sueldo base * bono/100)

```python
# Ejemplo:
vendedor = Vendedor("Juan", "Pérez", "12345678-9", 500000)
vendedor.agregar_comision(50000)
vendedor.agregar_comision(75000)
print(f"Sueldo total: {vendedor.calcular_sueldo()}")

gerente = Gerente("María", "González", "98765432-1", 800000, 25)
print(f"Sueldo total: {gerente.calcular_sueldo()}")
```

## 4. Calculadora Simple

Crea una clase `Calculadora` con:
- Métodos `sumar(a, b)`, `restar(a, b)`, `multiplicar(a, b)`, `dividir(a, b)`
- El método `dividir` debe mostrar un mensaje de error si se divide por cero
- Método `__str__()` que retorne "Calculadora lista para usar"

```python
# Ejemplo:
calc = Calculadora()
print(calc.sumar(5, 3))     # 8
print(calc.dividir(10, 0))  # Error: No se puede dividir por cero
print(calc)
```

## 5. Vehículos

Crea una clase `Vehiculo` con:
- `marca`, `modelo`, `año`
- Método `arrancar()` que imprime "El vehículo está arrancando"
- Método `__str__()` con información del vehículo

Crea las clases `Auto` y `Motocicleta` que funcionen como `Vehiculo` pero:

**`Auto`**:
- Atributo adicional: `num_puertas`
- Su `arrancar()` debe decir "El auto está arrancando"

**`Motocicleta`**:
- Atributo adicional: `cilindrada`
- Su `arrancar()` debe decir "La motocicleta está arrancando"

Crea una función `probar_vehiculo(vehiculo)` que funcione con cualquier tipo de vehículo.

```python
# Ejemplo:
auto = Auto("Toyota", "Corolla", 2020, 4)
moto = Motocicleta("Honda", "CBR", 2021, 600)

vehiculos = [auto, moto]
for vehiculo in vehiculos:
    probar_vehiculo(vehiculo)
```

## 6. Rectángulo con validación

Crea una clase `Rectangulo` con:
- Atributos internos `_ancho` y `_alto` (protegidos)
- Debe permitir leer y escribir `ancho` y `alto` como atributos normales
- Al escribir `ancho` o `alto`, debe validar que sean positivos (sino mostrar error)
- Debe calcular automáticamente `area` y `perimetro` cuando se acceda a ellos
- Método `__str__()` que muestre las dimensiones y el área

```python
# Ejemplo:
rect = Rectangulo(5, 3)
print(rect.area)      # 15
rect.ancho = 10       # Validación automática
print(rect.area)      # 30
rect.ancho = -5       # Debe mostrar error
print(rect)
```

## 7. Inventario

Crea una clase `Inventario` que se comporte como un diccionario de productos:

- Debe permitir acceso con corchetes: `inventario["laptop"]`
- Debe permitir asignación con corchetes: `inventario["mouse"] = {"precio": 15000, "cantidad": 20}`
- Debe funcionar con `len()` para obtener cantidad de productos
- Debe poder imprimirse mostrando todo el inventario
- Método `valor_total()` que calcule el valor total (precio × cantidad de todos los productos)
- Método `productos_disponibles()` que retorne productos con cantidad > 0

```python
# Ejemplo:
inventario = Inventario()
inventario["laptop"] = {"precio": 800000, "cantidad": 5}
inventario["mouse"] = {"precio": 15000, "cantidad": 20}
print(len(inventario))  # 2
print(inventario["laptop"])  # {'precio': 800000, 'cantidad': 5}
print(f"Valor total: ${inventario.valor_total()}")
```

## 8. Punto Matemático

Crea una clase `Punto` que represente un punto en el plano cartesiano:

- Atributos `x` e `y`
- Debe poder imprimirse como "(x, y)"
- Debe poder sumarse con otro punto usando `+` (suma las coordenadas)
- Debe poder compararse con otro punto usando `==` (igualdad de coordenadas)
- Método `distancia_origen()` que calcule la distancia al punto (0,0)

```python
# Ejemplo:
p1 = Punto(3, 4)
p2 = Punto(1, 2)
p3 = Punto(3, 4)

print(p1)                    # (3, 4)
suma = p1 + p2               # Suma de puntos
print(suma)                  # (4, 6)
print(p1 == p3)              # True
print(p1 == p2)              # False
print(p1.distancia_origen()) # 5.0
```
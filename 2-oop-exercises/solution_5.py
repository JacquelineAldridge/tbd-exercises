# Crea una clase `Vehiculo` con:
# - `marca`, `modelo`, `año`
# - Método `arrancar()` que imprime "El vehículo está arrancando"
# - Método `__str__()` con información del vehículo

# Crea las clases `Auto` y `Motocicleta` que funcionen como `Vehiculo` pero:

# **`Auto`**:
# - Atributo adicional: `num_puertas`
# - Su `arrancar()` debe decir "El auto está arrancando"

# **`Motocicleta`**:
# - Atributo adicional: `cilindrada`
# - Su `arrancar()` debe decir "La motocicleta está arrancando"

# Crea una función `probar_vehiculo(vehiculo)` que funcione con cualquier tipo de vehículo.


class Vehiculo:
    """Clase base para vehículos.

    Attributes:
        marca: Marca del vehículo.
        modelo: Modelo del vehículo.
        año: Año de fabricación.
    """

    def __init__(self, marca, modelo, año):
        """Inicializa un vehículo.

        Args:
            marca: Marca del vehículo.
            modelo: Modelo del vehículo.
            año: Año de fabricación.
        """
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def arrancar(self):
        """Arranca el vehículo."""
        print(f"El vehículo esta arrancando")

    def __str__(self):
        """Representación en cadena del vehículo.

        Returns:
            Información del vehículo.
        """
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}"


class Auto(Vehiculo):
    """Auto que extiende Vehiculo.

    Attributes:
        num_puertas: Número de puertas.
    """

    def __init__(self, marca, modelo, año, num_puertas):
        """Inicializa un auto.

        Args:
            marca: Marca del auto.
            modelo: Modelo del auto.
            año: Año de fabricación.
            num_puertas: Número de puertas.
        """
        super().__init__(marca, modelo, año)
        self.num_puertas = num_puertas

    def arrancar(self):
        """Arranca el auto."""
        print("El auto esta arrancando")


class Motocicleta(Vehiculo):
    """Motocicleta que extiende Vehiculo.

    Attributes:
        cilindrada: Cilindrada de la motocicleta.
    """

    def __init__(self, marca, modelo, año, cilindrada):
        """Inicializa una motocicleta.

        Args:
            marca: Marca de la motocicleta.
            modelo: Modelo de la motocicleta.
            año: Año de fabricación.
            cilindrada: Cilindrada de la motocicleta.
        """
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada

    def arrancar(self):
        """Arranca la motocicleta."""
        print("La motocicleta esta arrancadando")


def probar_vehiculo(vehiculo):
    """Prueba cualquier tipo de vehículo.

    Args:
        vehiculo: Instancia de vehículo a probar.
    """
    vehiculo.arrancar()
    print(vehiculo)


auto = Auto("Toyota", "Corolla", 2020, 4)
moto = Motocicleta("Honda", "CBR", 2021, 600)

vehiculos = [auto, moto]
for vehiculo in vehiculos:
    probar_vehiculo(vehiculo)

# Crea una clase base `Empleado` con:
# - `nombre`, `apellido`, `rut`, `sueldo_base`
# - Método `calcular_sueldo()` que retorna el sueldo base
# - Método `__str__()` que muestra información del empleado

# Crea las siguientes clases que deben funcionar como `Empleado` pero con características adicionales:

# **`Vendedor`**:
# - Atributo adicional: `comisiones` (lista de montos)
# - Su `calcular_sueldo()` debe incluir: sueldo base + suma de comisiones
# - Método `agregar_comision(self, monto)` para añadir comisiones

# **`Gerente`**:
# - Atributo adicional: `bono_gerencial` (porcentaje)
# - Su `calcular_sueldo()` debe incluir: sueldo base + (sueldo base * bono/100)


class Empleado:
    """Representa un empleado con información básica.

    Attributes:
        nombre: Nombre del empleado.
        apellido: Apellido del empleado.
        rut: Número de identificación social.
        sueldo_base: Salario del empleado.
    """

    def __init__(self, nombre, apellido, rut, sueldo_base=0):
        """Inicializa una nueva instancia de Empleado.

        Args:
            nombre: Nombre del empleado.
            apellido: Apellido del empleado.
            rut: Número de identificación social.
            sueldo_base: Salario inicial (por defecto 0).
        """
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.sueldo_base = sueldo_base

    def calcular_sueldo(self):
        """Calcula el salario del empleado.

        Returns:
            El salario calculado.
        """
        return self.sueldo_base

    def __str__(self):
        """Representación en cadena del empleado.

        Returns:
            Cadena con detalles del empleado.
        """
        return (
            f"Detalles del empleado - Nombre: {self.nombre} ; Apellido: {self.apellido} ; "
            + "RUT: {self.rut} ; Sueldo: {self.sueldo_base}"
        )


class Vendedor(Empleado):
    """Representa un vendedor con comisiones.

    Attributes:
        nombre: Nombre del empleado.
        apellido: Apellido del empleado.
        rut: Número de identificación social.
        sueldo_base: Salario del empleado.
        comisiones: Lista de comisiones ganadas.
    """

    def __init__(self, nombre, apellido, rut, sueldo_base, comisiones=None):
        """Inicializa una nueva instancia de Vendedor.

        Args:
            nombre: Nombre del vendedor.
            apellido: Apellido del vendedor.
            rut: Número de identificación social.
            sueldo_base: Salario inicial.
            comisiones: Lista inicial de comisiones (por defecto None).
        """
        super().__init__(nombre, apellido, rut, sueldo_base)

        if comisiones is None:
            self.comisiones = []
        else:
            self.comisiones = comisiones

    def agregar_comision(self, monto):
        """Añade una comisión a la lista.

        Args:
            monto: Monto de la comisión.
        """
        self.comisiones.append(monto)

    def calcular_sueldo(self):
        """Calcula el salario incluyendo comisiones.

        Returns:
            El salario total con comisiones.
        """
        total_comisiones = sum(self.comisiones)
        self.sueldo_base += total_comisiones
        return self.sueldo_base


class Gerente(Empleado):
    """Representa un gerente con bonificación.

    Attributes:
        nombre: Nombre del empleado.
        apellido: Apellido del empleado.
        rut: Número de identificación social.
        sueldo_base: Salario del empleado.
        bono_gerencial: Porcentaje de bonificación gerencial.
    """

    def __init__(self, nombre, apellido, rut, sueldo_base, bono_gerencial):
        """Inicializa una nueva instancia de Gerente.

        Args:
            name: Nombre del gerente.
            apellido: Apellido del gerente.
            rut: Número de identificación social.
            sueldo_base: Salario inicial.
            bono_gerencial: Porcentaje de bonificación gerencial.
        """
        super().__init__(nombre, apellido, rut, sueldo_base)
        self.bono_gerencial = bono_gerencial

    def calculate_salary(self):
        """Calcula el salario con bonificación gerencial.

        Returns:
            El salario con bonificación aplicada.
        """
        self.sueldo_base = self.sueldo_base + (self.sueldo_base * (self.bono_gerencial / 100))
        return self.sueldo_base


vendedor = Vendedor("Juan", "Pérez", "12345678-9", 500000)
vendedor.agregar_comision(50000)
vendedor.agregar_comision(75000)
print(f"Vendedor salario : {vendedor.calcular_sueldo()}")

gerente = Gerente("María", "González", "98765432-1", 800000, 25)
print(f"Gerente salario: {gerente.calcular_sueldo()}")

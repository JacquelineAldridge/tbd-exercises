# Crea una clase `Rectangulo` con:
# - Atributos internos `_ancho` y `_alto` (protegidos)
# - Debe permitir leer y escribir `ancho` y `alto` como atributos normales
# - Al escribir `ancho` o `alto`, debe validar que sean positivos (sino mostrar error)
# - Debe calcular automáticamente `area` y `perimetro` cuando se acceda a ellos
# - Método `__str__()` que muestre las dimensiones y el área


class Rectangulo:
    """Representa un rectángulo con validación de dimensiones.

    Attributes:
        ancho: Ancho del rectángulo (debe ser positivo).
        alto: Alto del rectángulo (debe ser positivo).
        area: Área del rectángulo (calculada automáticamente).
        perimetro: Perímetro del rectángulo (calculado automáticamente).
    """

    def __init__(self, ancho, alto):
        """Inicializa un rectángulo.

        Args:
            ancho: Ancho inicial del rectángulo.
            alto: Alto inicial del rectángulo.
        """
        self._ancho = ancho
        self._alto = alto

    @property
    def ancho(self):
        """Obtiene el ancho del rectángulo.

        Returns:
            El ancho actual del rectángulo.
        """
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        """Establece el ancho del rectángulo con validación.

        Args:
            valor: Nuevo valor para el ancho.
        """
        if valor <= 0:
            print("Error: El ancho debe ser positivo")
            return
        self._ancho = valor

    @property
    def alto(self):
        """Obtiene el alto del rectángulo.

        Returns:
            El alto actual del rectángulo.
        """
        return self._alto

    @alto.setter
    def alto(self, valor):
        """Establece el alto del rectángulo con validación.

        Args:
            valor: Nuevo valor para el alto.
        """
        if valor <= 0:
            print("Error: El alto debe ser positivo")
            return
        self._alto = valor

    @property
    def area(self):
        """Calcula el área del rectángulo.

        Returns:
            El área del rectángulo.
        """
        return self._ancho * self._alto

    @property
    def perimetro(self):
        """Calcula el perímetro del rectángulo.

        Returns:
            El perímetro del rectángulo.
        """
        return 2 * (self._ancho + self._alto)

    def __str__(self):
        """Representación en cadena del rectángulo.

        Returns:
            Información del rectángulo con dimensiones y área.
        """
        return f"Rectángulo: {self._ancho} x {self._alto}, Área: {self.area}"


# Ejemplo de uso
rect = Rectangulo(5, 3)
print(rect.area)  # 15
rect.ancho = 10  # Validación automática
print(rect.area)  # 30
rect.ancho = -5  # Debe mostrar error
print(rect)

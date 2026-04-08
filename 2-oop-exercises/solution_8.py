# Crea una clase `Punto` que represente un punto en el plano cartesiano:

# - Atributos `x` e `y`
# - Debe poder imprimirse como "(x, y)"
# - Debe poder sumarse con otro punto usando `+` (suma las coordenadas)
# - Debe poder compararse con otro punto usando `==` (igualdad de coordenadas)
# - Método `distancia_origen()` que calcule la distancia al punto (0,0)
import math


class Punto:
    """Representa un punto en el plano cartesiano.

    Attributes:
        x: Coordenada x del punto.
        y: Coordenada y del punto.
    """

    def __init__(self, x, y):
        """Inicializa un punto.

        Args:
            x: Coordenada x.
            y: Coordenada y.
        """
        self.x = x
        self.y = y

    def __str__(self):
        """Representación en cadena del punto.

        Returns:
            Cadena con las coordenadas del punto.
        """
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        """Suma dos puntos.

        Args:
            other: Otro punto a sumar.

        Returns:
            Nuevo punto con la suma de coordenadas.
        """
        return Punto(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        """Compara si dos puntos son iguales.

        Args:
            other: Otro punto a comparar.

        Returns:
            True si los puntos tienen las mismas coordenadas.
        """
        return self.x == other.x and self.y == other.y

    def distancia_origen(self):
        """Calcula la distancia desde el punto al origen.

        Returns:
            La distancia euclidiana al origen (0, 0).
        """
        return math.sqrt(self.x**2 + self.y**2)


p1 = Punto(3, 4)
p2 = Punto(1, 2)
p3 = Punto(3, 4)

print(p1)  # (3, 4)
suma = p1 + p2
print(suma)  # (4, 6)
print(p1 == p3)  # True
print(p1 == p2)  # False
print(p1.distancia_origen())  # 5.0

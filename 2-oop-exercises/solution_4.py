# Crea una clase Calculadora con:

# Métodos sumar(a, b), restar(a, b), multiplicar(a, b), dividir(a, b)
# El método dividir debe mostrar un mensaje de error si se divide por cero
# Método __str__() que retorne "Calculadora lista para usar"


class Calculadora:
    """Calculadora básica con operaciones aritméticas."""

    def __init__(self):
        """Inicializa la calculadora."""
        pass

    def __str__(self):
        """Representación en cadena de la calculadora.

        Returns:
            Mensaje indicando que la calculadora está lista.
        """
        return "Calculadora lista para usar"

    def sumar(self, a, b):
        """Suma dos números.

        Args:
            a: Primer número.
            b: Segundo número.

        Returns:
            La suma de a y b.
        """
        return a + b

    def restar(self, a, b):
        """Resta dos números.

        Args:
            a: Primer número.
            b: Segundo número.

        Returns:
            La resta de a y b.
        """
        return a - b

    def multiplicar(self, a, b):
        """Multiplica dos números.

        Args:
            a: Primer número.
            b: Segundo número.

        Returns:
            El producto de a y b.
        """
        return a * b

    def dividir(self, a, b):
        """Divide dos números.

        Args:
            a: Dividendo.
            b: Divisor.

        Returns:
            El cociente de a y b, o mensaje de error si b es 0.
        """
        if b == 0:
            return "Error: No se puede dividir por cero"
        return a / b


calc = Calculadora()
print(calc.sumar(5, 3))
print(calc.dividir(10, 2))
print(calc)

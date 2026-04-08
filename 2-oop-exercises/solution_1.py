# Crea una clase `Producto` con los siguientes atributos:
# - `nombre` (string)
# - `precio` (float)
# - `stock` (int)

# Implementa los métodos:
# - `__init__(self, nombre, precio, stock)`
# - `mostrar_info(self)` - imprime la información del producto
# - `aplicar_descuento(self, porcentaje)` - reduce el precio según el porcentaje
# - `vender(self, cantidad)` - reduce el stock si hay suficiente, sino imprime error


class Producto:
    """Representa un producto con gestión de inventario.

    Attributes:
        nombre: Nombre del producto.
        precio: Precio del producto.
        stock: Cantidad en inventario.
    """

    def __init__(self, nombre, precio, stock):
        """Inicializa una nueva instancia de Producto.

        Args:
            nombre: Nombre del producto.
            precio: Precio del producto.
            stock: Cantidad inicial en inventario.
        """
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        """Muestra la información del producto."""
        print(f"Producto: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}")

    def aplicar_descuento(self, porcentaje):
        """Aplica un descuento al precio del producto.

        Args:
            porcentaje: Porcentaje de descuento a aplicar.
        """
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento
        print(f"Nuevo precio de {self.nombre} después del descuento: {self.precio:.0f}")

    def vender(self, cantidad):
        """Vende una cantidad especificada del producto.

        Args:
            cantidad: Cantidad de productos a vender.
        """
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Vendidos {cantidad} de {self.nombre}. Stock restante: {self.stock}")
        else:
            print(
                f"No hay suficiente stock para vender {cantidad} de {self.nombre}. Stock actual: {self.stock}"
            )


producto = Producto("Laptop", 800000, 5)
producto.mostrar_info()
producto.aplicar_descuento(10)
producto.vender(2)

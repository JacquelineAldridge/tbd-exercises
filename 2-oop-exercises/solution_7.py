# Crea una clase `Inventario` que se comporte como un diccionario de productos:
# - Debe permitir acceso con corchetes: `inventario["laptop"]`
# - Debe permitir asignación con corchetes: `inventario["mouse"] = {"precio": 15000, "cantidad": 20}`
# - Debe funcionar con `len()` para obtener cantidad de productos
# - Debe poder imprimirse mostrando todo el inventario
# - Método `valor_total()` que calcule el valor total (precio × cantidad de todos los productos)
# - Método `productos_disponibles()` que retorne productos con cantidad > 0


class Inventario:
    """Representa un inventario de productos que se comporta como un diccionario.

    Permite gestionar productos con sus precios y cantidades de forma similar
    a un diccionario, con métodos adicionales para cálculos de inventario.
    """

    def __init__(self):
        """Inicializa un inventario vacío."""
        self._productos = {}

    def __getitem__(self, nombre_producto):
        """Permite acceso a productos usando corchetes.

        Args:
            nombre_producto: Nombre del producto a buscar.

        Returns:
            Diccionario con precio y cantidad del producto.

        Raises:
            KeyError: Si el producto no existe.
        """
        return self._productos[nombre_producto]

    def __setitem__(self, nombre_producto, datos_producto):
        """Permite asignar productos usando corchetes.

        Args:
            nombre_producto: Nombre del producto.
            datos_producto: Diccionario con 'precio' y 'cantidad'.
        """
        self._productos[nombre_producto] = datos_producto

    def __len__(self):
        """Retorna la cantidad de productos en el inventario.

        Returns:
            Número de productos diferentes en el inventario.
        """
        return len(self._productos)

    def __str__(self):
        """Representación en cadena del inventario.

        Returns:
            Cadena mostrando todo el inventario.
        """
        if not self._productos:
            return "Inventario vacío"

        resultado = "Inventario:\n"
        for nombre, datos in self._productos.items():
            resultado += f"- {nombre}: ${datos['precio']} (cantidad: {datos['cantidad']})\n"
        return resultado.rstrip()

    def valor_total(self):
        """Calcula el valor total del inventario.

        Returns:
            Valor total (precio × cantidad de todos los productos).
        """
        total = 0
        for datos in self._productos.values():
            total += datos["precio"] * datos["cantidad"]
        return total

    def productos_disponibles(self):
        """Retorna productos con cantidad mayor a 0.

        Returns:
            Diccionario con productos que tienen cantidad > 0.
        """
        disponibles = {}
        for nombre, datos in self._productos.items():
            if datos["cantidad"] > 0:
                disponibles[nombre] = datos
        return disponibles


# Ejemplo de uso
inventario = Inventario()
inventario["laptop"] = {"precio": 800000, "cantidad": 5}
inventario["mouse"] = {"precio": 15000, "cantidad": 20}
inventario["teclado"] = {"precio": 25000, "cantidad": 0}

print(len(inventario))  # 3
print(inventario["laptop"])  # {'precio': 800000, 'cantidad': 5}
print(f"Valor total: ${inventario.valor_total()}")

print("\nInventario completo:")
print(inventario)

print("\nProductos disponibles:")
disponibles = inventario.productos_disponibles()
for nombre, datos in disponibles.items():
    print(f"- {nombre}: ${datos['precio']} (cantidad: {datos['cantidad']})")

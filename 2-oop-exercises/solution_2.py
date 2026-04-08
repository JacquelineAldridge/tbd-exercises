# Crea una clase `CuentaBancaria` con:
# - `titular` (string)
# - `_saldo` (float, protegido)
# - `_numero_cuenta` (string, protegido)

# Métodos:
# - `__init__(self, titular, numero_cuenta, saldo_inicial=0)`
# - `depositar(self, monto)` - agrega dinero al saldo
# - `retirar(self, monto)` - quita dinero si hay suficiente saldo
# - `obtener_saldo(self)` - retorna el saldo actual
# - `transferir(self, cuenta_destino, monto)` - transfiere dinero a otra cuenta
# - `__str__(self)` - retorna información de la cuenta en formato legible


class CuentaBancaria:
    """Representa una cuenta bancaria con operaciones básicas.

    Attributes:
        titular: Nombre del titular de la cuenta.
        saldo: Saldo actual de la cuenta.
    """

    def __init__(self, titular, numero_cuenta, saldo_inicial=0):
        """Inicializa una nueva cuenta bancaria.

        Args:
            titular: Nombre del titular.
            numero_cuenta: Número único de la cuenta.
            saldo_inicial: Saldo inicial (por defecto 0).
        """
        self.titular = titular
        self._numero_cuenta = numero_cuenta
        self._saldo = saldo_inicial

    def depositar(self, monto):
        """Deposita dinero en la cuenta.

        Args:
            monto: Cantidad a depositar.
        """
        if monto > 0:
            self._saldo += monto
            print(f"Depósito realizado: {monto}. Saldo actual: {self._saldo}.")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, monto):
        """Retira dinero de la cuenta.

        Args:
            monto: Cantidad a retirar.
        """
        if 0 < monto <= self._saldo:
            self._saldo -= monto
            print(f"Retiro realizado: {monto}. Saldo actual: {self._saldo}.")
        else:
            print("Fondos insuficientes o cantidad inválida para retirar.")

    def obtener_saldo(self):
        """Obtiene el saldo actual de la cuenta.

        Returns:
            El saldo actual.
        """
        return self._saldo

    def transferir(self, cuenta_destino, monto):
        """Transfiere dinero a otra cuenta.

        Args:
            cuenta_destino: Cuenta de destino.
            monto: Cantidad a transferir.
        """
        if 0 < monto <= self._saldo:
            self._saldo -= monto
            cuenta_destino._saldo += monto
            print(
                f"Transferencia de {monto} a {cuenta_destino.titular} realizada. Saldo actual: {self._saldo}."
            )
        else:
            print("Fondos insuficientes o cantidad inválida para transferir.")

    def obtener_numero_cuenta(self):
        """Obtiene el número de cuenta de forma controlada.

        Returns:
            El número de cuenta.
        """
        return self._numero_cuenta

    def __str__(self):
        """Representación en cadena de la cuenta.

        Returns:
            Cadena con información de la cuenta.
        """
        return f"Cuenta de {self.titular} (Número: {self._numero_cuenta}) - Saldo: {self._saldo}"


cuenta1 = CuentaBancaria("Ana García", "123456789", 100000)
cuenta2 = CuentaBancaria("Carlos López", "987654321", 50000)
cuenta1.transferir(cuenta2, 25000)
print(cuenta1)

# Demostración de que el atributo es privado
print("\n--- Demostrando privacidad del número de cuenta ---")
print(f"Acceso mediante método: {cuenta1.obtener_numero_cuenta()}")

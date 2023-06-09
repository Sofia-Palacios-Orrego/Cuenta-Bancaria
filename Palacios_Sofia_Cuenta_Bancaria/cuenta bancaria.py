class CuentaBancaria:
    cuentas = []  # Lista para almacenar todas las instancias de cuentas bancarias

    def __init__(self, tasa_interes, balance=0): 
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.cuentas.append(self)   #guarda las instancias de la CuentaBancaria en la lista


    def mostrar_info_cuenta(self):
        print("Balance actual: $", self.balance)
        print("Tasa de interés:", self.tasa_interes)
        return self

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
            return self

    def generar_interes(self):
        if self.balance > 0:
            interes_generado = self.balance * self.tasa_interes
            self.balance += interes_generado
            return self
        
    @classmethod
    def imprimir_todas_las_cuentas(cls):
        for cuenta in cls.cuentas:         #"cuenta" es una variable que representa a cada instancia de la clase CuentaBancaria que esta guardada en la lista cls.cuentas.
            print("Cuenta Bancaria:")
            cuenta.mostrar_info_cuenta()
            print("Tasa de interés:", cuenta.tasa_interes)
            print("------------------------")


account = CuentaBancaria(0.01).mostrar_info_cuenta().deposito(200).deposito(200).deposito(100).retiro(600).generar_interes().mostrar_info_cuenta()

second_account = CuentaBancaria(0.01).mostrar_info_cuenta().deposito(1000).deposito(1000).retiro(100).retiro(100).retiro(100).retiro(100).generar_interes().mostrar_info_cuenta()

CuentaBancaria.imprimir_todas_las_cuentas()
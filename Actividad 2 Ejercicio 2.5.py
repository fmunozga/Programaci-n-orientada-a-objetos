class CuentaBancaria:
    def __init__(self, nombres, apellidos, numero_cuenta, tipo_cuenta):
        self.nombres = nombres
        self.apellidos = apellidos
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0

    def imprimir_datos(self):
        print(f"\nNombre del titular: {self.nombres} {self.apellidos}")
        print(f"cuenta: {self.numero_cuenta}")
        print(f"Tipo de cuenta: {self.tipo_cuenta}")
        print(f"Saldo: ${self.saldo}")

    def consignar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Consignación exitosa")
        else:
            print("Valor inválido")

    def retirar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print("Retiro exitoso.")
        else:
            print("Saldo insuficiente")


print("Bienvenido al sistema de creación de cuenta bancaria")
nombre1 = input("Ingrese nombre: ")
apellido1 = input("Ingrese apellido: ")
numero1 = input("Ingrese número de cuenta: ")
tipo1 = input("Tipo Ahorro o Corriente: ")

mi_cuenta = CuentaBancaria(nombre1, apellido1, numero1, tipo1)

continuar = True
while continuar:
    mi_cuenta.imprimir_datos()
    opcion = input("\n¿Desea consignar, retiar o salir?: ").upper()
    
    if opcion == "CONSIGNAR":
        monto = float(input("Dinero a consignar: "))
        mi_cuenta.consignar(monto)
    elif opcion == "RETIRAR":
        monto = float(input("Dinero a retirar: "))
        mi_cuenta.retirar(monto)
    elif opcion == "SALIR":
        continuar = False
        print("Gracias por usar el sistema.")

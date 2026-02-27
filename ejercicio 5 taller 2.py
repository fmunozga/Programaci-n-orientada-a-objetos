def atributos():
    b = str(input("Ingrese el nombre del titular: "))
    c = str(input("Ingrese apellido del titular: "))
    d = int(input("Ingrese numero de cuenta: "))
    
    
    return  b,c,d

def tcuenta():
    g = 1
    while g == 1: 
        f = str(input("Ingrese el tipo de cuenta que deseas, Ahorro o Corriente: "))
        f = f.upper()
        if f == "AHORRO" or f == "CORRIENTE":
            g = 0
        else:
            print("por favor digite, Ahorro o Corriente")
    
    
    
    return f

def dinero(a,b):
    C = 0
    if b == "CONSIGNAR":
        c = float(input(f"¿Cuanto dinero desea consignar?: "))
        a = a + c
    elif b == "RETIRAR":
        g = 1
        while g == 1:
            c = float(input(f"¿Cuanto dinero desea retirar?: "))
            if c > a or c < 0:
                print("ingrese un valor positivo menor a su saldo total")
            else:
                a = a - c
                g = 0
    return a 
            
        



a = 1
saldo = 0

print("bienvenido al sistema de creacion de cuenta bancaria")

nombre, apellido, ncuenta = atributos()
tipocuenta = tcuenta()

print(f"su informacion de cuenta es:\nNombre del titular: {nombre} {apellido}\nSu tipo de cuenta es:{tipocuenta}")

while a == 1:
    print(f"su saldo es:{saldo}$")
    b = str(input("¿Desea consignar o retirar?: ")).upper()
    saldo = dinero(saldo,b)
    print(f"su saldo se acctualizo a:{saldo}$")
    c = str(input("¿Desea seguir con la operacion?: ")).upper()
    if c == "NO":
        a = 0
print(f"su informacion de cuenta es:\nNombre del titular: {nombre} {apellido}\nSu tipo de cuenta es:{tipocuenta}\nSu saldo es:{saldo}$\nGracias por elegirnos")

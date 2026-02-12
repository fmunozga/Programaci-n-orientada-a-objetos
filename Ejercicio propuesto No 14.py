def cuadrado (a):
    dos = a**2
    return dos 
def cubo (b):
    tres = b**3
    return tres

numero = float(input("ingrese un numero:"))
c = cuadrado(numero)
cc = cubo(numero)
print(f"el cuadrado de su numero es:{c}\nel cubo de su numero es:{cc}")

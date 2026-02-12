def area(a):
    A = a* 3.1416
    return A
def longitud (b):
    l = (b*2)*3.1416
    return l

radio= float(input("¿cual es el radio del circulo?:"))

Area = area(radio)
Longitud = longitud(radio)

print(f"el area del circulo es:{Area}\nla longitud del circulo es:{Longitud}")

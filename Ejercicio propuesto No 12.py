def salariob(a, b):
    bruto = a * b
    return bruto
def descuento (c):
    dretenido = salariob(horas, salario)*c
    return dretenido
def total ():
    totall= salariob(horas, salario) - descuento(retencion)
    return totall
    

horas = 48
salario = 5000
retencion = 0.125

q = salariob(horas, salario)
w = int(descuento(retencion))
r = int(total())
print(f"El salario bruto fue de ${q}\nLa retencion de la fuente fue de ${w}\nEl salario neto fue de ${r}")

def su(a,b,d):
    if b == 20:
        summ = a + b 
    else:
        summ = a + (b/d)
    return summ


def equis(c,d):
    eq = c +(d**2)
    return eq


suma= 0
x = 20
y = 40

suma = su(suma,x,y)
x = equis(x,y)
suma = su(suma,x,y)

print(f"el valor de la suma es:{suma}")

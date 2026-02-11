def edalber(a):
    alber = a*(2/3)
    return alber
    
def edana(b):
    ana = b*(4/3)
    return ana 
    
def edmama(c,d,e):
    mama = c + d + e
    return mama


edjuan = 9

print("la edad de mamá es",int(edmama(edalber(edjuan),edana(edjuan),edjuan)))
print("la edad de alber es", int(edalber(edjuan)))
print("la edad de ana es",int(edana(edjuan)))
print("la edad de juan es",int(edjuan))
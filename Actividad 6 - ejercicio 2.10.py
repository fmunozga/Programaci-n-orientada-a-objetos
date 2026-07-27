class Restaurante:
    def pedido(self, primerplato, cprimerplato, bebida, cbebida, segundoplato=None, csegundoplato=0.0, postre=None, cpostre=0.0):
        if segundoplato is not None and postre is not None:
            total = cprimerplato + csegundoplato + cbebida + cpostre
            print(f"El costo de {primerplato} + {segundoplato} + {bebida} + {postre} es = ${total}")
        elif segundoplato is not None:
            total = cprimerplato + csegundoplato + cbebida
            print(f"El costo de {primerplato} + {segundoplato} + {bebida} es = ${total}")
        else:
            total = cprimerplato + cbebida
            print(f"El costo de {primerplato} y {bebida} es = ${total}")

    def usuario(self):
        print("Bienvenido al restaurante\nQue desea ordenar?\n1)Primer plato y bebida\n2)Un primer plato, un segundo plato y una bebida\n3)Un primer plato, un segundo plato, una bebida y un postre.")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            primerplato = input("Ingrese el primer plato: ")
            cprimerplato = float(input("Ingrese el costo del primer plato: "))
            bebida = input("Ingrese la bebida: ")
            cbebida = float(input("Ingrese el costo de la bebida: "))
            self.pedido(primerplato, cprimerplato, bebida, cbebida)

        elif opcion == 2:
            primerplato = input("Ingrese el primer plato: ")
            cprimerplato = float(input("Ingrese el costo del primer plato: "))
            segundoplato = input("Ingrese el segundo plato: ")
            csegundoplato = float(input("Ingrese el costo del segundo plato: "))
            bebida = input("Ingrese la bebida: ")
            cbebida = float(input("Ingrese el costo de la bebida: "))
            # Usamos argumentos con nombre (keywords) para evitar confusiones de orden:
            self.pedido(primerplato, cprimerplato, bebida, cbebida, segundoplato=segundoplato, csegundoplato=csegundoplato)

        elif opcion == 3:
            primerplato = input("Ingrese el primer plato: ")
            cprimerplato = float(input("Ingrese el costo del primer plato: "))
            segundoplato = input("Ingrese el segundo plato: ")
            csegundoplato = float(input("Ingrese el costo del segundo plato: "))
            bebida = input("Ingrese la bebida: ")
            cbebida = float(input("Ingrese el costo de la bebida: "))
            postre = input("Ingrese el postre: ")
            cpostre = float(input("Ingrese el costo del postre: "))
            self.pedido(primerplato, cprimerplato, bebida, cbebida, segundoplato=segundoplato, csegundoplato=csegundoplato, postre=postre, cpostre=cpostre)


restaurante = Restaurante()
restaurante.usuario()

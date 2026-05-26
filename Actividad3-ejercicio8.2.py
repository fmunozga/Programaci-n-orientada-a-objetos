from tkinter import *
from tkinter import messagebox

class AppNotas:
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Notas")
        self.ventana.config(bg = "steel blue")

        self.p = 0
        self.n1 = StringVar()
        self.n2 = StringVar()
        self.n3 = StringVar()
        self.n4 = StringVar()
        self.n5 = StringVar()
        self.descuento = StringVar()
        self.desviacion = StringVar()
        self.nmayores = StringVar()
        self.nmenores = StringVar()

        
        self.Nota1 = Label(self.ventana)
        self.Nota1.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.Nota1.config(text = "Nota 1 :", bg = "lightblue")

        self.Nota1entrada = Entry(self.ventana)
        self.Nota1entrada.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.Nota1entrada.config(justify = "center", textvariable = self.n1)

        
        self.Nota2 = Label(self.ventana)
        self.Nota2.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.Nota2.config(text = "Nota 2 :", bg = "lightblue")

        self.Nota2entrada = Entry(self.ventana)
        self.Nota2entrada.grid(row = 1, column = 1, padx = 10, pady = 10)
        self.Nota2entrada.config(justify = "center", textvariable = self.n2)

        
        self.Nota3 = Label(self.ventana)
        self.Nota3.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.Nota3.config(text = "Nota 3 :", bg = "lightblue")

        self.Nota3entrada = Entry(self.ventana)
        self.Nota3entrada.grid(row = 2, column = 1, padx = 10, pady = 10)
        self.Nota3entrada.config(justify = "center", textvariable = self.n3)

        
        self.Nota4 = Label(self.ventana)
        self.Nota4.grid(row = 3, column = 0, padx = 10, pady = 10)
        self.Nota4.config(text = "Nota 4 :", bg = "lightblue")

        self.Nota4entrada = Entry(self.ventana)
        self.Nota4entrada.grid(row = 3, column = 1, padx = 10, pady = 10)
        self.Nota4entrada.config(justify = "center", textvariable = self.n4)

        
        self.Nota5 = Label(self.ventana)
        self.Nota5.grid(row = 4, column = 0, padx = 10, pady = 10)
        self.Nota5.config(text = "Nota 5 :", bg = "lightblue")

        self.Nota5entrada = Entry(self.ventana)
        self.Nota5entrada.grid(row = 4, column = 1, padx = 10, pady = 10)
        self.Nota5entrada.config(justify = "center", textvariable = self.n5)

    
        self.promedio1 = Label(self.ventana)
        self.promedio1.grid(row = 6, column = 0, padx = 10, pady = 10)
        self.promedio1.config(text = "promedio : " , bg = "lightblue")

        self.promedio = Label(self.ventana)
        self.promedio.grid(row = 6, column = 1, padx = 10, pady = 10)
        self.promedio.config(textvariable = self.descuento , bg = "lightblue")

        
        self.Destandar1 = Label(self.ventana)
        self.Destandar1.grid(row = 7, column = 0, padx = 10, pady = 10)
        self.Destandar1.config(text = "Desviación estándar  : " , bg = "lightblue")

        self.destandar= Label(self.ventana)
        self.destandar.grid(row = 7, column = 1, padx = 10, pady = 10)
        self.destandar.config(textvariable = self.desviacion , bg = "lightblue")

        
        self.vmayor1 = Label(self.ventana)
        self.vmayor1.grid(row = 8, column = 0, padx = 10, pady = 10)
        self.vmayor1.config(text = "Valor mayor : " , bg = "lightblue")

        self.vmayor = Label(self.ventana)
        self.vmayor.grid(row = 8, column = 1, padx = 10, pady = 10)
        self.vmayor.config(textvariable = self.nmayores , bg = "lightblue")

        
        self.vmenor1 = Label(self.ventana)
        self.vmenor1.grid(row = 9, column = 0, padx = 10, pady = 10)
        self.vmenor1.config(text = "Valor menor : " , bg = "lightblue")

        self.vmenor = Label(self.ventana)
        self.vmenor.grid(row = 9, column = 1, padx = 10, pady = 10)
        self.vmenor.config(textvariable = self.nmenores , bg = "lightblue")

        
        
        self.botoncalcular = Button(self.ventana)
        self.botoncalcular.config(text = "calcular", width = 10, command = self.maestro )
        self.botoncalcular.grid(row = 5, column = 0, padx = 10, pady = 10)

        self.botonlimpiar = Button(self.ventana)
        self.botonlimpiar.config(text = "limpiar", width = 10, command = self.limpiarv)
        self.botonlimpiar.grid(row = 5, column = 1, padx = 10, pady = 10)


    

    def calpromedio(self):
        num1 = float(self.n1.get())
        num2 = float(self.n2.get())
        num3 = float(self.n3.get())
        num4 = float(self.n4.get())
        num5 = float(self.n5.get())

        resultado = (num1 + num2 + num3 + num4+ num5)/5
        self.descuento.set(resultado)
        return resultado

    def limpiarv(self):
        self.n1.set("")
        self.n2.set("")
        self.n3.set("")
        self.n4.set("")
        self.n5.set("")
        
        self.descuento.set("")
        self.desviacion.set("")
        self.nmayores.set("")
        self.nmenores.set("")

    def DesviacionEstandar(self):
        p = self.calpromedio()
        num1 = (float(self.n1.get())- p)**2
        num2 = (float(self.n2.get())- p)**2
        num3 = (float(self.n3.get())- p)**2
        num4 = (float(self.n4.get())- p)**2
        num5 = (float(self.n5.get())- p)**2

        resultado = round(((num1 + num2 + num3 + num4+ num5)/5)**0.5,2)
        self.desviacion.set(resultado)

    def mayores(self):
        num1 = float(self.n1.get())
        num2 = float(self.n2.get())
        num3 = float(self.n3.get())
        num4 = float(self.n4.get())
        num5 = float(self.n5.get())

        notas = [num1,num2,num3,num4,num5]
        notas.sort(reverse=True)
        notamayor = notas[0]
        self.nmayores.set(notamayor)
        
    def menores(self):
        num1 = float(self.n1.get())
        num2 = float(self.n2.get())
        num3 = float(self.n3.get())
        num4 = float(self.n4.get())
        num5 = float(self.n5.get())

        notas = [num1,num2,num3,num4,num5]
        notas.sort()
        notamenor = notas[0]
        self.nmenores.set(notamenor)

    
    def maestro(self):
        try:
            self.DesviacionEstandar()
            self.calpromedio()
            self.mayores()
            self.menores()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa todas las notas con números válidos.")



ventana_raiz = Tk()
mi_programa = AppNotas(ventana_raiz)
ventana_raiz.mainloop()

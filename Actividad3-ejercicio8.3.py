from tkinter import *
from tkinter import messagebox

class AppFiguras:

    def __init__(self, ventana_principal):
        self.ventana = ventana_principal
        self.ventana.title("figuras")
        self.ventana.config(bg = "steel blue")

        
        self.n1 = 0
        self.n2 = 0

        
        self.boton_cilindro = Button(self.ventana)
        self.boton_cilindro.config(text = "Cilindro", width = 10, command = self.ventanacilindro)
        self.boton_cilindro.grid(row = 0, column = 0, padx = 10, pady = 10)

        self.boton_esfera = Button(self.ventana)
        self.boton_esfera.config(text = "Esfera", width = 10, command = self.ventanaEsfera)
        self.boton_esfera.grid(row = 0, column = 1, padx = 10, pady = 10)

        self.boton_piramide = Button(self.ventana)
        self.boton_piramide.config(text = "Piramide", width = 10, command = self.ventanaPiramide)
        self.boton_piramide.grid(row = 0, column = 3, padx = 10, pady = 10)

    

    def ventanacilindro(self):
        
        vencilindro = Toplevel(self.ventana)
        vencilindro.title("Cilindro")
        vencilindro.config(bg = "steel blue")

        n1 = StringVar()
        n2 = StringVar()
        Volumen = StringVar()
        Superficie = StringVar()

        radio1 = Label(vencilindro)
        radio1.grid(row = 0, column = 0, padx = 10, pady = 10)
        radio1.config(text = "Radio (cms): " , bg = "lightblue")

        radioentrada = Entry(vencilindro)
        radioentrada.grid(row = 0, column = 1, padx = 10, pady = 10)
        radioentrada.config(justify = "center", textvariable = n1)

        radio2 = Label(vencilindro)
        radio2.grid(row = 1, column = 0, padx = 10, pady = 10)
        radio2.config(text = "Altura (cms): " , bg = "lightblue")

        radio2entrada = Entry(vencilindro)
        radio2entrada.grid(row = 1, column = 1, padx = 10, pady = 10)
        radio2entrada.config(justify = "center", textvariable = n2)

        botoncalcular = Button(vencilindro)
       
        botoncalcular.config(text = "calcular", width = 10, command = lambda: self.Cvolumen(n1, n2, Volumen, Superficie))
        botoncalcular.grid(row = 2, column = 1, padx = 10, pady = 10)

        volumen1 = Label(vencilindro)
        volumen1.grid(row = 3, column = 0, padx = 10, pady = 10)
        volumen1.config(text = " Volumen (cm3): " , bg = "lightblue")

        volumen = Label(vencilindro)
        volumen.grid(row = 3, column = 1, padx = 10, pady = 10)
        volumen.config(textvariable = Volumen , bg = "lightblue")

        superficie1 = Label(vencilindro)
        superficie1.grid(row = 4, column = 0, padx = 10, pady = 10)
        superficie1.config(text = "superficie (cm2) : " , bg = "lightblue")

        superficie = Label(vencilindro)
        superficie.grid(row = 4, column = 1, padx = 10, pady = 10)
        superficie.config(textvariable = Superficie , bg = "lightblue")

    def Cvolumen(self, a, b, c, d):
        try:
            num1 = float(a.get())
            num2 = float(b.get())

            volumen = (num1 ** 2)*num2*3.14
            superficie = 2*3.14*num1*(num1+num2)

            c.set(volumen)
            d.set(superficie)
        except ValueError:
            messagebox.showerror("Error", "Ingresa valores numéricos válidos.")

    def ventanaEsfera(self):
        vencilindro = Toplevel(self.ventana)
        vencilindro.title("Esfera")
        vencilindro.config(bg = "steel blue")

        n1 = StringVar()
        n2 = StringVar()
        Volumen = StringVar()
        Superficie = StringVar()

        radio1 = Label(vencilindro)
        radio1.grid(row = 0, column = 0, padx = 10, pady = 10)
        radio1.config(text = "Radio (cms): " , bg = "lightblue")

        radioentrada = Entry(vencilindro)
        radioentrada.grid(row = 0, column = 1, padx = 10, pady = 10)
        radioentrada.config(justify = "center", textvariable = n1)

        botoncalcular = Button(vencilindro)
        botoncalcular.config(text = "calcular", width = 10, command = lambda: self.Esfera(n1, Volumen, Superficie))
        botoncalcular.grid(row = 2, column = 1, padx = 10, pady = 10)

        volumen1 = Label(vencilindro)
        volumen1.grid(row = 3, column = 0, padx = 10, pady = 10)
        volumen1.config(text = " Volumen (cm3): " , bg = "lightblue")

        volumen = Label(vencilindro)
        volumen.grid(row = 3, column = 1, padx = 10, pady = 10)
        volumen.config(textvariable = Volumen , bg = "lightblue")

        superficie1 = Label(vencilindro)
        superficie1.grid(row = 4, column = 0, padx = 10, pady = 10)
        superficie1.config(text = "superficie (cm2) : " , bg = "lightblue")

        superficie = Label(vencilindro)
        superficie.grid(row = 4, column = 1, padx = 10, pady = 10)
        superficie.config(textvariable = Superficie , bg = "lightblue")

    def Esfera(self, a, b, c):
        try:
            num1 = float(a.get())

            volumen = (4/3)*3.14*(num1**3)
            superficie = 4*3.14*(num1**2)
            b.set(volumen)
            c.set(superficie)
        except ValueError:
            messagebox.showerror("Error", "Ingresa valores numéricos válidos.")

    def ventanaPiramide(self):
        vencilindro = Toplevel(self.ventana)
        vencilindro.title("Pirámide") 
        vencilindro.config(bg = "steel blue")

        n1 = StringVar()
        n2 = StringVar()
        n3 = StringVar()
        Volumen = StringVar()
        Superficie = StringVar()

        radio1 = Label(vencilindro)
        radio1.grid(row = 0, column = 0, padx = 10, pady = 10)
        radio1.config(text = "Base (cms): " , bg = "lightblue")

        radioentrada = Entry(vencilindro)
        radioentrada.grid(row = 0, column = 1, padx = 10, pady = 10)
        radioentrada.config(justify = "center", textvariable = n1)

        radio2 = Label(vencilindro)
        radio2.grid(row = 1, column = 0, padx = 10, pady = 10)
        radio2.config(text = "Altura (cms): " , bg = "lightblue")

        radio2entrada = Entry(vencilindro)
        radio2entrada.grid(row = 1, column = 1, padx = 10, pady = 10)
        radio2entrada.config(justify = "center", textvariable = n2)

        apotema1 = Label(vencilindro)
        apotema1.grid(row = 2, column = 0, padx = 10, pady = 10)
        apotema1.config(text = "Apotema (cms): " , bg = "lightblue")

        apotema1entrada = Entry(vencilindro)
        apotema1entrada.grid(row = 2, column = 1, padx = 10, pady = 10)
        apotema1entrada.config(justify = "center", textvariable = n3)

        botoncalcular = Button(vencilindro)
        botoncalcular.config(text = "calcular", width = 10, command = lambda: self.Piramide(n1, n2, n3, Volumen, Superficie))
        botoncalcular.grid(row = 3, column = 1, padx = 10, pady = 10)

        volumen1 = Label(vencilindro)
        volumen1.grid(row = 4, column = 0, padx = 10, pady = 10)
        volumen1.config(text = " Volumen (cm3): " , bg = "lightblue")

        volumen = Label(vencilindro)
        volumen.grid(row = 4, column = 1, padx = 10, pady = 10)
        volumen.config(textvariable = Volumen , bg = "lightblue")

        superficie1 = Label(vencilindro)
        superficie1.grid(row = 5, column = 0, padx = 10, pady = 10)
        superficie1.config(text = "superficie (cm2) : " , bg = "lightblue")

        superficie = Label(vencilindro)
        superficie.grid(row = 5, column = 1, padx = 10, pady = 10)
        superficie.config(textvariable = Superficie , bg = "lightblue")

    def Piramide(self, a, b, c, d, f):
        try:
            num1 = float(a.get())
            num2 = float(b.get())
            num3 = float(c.get())

            volumen = (num1*num2)/3
            superficie = (num1*num3)/2

            d.set(volumen)
            f.set(superficie)
        except ValueError:
            messagebox.showerror("Error", "Ingresa valores numéricos válidos.")


ventana = Tk()
mi_app = AppFiguras(ventana)
ventana.mainloop()

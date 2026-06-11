from tkinter import *
from tkinter import messagebox

class Lector:
    def __init__(self, ventana):
        
        self.ventana = ventana
        self.ventana.title("Leer Texto")
        self.ventana.config(bg = "steel blue")

        
        self.n1 = StringVar()
        self.texto = StringVar()
        
        self.nombre = Label(self.ventana)
        self.nombre.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.nombre.config(text = "Nombre del archivo :", bg = "lightblue")

        self.Nota1entrada = Entry(self.ventana)
        self.Nota1entrada.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.Nota1entrada.config(justify = "center", textvariable = self.n1)

        self.botoncalcular = Button(self.ventana, text="Buscar y leer texto", width=18, command=self.buscar)
        self.botoncalcular.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

        self.stext = Label(self.ventana)
        self.stext.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.stext.config(text = "Su texto es :", bg = "lightblue")

        self.text = Text(self.ventana, width=40, height=10, wrap=WORD)
        self.text.grid(row=2, column=1, padx=10, pady=10)
        self.text.config(state=DISABLED) 

    def buscar(self):
       
        nom = self.n1.get()
        with open(nom, "r") as f:
            contenido = f.read()
        
        self.text.config(state=NORMAL)       
        self.text.delete("1.0", END)         
        self.text.insert(END, contenido)     
        self.text.config(state=DISABLED)


if __name__ == "__main__":
    root = Tk()
    app = Lector(root)
    root.mainloop()

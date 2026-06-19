import tkinter as tk
from tkinter import messagebox
import math


class CalculosNumericos:

    @staticmethod
    def calcular_logaritmo_neperiano(valor):
        try:
            if valor <= 0:
                raise ArithmeticError()

            resultado = math.log(valor)
            return f"Logaritmo: {resultado}"

        except ArithmeticError:
            return "Error: El valor debe ser positivo para el logaritmo"
        except ValueError:
            return "Error: Debe ingresar un número válido"

    @staticmethod
    def calcular_raiz_cuadrada(valor):
        try:
            if valor < 0:
                raise ArithmeticError()

            resultado = math.sqrt(valor)
            return f"Raíz cuadrada: {resultado}"

        except ArithmeticError:
            return "Error: El valor debe ser positivo para la raíz"
        except ValueError:
            return "Error: Debe ingresar un número válido"


def calcular():
    try:
        valor = float(entrada.get())

        resultado1 = CalculosNumericos.calcular_logaritmo_neperiano(valor)
        resultado2 = CalculosNumericos.calcular_raiz_cuadrada(valor)

        resultado_label.config(text=resultado1 + "\n" + resultado2)

    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido")


ventana = tk.Tk()
ventana.title("Cálculos Numéricos")
ventana.geometry("350x200")

label = tk.Label(ventana, text="Ingrese un valor:")
label.pack(pady=10)

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Calcular", command=calcular)
boton.pack(pady=10)

resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

ventana.mainloop()

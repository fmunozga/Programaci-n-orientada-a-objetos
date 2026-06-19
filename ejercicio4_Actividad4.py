import tkinter as tk
from tkinter import messagebox


class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos


class EquipoMaratonProgramacion:
    def __init__(self, nombre_equipo, universidad, lenguaje):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje = lenguaje
        self.programadores = []
        self.tamano_max = 3

    def esta_lleno(self):
        return len(self.programadores) == self.tamano_max

    def anadir(self, programador):
        if self.esta_lleno():
            raise Exception("El equipo está completo (máximo 3).")
        self.programadores.append(programador)

    @staticmethod
    def validar_campo(campo):
        if len(campo) == 0:
            raise Exception("El campo no puede estar vacío")

        if len(campo) > 20:
            raise Exception("Máximo 20 caracteres")

        for c in campo:
            if c.isdigit():
                raise Exception("No se permiten números")



equipo = None


def crear_equipo():
    global equipo
    try:
        nombre = entrada_nombre_equipo.get()
        universidad = entrada_universidad.get()
        lenguaje = entrada_lenguaje.get()

        if not nombre or not universidad or not lenguaje:
            raise Exception("Todos los campos del equipo son obligatorios")

        equipo = EquipoMaratonProgramacion(nombre, universidad, lenguaje)

        messagebox.showinfo("Éxito", "Equipo creado correctamente")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def agregar_programador():
    try:
        if equipo is None:
            raise Exception("Primero debes crear el equipo")

        nombre = entrada_nombre_prog.get()
        apellidos = entrada_apellidos_prog.get()

        EquipoMaratonProgramacion.validar_campo(nombre)
        EquipoMaratonProgramacion.validar_campo(apellidos)

        programador = Programador(nombre, apellidos)
        equipo.anadir(programador)

        resultado_label.config(
            text=f"Programadores: {len(equipo.programadores)} / 3"
        )

        messagebox.showinfo("Éxito", "Programador agregado")

    except Exception as e:
        messagebox.showerror("Error", str(e))


ventana = tk.Tk()
ventana.title("Equipo Maratón Programación")
ventana.geometry("400x400")

tk.Label(ventana, text="Nombre del equipo").pack()
entrada_nombre_equipo = tk.Entry(ventana)
entrada_nombre_equipo.pack()

tk.Label(ventana, text="Universidad").pack()
entrada_universidad = tk.Entry(ventana)
entrada_universidad.pack()

tk.Label(ventana, text="Lenguaje").pack()
entrada_lenguaje = tk.Entry(ventana)
entrada_lenguaje.pack()

tk.Button(ventana, text="Crear Equipo", command=crear_equipo).pack(pady=10)

tk.Label(ventana, text="Nombre programador").pack()
entrada_nombre_prog = tk.Entry(ventana)
entrada_nombre_prog.pack()

tk.Label(ventana, text="Apellidos programador").pack()
entrada_apellidos_prog = tk.Entry(ventana)
entrada_apellidos_prog.pack()

tk.Button(ventana, text="Agregar Programador", command=agregar_programador).pack(pady=10)

resultado_label = tk.Label(ventana, text="Programadores: 0 / 3")
resultado_label.pack()

ventana.mainloop()


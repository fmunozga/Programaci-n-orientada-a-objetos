import tkinter as tk
from tkinter import messagebox
import os    

class ContactoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD Contactos")

        self.file_name = "friendsContact.txt"

        tk.Label(root, text="Nombre").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(root, text="Número").grid(row=1, column=0, padx=5, pady=5)

        self.entry_name = tk.Entry(root)
        self.entry_number = tk.Entry(root)

        self.entry_name.grid(row=0, column=1, padx=5, pady=5)
        self.entry_number.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(root, text="Create", command=self.create, width=10).grid(row=2, column=0, pady=5)
        tk.Button(root, text="Read", command=self.read, width=10).grid(row=2, column=1, pady=5)
        tk.Button(root, text="Update", command=self.update, width=10).grid(row=3, column=0, pady=5)
        tk.Button(root, text="Delete", command=self.delete, width=10).grid(row=3, column=1, pady=5)

        self.text_area = tk.Text(root, width=40, height=10)
        self.text_area.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        try:
            if not os.path.exists(self.file_name):
                with open(self.file_name, "w") as file:
                    pass
        except IOError as e:
            messagebox.showerror("Error de Inicialización", f"No se pudo crear el archivo:\n{e}")

    def create(self):
        name = self.entry_name.get().strip()
        number = self.entry_number.get().strip()

        # 1. Validación: campos vacíos
        if not name or not number:
            messagebox.showwarning("Campos vacíos", "Por favor, llena tanto el nombre como el número.")
            return

        # 2. NUEVA VALIDACIÓN: Solo números en el campo teléfono
        if not number.isdigit():
            messagebox.showwarning("Formato incorrecto", "El número de contacto solo debe contener dígitos numéricos.")
            return

        # 3. Validación: evitar el caracter separador
        if "!" in name:
            messagebox.showwarning("Carácter inválido", "El carácter '!' no está permitido en el nombre.")
            return

        found = False

        try:
            with open(self.file_name, "r") as file:
                for line in file:
                    if not line.strip():
                        continue
                    data = line.strip().split("!")
                    if len(data) >= 2 and (data[0] == name or data[1] == number):
                        found = True
                        break

            if not found:
                with open(self.file_name, "a") as file:
                    file.write(f"{name}!{number}\n")
                messagebox.showinfo("Resultado", "Contacto añadido con éxito.")
                self.clear_entries()
            else:
                messagebox.showwarning("Resultado", "El nombre o el número ya existen.")
        
        except IOError as e:
            messagebox.showerror("Error de Archivo", f"No se pudo guardar el contacto:\n{e}")

    def read(self):
        self.text_area.delete(1.0, tk.END)

        try:
            with open(self.file_name, "r") as file:
                has_contacts = False
                for line in file:
                    if not line.strip():
                        continue
                    
                    try:
                        name, number = line.strip().split("!")
                        self.text_area.insert(tk.END, f"Friend Name: {name}\nContact Number: {number}\n\n")
                        has_contacts = True
                    except ValueError:
                        continue
                
                if not has_contacts:
                    self.text_area.insert(tk.END, "No hay contactos guardados.")
                    
        except IOError as e:
            messagebox.showerror("Error de Lectura", f"Error al leer el archivo:\n{e}")

    def update(self):
        new_name = self.entry_name.get().strip()
        new_number = self.entry_number.get().strip()

        if not new_name or not new_number:
            messagebox.showwarning("Campos vacíos", "Necesitas el nombre para buscar y el nuevo número.")
            return

        # NUEVA VALIDACIÓN: Solo números al actualizar
        if not new_number.isdigit():
            messagebox.showwarning("Formato incorrecto", "El nuevo número de contacto solo debe contener dígitos numéricos.")
            return

        found = False
        lines = []

        try:
            with open(self.file_name, "r") as file:
                for line in file:
                    if not line.strip():
                        continue
                    data = line.strip().split("!")
                    if len(data) >= 2 and data[0] == new_name:
                        lines.append(f"{new_name}!{new_number}\n")
                        found = True
                    else:
                        lines.append(line)

            if found:
                with open(self.file_name, "w") as file:
                    file.writelines(lines)
                messagebox.showinfo("Resultado", "Contacto actualizado.")
                self.clear_entries()
            else:
                messagebox.showwarning("Resultado", "El nombre ingresado no existe.")
                
        except IOError as e:
            messagebox.showerror("Error", f"Error al procesar la actualización:\n{e}")

    def delete(self):
        target_name = self.entry_name.get().strip()

        if not target_name:
            messagebox.showwarning("Campo vacío", "Ingresa el nombre del contacto que deseas eliminar.")
            return

        found = False
        lines = []

        try:
            with open(self.file_name, "r") as file:
                for line in file:
                    if not line.strip():
                        continue
                    data = line.strip().split("!")
                    if len(data) >= 2 and data[0] == target_name:
                        found = True
                    else:
                        lines.append(line)

            if found:
                with open(self.file_name, "w") as file:
                    file.writelines(lines)
                messagebox.showinfo("Resultado", "Contacto eliminado.")
                self.clear_entries()
            else:
                messagebox.showwarning("Resultado", "El nombre ingresado no existe.")
                
        except IOError as e:
            messagebox.showerror("Error", f"Error al intentar eliminar:\n{e}")

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_number.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactoApp(root)
    root.mainloop()

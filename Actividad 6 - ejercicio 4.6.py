class Profesor:
   def imprimir(self):
       print("Es un profesor.")

class ProfesorTitular(Profesor):
    def __init__(self, años=0):
        self.años = años
    def imprimir(self):
       print("Es un profesor titular.")
    def imprimir_años(self):
       print(f"Años = {self.años}")

if __name__ == "__main__":
    profesor1 = ProfesorTitular()
    profesor1.imprimir_años()

import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcularArea(self):
        return math.pi * math.pow(self.radio, 2)

    def calcularPerimetro(self):
        return 2 * math.pi * self.radio


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

    def calcularPerimetro(self):
        return (2 * self.base) + (2 * self.altura)


class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado * self.lado

    def calcularPerimetro(self):
        return 4 * self.lado


class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return (self.base * self.altura) / 2

    def calcularPerimetro(self):
        return self.base + self.altura + self.calcularHipotenusa()

    def calcularHipotenusa(self):
        return math.sqrt(self.base * self.base + self.altura * self.altura)

    def determinarTipoTriangulo(self):
        if (self.base == self.altura) and (self.base == self.calcularHipotenusa()) and (self.altura == self.calcularHipotenusa()):
            print("Es un triángulo equilátero")
        elif (self.base != self.altura) and (self.base != self.calcularHipotenusa()) and (self.altura != self.calcularHipotenusa()):
            print("Es un triángulo escaleno")
        else:
            print("Es un triángulo isósceles")


class PruebaFiguras:
    
    @staticmethod
    def main():
        radio = float(input("Radio del círculo: "))
        figura1 = Circulo(radio)
        
        base_rect = float(input("Base del rectángulo: "))
        altura_rect = float(input("Altura del rectángulo: "))
        figura2 = Rectangulo(base_rect, altura_rect)
        
        lado = float(input("Lado del cuadrado: "))
        figura3 = Cuadrado(lado)
        
        base_tri = float(input("Base del triángulo: "))
        altura_tri = float(input("Altura del triángulo: "))
        figura4 = TrianguloRectangulo(base_tri, altura_tri)
        
        print("El área del círculo es =", figura1.calcularArea())
        print("El perímetro del círculo es =", figura1.calcularPerimetro())
        print()
        
        print("El área del rectángulo es =", figura2.calcularArea())
        print("El perímetro del rectángulo es =", figura2.calcularPerimetro())
        print()
        
        print("El área del cuadrado es =", figura3.calcularArea())
        print("El perímetro del cuadrado es =", figura3.calcularPerimetro())
        print()
        
        print("El área del triángulo es =", figura4.calcularArea())
        print("El perímetro del triángulo es =", figura4.calcularPerimetro())
        
        figura4.determinarTipoTriangulo()
        
if __name__ == "__main__":
    PruebaFiguras.main()

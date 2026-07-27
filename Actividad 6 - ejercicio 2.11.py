class ArticuloCientifico:
    def __init__(self, titulo=None, autor=None, palabras_claves=None, publicacion=None, año=None, resumen=None):
        self.titulo = titulo
        self.autor = autor
        self.palabras_claves = palabras_claves if palabras_claves is not None else []
        self.publicacion = publicacion
        self.año = año
        self.resumen = resumen

    def imprimir(self):
        print("\nartículo científico:")
        print(f"Título: {self.titulo if self.titulo else ''}")
        print(f"Autor: {self.autor if self.autor else ''}")
        palabras_str = ", ".join(self.palabras_claves) if self.palabras_claves else ""
        print(f"Palabras Claves: {palabras_str}")
        print(f"Publicación: {self.publicacion if self.publicacion else ''}")
        print(f"Año: {self.año if self.año else ''}")
        print(f"Resumen: {self.resumen if self.resumen else ''}")

    def preguntar(self):
        self.titulo = input("Ingrese el título del artículo: ")
        self.autor = input("Ingrese el autor del artículo: ")
        palabras_input = input("Ingrese las palabras claves (separadas por comas): ")
        self.palabras_claves = [palabra.strip() for palabra in palabras_input.split(",")] if palabras_input else []
        self.publicacion = input("Ingrese la publicación (opcional): ") or None
        año_input = input("Ingrese el año de publicación (opcional): ")
        self.año = int(año_input) if año_input.isdigit() else None
        self.resumen = input("Ingrese el resumen (opcional): ") or None


if __name__ == "__main__":
    articulo = ArticuloCientifico()
    articulo.preguntar()
    articulo.imprimir()

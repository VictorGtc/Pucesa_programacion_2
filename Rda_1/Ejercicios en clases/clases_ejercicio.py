class Libro:
    def __init__(self, titulo, autor, anio, ):
        self.titulo=titulo
        self.autor=autor
        self.anio=anio
    def descripcion(self):
        return f"Nombre: {self.titulo} \n Autor: {self.autor}\n Anio: {self.anio}"
    
    
Libros=Libro("La Divina Comedia", "Dante Alighieri","1265-1321")
print(Libros.descripcion())

print("\n")

Libros=Libro("Orgullo y Prejuicio", "Jane Austen","1813")
print(Libros.descripcion())
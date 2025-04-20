class Estudiante:
    def __init__(self, nombre, carrera, nota_final):
        self.nombre=nombre
        self.correra=carrera
        self.nota_final=nota_final
    def datos_estu(self):
        return f"Nombre del o la estudiante: {self.nombre}\n Carre que esta cursando: {self.correra} \n Nota final: {self.nota_final}"
    def notas(self):
        if self.nota_final<7:
            print("La nota de es menor a 7 No aprueba :c")
        else:
            print("Aprobo con exito c: ")

estudiante1=Estudiante("Victor Toasa", "Ingenieria en Sistemas", 6)
print(estudiante1.datos_estu())
estudiante1.notas()

print("\n")

estudiante1=Estudiante("Juan Gabriel", "Medicina", 7)
print(estudiante1.datos_estu())
estudiante1.notas()

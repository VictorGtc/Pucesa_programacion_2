import time

class Incidente:
    def __init__(self,nombre,anio, tipo,id_estudiante):
        self.nombre=nombre
        self.anio=anio
        self.tipo=tipo
        self.id_estudiante=id_estudiante
        self.siguiente=None
        self.anterior=None
        

# Clase ListaBitacora
class ListaBitacora:
    def __init__(self):
        self.inicio = None
    def agregar_incidente(self,nombre,anio, tipo,id_estudiante):
        nodo_nuevo=Incidente(nombre, anio,tipo,id_estudiante)
        nodo_nuevo.siguiente=self.inicio
        self.inicio=nodo_nuevo

    def eliminar_incidente(self, nombre_buscar):
        actual=self.inicio
        while actual and actual.nombre !=nombre_buscar:
            actual=actual.siguiente
            
        if actual is None:
            print("La lista esta vacia, primeor ingrese valores :D")
            return
        if actual.anterior is None:
            self.inicio=actual.siguiente
            if self.inicio:
                self.inicio.anterior=None
        else:
            actual.anterior.siguiente=actual.siguiente
            if actual.siguiente:
                actual.siguiente.anterior=actual.anterior
        print(f"El reguistro del estudiante; {nombre_buscar} ha sido eliminado ")

    def buscar_incidente(self, nombre_encontrar):
        actual=self.inicio
        encontrado=False
        while actual:
            if actual.nombre==nombre_encontrar:
                print(f"""
                      Registro del estudiante buscado: 
                      Nombre del estudiante:{actual.nombre}
                      Año del del reguistro :{actual.anio}
                      Tipo de incidente: {actual.anio}
                      Id del estudiante: {actual.id_estudiante}
                      
                      """)
                encontrado=True
                break
            actual=actual.siguiente
        if not encontrado:
            print(f"El estudiante: {nombre_encontrar} no ha sido encontrado")
        

    def mostrar_incidentes(self):
        actual=self.inicio
        if self.inicio==None:
            print("La lista esta vacia, ingrese primero estudiantes")
            return
        
        while actual is not None:
            print("Los estudiantes que estan dentro de la lista para la evacuacion son los siguinetes: ")
            print(f"""
                  Nombre del estudiante: {actual.nombre}
                  ID del estudiante: {actual.id_estudiante}
                  Año del incidente: {actual.anio}
                  Tipo de incidente: {actual.tipo}
                  ----------------------------------------------
                  """)
            actual=actual.siguiente
            
            
cola_usar=ListaBitacora()
while True:
        print("""
========= MENÚ EVACUACION =========
1. Agregar incidente
2. Eliminar incidente 
3. Buscar indicente de los estudiantes 
4. Mostrar todos los incidentes
5. Salir """)
        
        opcion = input("Seleccione una opción: ").strip().lower()
        if opcion == "1":
            nombre_estudiante= input("Ingrese el nombre del estudiante: ")
            anio_incidente =input("Ingrese el año que sucedio el incidente: ")
            id_estudiante=input("Ingrese el id del estudiante: ")
            tipo_incidente=input("Ingrese el tipo de incidente que paso: ")
            cola_usar.agregar_incidente(nombre_estudiante,anio_incidente,tipo_incidente,id_estudiante)
        if opcion=="2":
            nombre_eliminar=input("Ingrese el nombre del estudiante que quiere eliminar: ").lower().strip()
            cola_usar.eliminar_incidente(nombre_eliminar)
        if opcion=="3":
            nombre_buscar=input("Ingrese el nombre del estudiante que quiero buscar: ")
            cola_usar.buscar_incidente(nombre_buscar)
        if opcion=="4":
            cola_usar.mostrar_incidentes()
        if opcion=="5":
            print("Saleindo.........")
            time.sleep(2)
            break
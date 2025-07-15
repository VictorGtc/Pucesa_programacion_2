""" COLAS PRINCIPIO FIFO"""

import time

class EstudianteEvacuacion:
    def __init__(self, nombre, aula, id_estudiante):
        self.nombre = nombre
        self.aula = aula
        self.id_estudiante=id_estudiante
        self.siguiente=None

class ColaDeAtencionSimple:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar(self, nombre, aula, id_estudiante):
        nuevo_nodo = EstudianteEvacuacion(nombre, aula, id_estudiante)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
    def avanzar(self):
        atendido=self.cabeza
        if self.cabeza is None:
            print("--- La cola está vacía. No hay nadie para atender. ---")
            return None
        while atendido is not None:
            print("Se simulara una evaciacion")
            print(f"""
                {time.sleep(1)}
                El estudiante: {atendido.nombre}
                Del Aula: {atendido.aula}
                Con su ID: {atendido.id_estudiante}
                {time.sleep(1)}
                Ha sido correctamente evacuados, continuando con los siguientes 
                """)
            
            atendido=atendido.siguiente

    def mostrar_en_espera(self):
        actual = self.cabeza
        if self.cabeza is None:
            print("La cola de atención está vacía.")
            return
        
        
        
        while actual is not None:
            print("Los estudiantes que estan en espera son los siquientes ")
            print(f"""
              
              El estudiante: {actual.nombre}
              Del Aula: {actual.aula}
              Con su ID: {actual.id_estudiante}
              ---------------------------------------
              """)
            actual=actual.siguiente
            
        

cola_usar=ColaDeAtencionSimple()

while True:
        print("""
========= MENÚ EVACUACION =========
1. Agregar Estudiantes 
2. Simular evacuacion
3. Mostrar los estudiantes, en esta simulacion
4. Sali""")
        opcion = input("Seleccione una opción: ").strip().lower()
        if opcion == "1":
            nombre_estudiante= input("Ingrese el nombre del estudiante: ")
            aula_estudiante=input("Ingrese el aula del estudiante: ")
            id_estudiante=input("Ingrese el id del estudiante: ")
            cola_usar.insertar(nombre_estudiante,aula_estudiante,id_estudiante)
        if opcion=="2":
            cola_usar.avanzar()
        if opcion=="3":
            cola_usar.mostrar_en_espera()
        if opcion=="4":
            print("Saleindo.........")
            time.sleep(2)
            break
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ColaDeAtencionSimple:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

        print(f"--> '{dato}' ha sido añadido a la cola.")

    def avanzar(self):
        if self.cabeza is None:
            print("--- La cola está vacía. No hay nadie para atender. ---")
            return None

        dato_atendido = self.cabeza.dato
        
        self.cabeza = self.cabeza.siguiente

        if self.cabeza is None:
            self.cola = None

        print(f"'{dato_atendido}' ha sido atendido y eliminado de la cola\n")
        return dato_atendido

    def mostrar(self):
        if self.cabeza is None:
            print("La cola de atención está vacía.")
            return

        print("\n--- Contenido actual de la cola ---")
        actual = self.cabeza
        posicion = 1
        while actual is not None:
            print(f"  {posicion}. {actual.dato}")
            actual = actual.siguiente
            posicion += 1
        print("------------------------------------")



print("=== INICIANDO SIMULACIÓN DE COLA DE ATENCIÓN (BANCO) ===")

mi_cola_banco = ColaDeAtencionSimple()

while True:
    print("""
========= MENÚ BANCO =========
1. Agregar nuevo cliente a la cola
2. Atender a todos los clientes
3. Mostrar clientes en espera
4. Recorrer la cola (hacia adelante)
5. Salir
""")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        cliente = input("Ingrese el nombre del cliente: ")
        mi_cola_banco.insertar(cliente)

    elif opcion == "2":
        print("Atendiendo a todos los clientes en la cola:")
        while not mi_cola_banco.esta_vacia():
            mi_cola_banco.avanzar()

    elif opcion == "3":
        mi_cola_banco.mostrar()

    elif opcion == "4":
        print("↪ Recorrido de la cola (hacia adelante):")
        mi_cola_banco.mostrar()

    elif opcion == "5":
        print("Fin de la simulación en el banco.")
        break

    else:
        print("Opción no válida. Intente de nuevo.")

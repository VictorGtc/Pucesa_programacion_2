from collections import deque
import time 
import random

print("Simulador de parque de diversiones")

cola_general=deque()
cola_prioritaria=deque()
lista_usarios_discapacitados=deque()
vagon=[]

def una_sola_lista():
    cola_general.extend(cola_prioritaria)
    cola_general.extend(lista_usarios_discapacitados)

def gurdar_nombres():
    nombre=input("Ingrese el nombre del usuario:\n")
    
    print("""Prioridades:
          1. Discapacitados
          2. Niños
          3. Ancianos
          4. Personas en general\n""")
    prioridad=int(input("Ingrese la prioridad de usuario:\n "))
    if prioridad==1: 
        lista_usarios_discapacitados.append((nombre,prioridad))
    if prioridad==2 or prioridad==3:
        cola_prioritaria.append((nombre,prioridad))
    elif prioridad==4:
        cola_general.append((nombre,prioridad))


def mostra_listas():
    print("""Cola prioritaria\n""")
    for i in cola_prioritaria:
        print("\nNombre: ",i)
    print("""Cola general\n""")
    for j in cola_general:
        print("\nNombre: ",j)
    print("""Cola discapasitados\n""")
    for m in lista_usarios_discapacitados:
        print("\nNombre: ",m)
        

def funcion_principal(turnos_totales):
    
    for i in range(turnos_totales):
        print(f"El turno nuermo {i+1} a comenzado ")
        for h in range(3):
            print(f"La vuelta {h} ha comenzado")
            print(f"""En el vagon los pasajeros son:\n""")
            for j in vagon:
                print(j)
        time.sleep(1)
            

def generar_ticket(nombre, prioridad, numero_viaje):

    tipo_acceso = ""
    if prioridad == 1:
        tipo_acceso = "Discapacidad"
    elif prioridad == 2:
        tipo_acceso = "Niño (Prioridad)"
    elif prioridad == 3:
        tipo_acceso = "Anciano (Prioridad)"
    elif prioridad == 4:
        tipo_acceso = "General"
    else:
        tipo_acceso = "Desconocido"

    print("\n--- ¡Ticket de Acceso K-Boom Park! ---")
    print(f"  Nombre del Visitante: {nombre}")
    print(f"  Tipo de Acceso: {tipo_acceso}")
    print(f"  Número de Viaje: {numero_viaje}")
    print(f"  Mensaje Especial: ¡Gracias por visitar K-Boom Park!")
    print("--------------------------------------\n")


def seleccionar_personas():
    cantidad_seleccionar=4
    viaje_actual=0
    for i in range(10):
        if len(cola_general)<4:
            print("""\n
                  Se termino el juego 
                  No hay suficintes jugadores\n""")
            break
        if len(cola_general) < cantidad_seleccionar:
            print(f"\n¡Atención! No hay suficientes usuarios ({len(cola_general)}) "
            f"para seleccionar {cantidad_seleccionar}. Se seleccionarán todos los disponibles.")
            tuplas_seleccionadas = list(cola_general)
        else:
            tuplas_seleccionadas=random.sample(cola_general,k=cantidad_seleccionar)
        for i in range(3):
            print("\n En el vagon se encuentras las siguientes personas\n")
            for tupla in tuplas_seleccionadas:
                print(tupla)
            time.sleep(1)
            print(f"Vuelta{i+1}/3")
        viaje_actual+=1
        for tupla_pasajero in tuplas_seleccionadas:
            nombre = tupla_pasajero[0]
            prioridad = tupla_pasajero[1]
            print(f"  - {nombre} (Prioridad: {prioridad})")
            generar_ticket(nombre, prioridad, viaje_actual)
        
        for tupla_a_borrar in tuplas_seleccionadas:
            try:
                cola_general.remove(tupla_a_borrar)
                print(f"  - Borrado: {tupla_a_borrar}")
            except ValueError:
                print(f"  - Advertencia: {tupla_a_borrar} no se encontró en cola_general para borrar.")
        print("\nEstado de cola_general después de borrar:")
        if cola_general:
            for tupla in cola_general:
                print(f"  - {tupla}")
        else:
            print("  (Cola general está vacía)")
            
    
    
while True: 
    print("""
        //Montaña rusa//\n
        1. Ingresar Jugadores
        2. Ver estatus de las colas 
        3. Simular viaje
        4. Salir del sistema
        """)
    try:
        opc=int(input("Ingrese la opcion que desaea realizar: "))
    except ValueError:
        print("Ingrese un valor correcto ")
        continue
    
    if opc==1: 
        gurdar_nombres()
    if opc==2: 
        mostra_listas()
    if opc==3:
        una_sola_lista()
        seleccionar_personas()
    if opc==4:
        print("Gracias por usar nuestro programa")
        break






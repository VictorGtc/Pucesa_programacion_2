from collections import deque
import random
import time 


print("Simulador de parque de diversiones")

cola_general=deque()
cola_prioritaria=deque()
lista_usarios_general=[]


def agregar_personas(nombre, prioridad=True):
    if prioridad:
        cola_prioritaria.append(nombre)
    else:
        cola_general.append(nombre)

def mostrar_colas():
    print("Cola prioritaria: ",cola_prioritaria)
    print("Cola generañ :", cola_general)

capacidad_vagon=4

def carga_vagon():
    pasajeros=[]
    while len(pasajeros)<=capacidad_vagon:
        if cola_prioritaria:
            pasajeros.append(cola_prioritaria.popleft())
        elif cola_general:
            pasajeros.append(cola_general.popleft())
        else:
            break
    return pasajeros

duracion_viaje=3

def simular_viaje(pasajeros,numero_vijes):
    
    print(f"Viaje numero: {numero_vijes} con: {pasajeros}")
    
    for i in range(duracion_viaje):
        print(f"Turno {i+1}/3")
        time.sleep(1)
        
    print("Viaje finalizado gracias por su visita :D")
    
def iniciar_simulacion(turnos_totales):
    viaje_num = 1 

    for turno in range(turnos_totales):
        print(f"--- Turno {turno+1}/{turnos_totales} ---")
        cantidad = random.randint(1, 3)
        for _ in range(cantidad):
            nombre = random.choice([lista_usarios_general])
            es_prioridad = random.random() < 0.3
            agregar_personas(nombre, es_prioridad)
        mostrar_colas()
        if len(cola_general) + len(cola_prioritaria) >= capacidad_vagon:
            pasajeros = carga_vagon()         
            simular_viaje(pasajeros, viaje_num)  
            viaje_num += 1                    
        else:
            print("Aún no hay suficientes personas para el viaje.")
            




def ingreso_de_datos(nombre,prioridad):
    
    lista_usarios_general.append((nombre,prioridad))
    
    
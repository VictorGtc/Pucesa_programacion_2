"""Visualización y Gestión de Calificaciones"""
import random
import matplotlib.pylab as plt
from  IPython.display import clear_output
import bisect
notas=random.sample(range(1,21),15)
print("📋 Notas originales:", notas)

def bubble_sort_viz(lista, mostrar_pasos=False, pausa=0.3):

    lista = lista.copy()

    comparaciones = 0
    intercambios = 0

    n = len(lista)
    
    pasos = []
    for i in range(n):
        
        for j in range(0, n - i - 1):
            
            comparaciones += 1
            
            if lista[j] > lista[j + 1]:
                
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                
                intercambios += 1
                
                pasos.append(lista.copy())
    return lista, comparaciones, intercambios, pasos


def animar_comparacion_sorted_bubble_simulada(lista_original, pausa=0.2):


    lista_bubble = lista_original.copy()


    lista_sorted_final = sorted(lista_original)


    pasos_bubble = [lista_bubble.copy()]


    pasos_sorted = []

    n = len(lista_bubble)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_bubble[j] > lista_bubble[j + 1]:
                lista_bubble[j], lista_bubble[j + 1] = lista_bubble[j + 1], lista_bubble[j]
                pasos_bubble.append(lista_bubble.copy())

    lista_simulada = lista_original.copy()
    for i in range(len(lista_sorted_final)):
        if lista_simulada[i] != lista_sorted_final[i]:
            lista_simulada[i] = lista_sorted_final[i]
        pasos_sorted.append(lista_simulada.copy())
    total_pasos = max(len(pasos_bubble), len(pasos_sorted))
    for k in range(total_pasos):
        clear_output(wait=True) 
        fig, axs = plt.subplots(1, 2, figsize=(12, 4))
        if k < len(pasos_bubble):
            axs[0].bar(range(len(pasos_bubble[k])), pasos_bubble[k], color='skyblue')
            axs[0].set_title(f"Bubble Sort - Paso {k+1}")
            axs[0].set_ylim(0, max(lista_original) + 5)
        else:
            axs[0].bar(range(len(pasos_bubble[-1])), pasos_bubble[-1], color='skyblue')
            axs[0].set_title("Bubble Sort - Final")
        if k < len(pasos_sorted):
            axs[1].bar(range(len(pasos_sorted[k])), pasos_sorted[k], color='lightgreen')
            axs[1].set_title(f"sorted() - Paso {k+1}")
            axs[1].set_ylim(0, max(lista_original) + 5)
        else:
            axs[1].bar(range(len(lista_sorted_final)), lista_sorted_final, color='lightgreen')
            axs[1].set_title("sorted() - Final")
        plt.tight_layout()
        plt.pause(pausa)
    plt.show()


bubble_sort_viz(notas)
animar_comparacion_sorted_bubble_simulada(notas)

try:
    nueva_nota = int(input("Ingrese la nota que desaea guardar "))  # puedes cambiar o pedir por input
except ValueError:
    print("Ingrese solo valores numericos")
bisect.insort(notas, nueva_nota)
print("✅ Lista después de insertar la nueva nota:", notas)

try:
    nota_buscar = int(input("Ingrese el numero a busar dentro de la lisra"))
except ValueError:
    print("Ingrese solo valores numericos")
posicion = bisect.bisect_left(notas, nota_buscar)
if posicion < len(notas) and notas[posicion] == nota_buscar:
    print(f"🔍 La nota {nota_buscar} se encuentra en la posición {posicion}")
else:
    print(f"❌ La nota {nota_buscar} no está en la lista.")
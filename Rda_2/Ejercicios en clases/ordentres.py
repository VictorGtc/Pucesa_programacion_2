lista_precios=[]


def selection_sort(lista):
    print("\nAlgoritmos de ordenamiento selection_sort")
    comparaciones=0
    intercambios=0
    
    lista_rango=len(lista)
    for i in range(lista_rango-1):
        indice_minimo=i
        for j in range(i+1,lista_rango):
            comparaciones+=1
            if lista[j]<lista[indice_minimo]:
                indice_minimo=j
        if indice_minimo!=i:
            lista[i],lista[indice_minimo]=lista[indice_minimo],lista[i]
            intercambios+=1
    print(f""" Las comparaciones hechas dentro de este tercer metodo de ordenamiento han sido {comparaciones}
          Mientras que los intercambios realizados han sido {intercambios}""")
    
    print("\n La lista ordenada es: ")
    return lista

while True:
    print("""\n //==Bienvenido a nuestro sistema de ordenamiento de precios==//""")
    rango_precio=int(input("Ingrese cuantos precios se va a ingresar: "))
    for i in range(rango_precio):
        precios_guardar=int(input(f"Ingrese el precio numero {i+1} : "))
        lista_precios.append(precios_guardar)
        
    print("Los precios seran ordenados en forma selection sort:\n")
    
    print(selection_sort(lista_precios))
    
    opc=input("Si desea realizar nuevamente otro ordenamiento de valores preciose enter o escriba salir si desea terminar: ").lower().strip()
    
    lista_precios=[]
    if opc=="salir":
        print("Gracias por usar nuestro codigo C:")
        break
    
#Bubble Sort, Insertion Sort y Selection Sort: Resumen
#Cómo Funcionan
#Bubble Sort: Compara y intercambia elementos adyacentes repetidamente, haciendo que los grandes "floten" al final.
#Insertion Sort: Toma un elemento y lo inserta en su lugar correcto dentro de la parte ya ordenada de la lista, como al ordenar cartas.
#Selection Sort: Encuentra el elemento más pequeño en la parte no ordenada y lo intercambia con el primer elemento de esa sección.
#Eficiencia y Rendimiento
#Los tres son lentos para listas grandes (O(n2))
#,lo que significa que tardan mucho más si la lista crece.
#Insertion Sort es el más rápido de los tres si la lista es pequeña o ya está casi ordenada.
#Bubble Sort es el más lento en general.
#Todos usan muy poca memoria extra (O(1)).
#Cuándo Usarlos
#Bubble Sort: Ideal para enseñar cómo funciona el ordenamiento, o para listas muy pequeñas.
#Insertion Sort: Perfecto para listas pequeñas, listas casi ordenadas o cuando recibes 
# elementos uno a uno y los ordenas al instante (ordenamiento "online").
#Selection Sort: Útil cuando es caro mover datos (hacer intercambios), ya que hace e
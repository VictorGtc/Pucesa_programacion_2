print("///Comparador de metodos de ordenamientos///\n")
print("""Una empresa desea analizar cuál método de ordenamiento le conviene más para ordenar 
      listas pequeñas de productos según su precio. Para ello, te ha encargado realizar un comparador 
      práctico entre tres algoritmos clásicos de ordenamiento: Bubble Sort, Insertion Sort y Selection Sort.""")


lista_precios=[]


def bublle_sort(lista):
    print("\n Algoritmos de ordenamiento Bubble Sort")
    lista_rango=len(lista)
    
    comparaciones=0
    intercambios=0
    
    for i in range(lista_rango - 1):
        intercambio=False
        for j in range(lista_rango - 1 - i):
            comparaciones+=1
            if lista[j]>lista[j+1]: 
                lista[j], lista[j+1]=lista[j+1], lista[j]
                intercambios+=1
                intercambio=True
        if not intercambio:
            break
        
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
        
    print("Los precios seran ordenados en forma bubble sort:\n")
    
    print(bublle_sort(lista_precios))
    
    opc=input("Si desea realizar nuevamente otro ordenamiento de valores preciose enter o escriba salir si desea terminar: ").lower().strip()
    
    lista_precios=[]
    if opc=="salir":
        print("Gracias por usar nuestro codigo C:")
        break
    
#
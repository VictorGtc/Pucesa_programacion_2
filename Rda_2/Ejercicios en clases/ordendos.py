lista_precios=[]

def intertion_sort(lista):
    print("\nAlgoritmos de ordenamiento Insertion Sort")
    
    comparaciones=0
    intercambios=0
    
    lista_rango=len(lista)
    
    if lista_rango <= 1:
        return lista, comparaciones, intercambios
    for i in range(1,lista_rango):
        valor_actual=lista[i]
        j=i-1
        while j >= 0 and valor_actual < lista[j]:
            comparaciones+=1
            lista[j+1]=lista[j]
            intercambios+=1
            j-=1
        if j>=0:
            comparaciones+=1
        lista[j+1]=valor_actual
        
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
        
    print("Los precios seran ordenados en forma intertion sort:\n")
    
    print(intertion_sort(lista_precios))
    
    opc=input("Si desea realizar nuevamente otro ordenamiento de valores preciose enter o escriba salir si desea terminar: ").lower().strip()
    
    lista_precios=[]
    if opc=="salir":
        print("Gracias por usar nuestro codigo C:")
        break
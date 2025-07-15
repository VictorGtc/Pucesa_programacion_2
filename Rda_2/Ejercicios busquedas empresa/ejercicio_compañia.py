"""Una empresa de servicios quiere automatizar la gestión de su base de datos de clientes. 
Para ello, te han solicitado crear un pequeño sistema en Python que permita:

1. Ordenar clientes por nombre alfabéticamente.
2. Ordenar clientes por saldo adeudado de menor a mayor.
3. Buscar un cliente por su nombre para verificar si se encuentra en la base.
"""

lista_cliente_sueldo=[("Jorgue",186),
                      ("Braulio",100),
                      ("Alejandro",456),
                      ("Richard",300),
                      ("Esteban", 250),
                      ("Dilon",367),
                      ("Gabriel",800),
                      ("Yoshua",590),
                      ("Paul",600),
                      ("Cheche",1000)]

def insert_sort(lista):
    rango_lista=len(lista)
    for i in range(1,rango_lista):
        llave=lista[i]
        j=i-1
        while j>=0 and lista[j][0] > llave[0]:
            lista[j+1]=lista[j]
            j-=1
        lista[j+1]=llave
    return lista

def selection_sort(lista):
    contar_lista=len(lista)
    for i in range(contar_lista):
        valor_pequeño=i
        for j in range(i+1,contar_lista):
            if lista[j][1] < lista[valor_pequeño][1]:
                valor_pequeño=j
        lista[i],lista[valor_pequeño]=lista[valor_pequeño],lista[i]
    return lista


def busqueda_lineal(objeto,lista):
    encontrar=False
    for n in range(len(lista)):
        if objeto==lista[n][0]:
            print(f"\nEl cliente: {objeto} fue encontrado en la posicion: {n+1} su saldo es: {lista[n][1]}\n")
            encontrar=True
    if not encontrar:
        print("El nombre no coincide en la lista")
        
def busqueda_binaria(lista,objeto):
    bajo=0
    alto=len(lista)-1
    nombre_completo=objeto
    while bajo <=alto:
        medio=(bajo+alto)//2
        nombre_medio=lista[medio][0]
        if nombre_medio==nombre_completo:
            return lista[medio], medio
        elif nombre_completo < nombre_medio:
            alto=medio-1
        else:
            bajo = medio+1
    return None, -1
    
def añadir_cliente(lista,cliente,saldo):
    print("\n====Ingreso de nuevos clientes====\n")
    datos_clientes=cliente,saldo
    lista.append(datos_clientes)
    print("\nLos datos han sido guardados con exito C:\n")





print("""
      /////Gestion de base de datos de Clientes/////
      1. Clientes ordenados por orden alfabetico
      2. Clientes ordenados por saldo 
      3. Busqueda lienal de clientes
      4. Busqueda Binaria de cleintes
      5. Añadir clientes y su saldo""")
while True:
    opc=int(input("Ingrese la opcion que se desea realizar: \n"))
    while opc<0 or opc>5:
        print("Valor invalido, ingrese valores dentro del rango del 1 al 6")
        opc=int(input("Ingrese la opcion que se desea realizar: "))

    if opc==1: 
        print("=========Clientes ordenador por orden alfabetico============")
        lista_ordenada=insert_sort(lista_cliente_sueldo)
        
        for i in lista_ordenada:
            nombre,saldo=i
            print("____________________________________________")
            print(f"Nombre:{nombre:>10}           Saldo:{saldo}")
        cont=input("\nPrecione enter para continuar")

    if opc==2:
        print("========Clientes ordenados por orden de saldo pendiente========")
        
        lista2_ordenado=selection_sort(lista_cliente_sueldo)
        
        for j in lista2_ordenado:
            nombre2,saldo2=j
            print("_____________________________________________")
            print(f"Nombre:{nombre2:>10}          Saldo:{saldo2} ")
        cont=input("\nPrecione enter para continuar")

    if opc==3:
        print("==========Busqueda de clientes en la lista de datos======== \n")
        cliente=input("\nIngrese el nombre del cliente a buscar: \n").capitalize().strip()
        busqueda_lineal(cliente,lista_cliente_sueldo)
        cont=input("\nPrecione enter para continuar\n")

    if opc==4:
        print("=======Este apartado fue realizado mediante Busqueda binaria=======\n")
        lista_ordenada=insert_sort(lista_cliente_sueldo)
        cliente1=input("Ingrese el nombre del cliente a buscar: \n").capitalize().strip()
        
        busqueda_b,pos=busqueda_binaria(lista_ordenada,cliente1)
        if busqueda_b:
            print(f"El cliente: {busqueda_b[0]} esta en la lista, este se encuentra en la posicion {pos+1:>3}: Su saldo es: {busqueda_b[1]}")
        else:
            print(f"El cliente '{cliente1}' no fue enocntrado ")
        cont=input("\nPrecione enter para continuar\n")
    if opc==5:
        print("=====Registroa de nuevos clientes=====")
        cliente=input("Imgrese el nombre del nuevo usuario: ")
        saldo=int(input("Ingrese el valor del cliente: "))
        añadir_cliente(lista_cliente_sueldo,cliente,saldo)
        cont=input("\nPrecione enter para continuar\n")
    if opc==6:
        print("Gracias por usar nuestra aplicacion C:")
        break


# Preguntas de reflexión (escritas en celda Markdown)

# ¿Por qué es necesario ordenar antes de realizar la búsqueda binaria?

# Es necesario ordenar para la búsqueda binaria porque el algoritmo se 
# basa en dividir la lista por la mitad repetidamente. Si los datos no están ordenados, 
# no puedes garantizar que el elemento buscado estará en una de las mitades después de cada división, 
# haciendo que el método falle.

# ¿Qué pasaría si usamos búsqueda binaria sin ordenar primero?

# Si usaras la búsqueda binaria en una lista sin ordenar, el algoritmo no funcionaría. 
# La lógica de descarte de mitades se volvería inválida, y el algoritmo podría no encontrar 
# el elemento buscado, incluso si está presente, porque su fundamento (el orden) no existe.

# ¿Qué ventajas viste entre la búsqueda binaria y la búsqueda lineal?

# La principal ventaja es la eficiencia. La búsqueda binaria es mucho más rápida 
# (O(log n)) que la búsqueda lineal (O(n)) para listas grandes, ya que elimina la mitad 
# de los elementos posibles en cada paso.

# ¿Cuál de los dos ordenamientos te pareció más intuitivo de implementar y por qué?

# Generalmente, el ordenamiento por burbuja (Bubble Sort) es el más intuitivo. 
# Su lógica de comparar y intercambiar elementos adyacentes hasta que no haya más 
# desórdenes es directa y fácil de visualizar, lo que simplifica su implementación inicial.
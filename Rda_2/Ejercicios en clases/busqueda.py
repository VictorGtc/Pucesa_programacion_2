#1. ¿Qué es la búsqueda lineal? ¿Cómo funciona?
#la búsqueda lineal es un algoritmo sencillo para encontrar 
#un elemento específico dentro de una lista. Funciona revisando cada elemento de la lista uno por uno, 
#comenzando desde el principio, hasta encontrar el elemento buscado o llegar al final de la lista
#este tipo de busqueda tiene algo en particular, pues la lista en donde se hace esta busqueda 
#puede estar en desorden o en orden pues no importa como este la lista, pues esta siempre buscara 
#de principio a fin esto puede llegar a ser un poco lento pues, tiene una complejidad temporal de O(n), 
#lo que significa que el tiempo de ejecución aumenta linealmente con el tamaño de la lista. 
#Esto la hace ineficiente para listas grandes, pero es uno de los tipos
#mas basicos y faciles de entender e implementar 
#Es útil para listas pequeñas o cuando la lista no está ordenada, o cuando ordenar la lista no es práctico. 



#2. ¿Qué es la búsqueda binaria? ¿Qué condición especial debe cumplir la lista?

#La búsqueda binaria es una técnica para encontrar un elemento en una lista ordenada. 
#Se basa en la idea de dividir la lista repetidamente a la mitad hasta que se encuentre el elemento 
#o se determine que no está en la lista. 
#La condición fundamental para que la búsqueda binaria funcione es que la lista debe 
#estar ordenada, ya sea en orden ascendente o descendente. El algoritmo se basa en el orden 
#de los elementos para eliminar rápidamente las mitades de la lista que no pueden contener el elemento buscado. 
#La búsqueda binaria divide repetidamente la lista en dos partes, comparando el elemento 
#objetivo con el elemento en el medio de la lista. 
#Si el elemento objetivo es igual al elemento del medio, se ha encontrado el elemento 
#y la búsqueda termina. 
#Si el elemento objetivo es menor que el elemento del medio, se continúa la búsqueda 
#en la mitad izquierda de la lista. 
#Si el elemento objetivo es mayor que el elemento del medio, se continúa la búsqueda 
#en la mitad derecha de la lista. 


#3. ¿En qué casos conviene usar cada una?
#La búsqueda lineal se utiliza cuando tienes una lista pequeña o no está ordenada
#se lo sele usar para hacer pequeños proyectos o demostrar los tipos de busquedas y 
#la sintaxis de sus usos. 
#La búsqueda binaria es más eficiente para listas grandes y ordenadas, pues esta es mucho 
#mas rapida y mas eficiente ahorrando tiempo y maximizando la busqueda dentro de la lista.
#En detalle:
#Búsqueda Lineal:
#Es un método simple, comparando cada elemento uno por uno hasta encontrar el objetivo o 
#llegar al final de la lista.
#Es adecuada para conjuntos de datos pequeños o no ordenados, ya que no requiere 
#que los datos estén en un orden específico.
#Ejemplo: Buscar un nombre en una lista de nombres sin ordenar.
#Búsqueda Binaria:
#Es más rápida, especialmente para listas grandes, dividiendo la lista repetidamente 
#por la mitad hasta encontrar el elemento objetivo.
#Requiere que la lista esté ordenada.
#Ejemplo: Buscar un número en una lista de números ordenados. 



lista=["1984", "Cien años de soledad","Don Quijote de la Mancha","Crimen y castigo","Orgullo y prejuicio"
"La sombra del viento","El cuento de la criada","Kafka en la orilla","Los juegos del hambre","Las ventajas de ser invisible"]
def recorrer_lista(objeto,lista):
    #ciclo for en donde recorre toda la lista mediante el conteo de objetos
    print("\n====BUSQUEDA LINEAL====\n")
    for i in range(len(lista)): 
        #comparamos la fruta de la lista con la del usuasrio 
        if lista[i] == objeto:
            #imprimimos la forma en la que, queramos que nos aparezaca un mensaje 
            #al encontrar la fruta en nuestra listra 
            print(f"""
                  ====== Su libro fue encontrado encontrada :D ====
                  El libro {objeto} esta en la lista de nuestros libros
                  El libro se encuentra se encuentra en la posicion {i+1}\n
                  Este bucle sea a realizado :{i+1} veces""")
            print(f" ")
            #rompe el ciclo al encsontrar la fruta 
            break
        # Estas lineas nos permiten saber si la fruta no esta en la lista
        elif objeto not in lista:
            print("El libro no fue encontrado")
            break
        else:
            #Esta parte muestra cuantas comparaciones se realizan hasta encontrar la el libro 
            # solicitado por el ususario 
            print(f"La comparacion {i+1} realziada es: ")
            print(f"El libro {objeto} no es igual a {lista[i]} ")
            print("El libro no fue encontrada vamos con la siguiente comparacion\n")

print("""
      ===Bivenidos a nuestro sistema de busqueda de libros===
      """)



orden_lista=sorted(lista)

def busqueda_binaria(libros_buscar,lista):

    inicio=0
    fin=len(lista) - 1
    while inicio<=fin: 
        medio=(inicio+fin)//2
        libro_medio=orden_lista[medio]
        if libro_medio == libros_buscar:
            return medio
        elif libro_medio<libros_buscar:
            inicio=medio+1
        else: 
            fin = medio - 1
    return -1
while True:
    libros_buscar=input("Ingrese el libro que quiera buscar: ").capitalize().strip()
    while libros_buscar=="" or libros_buscar==" ":
        print("Ingrese un valor valido/no vacio")
        libros_buscar=input("Ingrese el libro que quiera buscar: ")
    if libros_buscar!="" or libros_buscar!=" ":
        print("\n===== Buscando libro ==== \n")
    if libros_buscar=="Salir":
        print("=== Gracias por usa nuestro Promgrama ===")
        break

    recorrer_lista(libros_buscar,lista)

    indice=busqueda_binaria(libros_buscar, orden_lista)

    print(f"""\nLa lista se ordeno para relizar la busqueda binaria
        la lista ordenada es: 
    """)
    for i in orden_lista:
        print(f"-->{i}")
        
    if indice != -1: 
        print(f"""
            ==Busqueda Binaria==
            Su libro fue encontrado :D
            el libro {libros_buscar}, se encontro en la posicion {indice+1}""")
    else:
        print(f"\n{libros_buscar}, este libro no esta en la lista ")

        
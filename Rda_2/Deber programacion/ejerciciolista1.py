#Funcion para realizar la busqueda del la fruta, mediante el uso la lista y la fruta a buscar como argumentos
def recorrer_lista(objeto,lista):
    #ciclo for en donde recorre toda la lista mediante el conteo de objetos
    for i in range(len(lista)): 
        #comparamos la fruta de la lista con la del usuasrio 
        if lista[i] == objeto:
            #imprimimos la forma en la que, queramos que nos aparezaca un mensaje al encontrar la fruta en nuestra listra 
            print(f"""
                  ====== La fruta fue encontrada :D ====
                  La fruta {objeto} esta en la lista de nuestras frutas
                  Esta fruta se encuentra se encuentra en la posicion {i+1}\n""")
            print("Este bucle sea a realizado :",i+1, "veces")
            #rompe el ciclo al encontrar la fruta 
            break
        # Estas lineas nos permiten saber si la fruta no esta en la lista
        elif objeto not in lista:
            print("La fruta no esta en la lista")
            break
        else:
            #Esta parte muestra cuantas comparaciones se realizan hasta encontrar la fruta 
            print(f"La comparacion {i+1} realziada es: ")
            print(f"La fruta {objeto} no es igual a {lista[i]} ")
            print("Como la fruta no fue encontrada vamos con la siguiente comparacion\n")
            
            
#Inicializamos nuestra lista con 20 frutas
lista1=["Manzana", "Banana", "Naranja", "Fresa","Uva", "Mango", "Piña", "Sandia", "Melon", "Pera", "Kiwi", "Durazno", "Cereza", "Frambuesa", "Arandano", "Aguacate", "Mandarina", "Papaya", "Granada", "Maracuya"]
#Iniciamos un bucle para que se busque varias frutas 
while True:  
    #Ingreso de la fruta mediante consolo para el usuario 
    opcion=input("Ingrese la fruta a buscar: ")
    #En esta ultima linea sea inicializa el programa 
    recorrer_lista(opcion.capitalize(),lista1)
    #Inicamos otra opcion si se desea terminar el programa o continuar
    opcion2=input("Desea continuar buscado mas frutas ==precione enter== ? Si desea salir escriba == Salir == : ")
    #Comparamos si se desea salir si es verdad, se mostrara un mensaje y terminara el programa 
    if opcion2.capitalize()=="Salir":
        print("Gracias por usar nustro programa C:")
        break
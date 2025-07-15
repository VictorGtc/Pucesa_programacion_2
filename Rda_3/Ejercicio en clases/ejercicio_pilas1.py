
historial = []
historial.append("www.google.com")
historial.append("www.python.org")
historial.append("www.stackoverflow.com """)

while True:
    print("""Navegacion de paginas
      Paginas disponibles: 
      
      1. Mostrar paginas
      2. Ultima pagina visitada
      3. Eliminar reciente
      4. Verificar
      5. salir
      """)
    opc=int(input("\nIngrese la opcion a realizar: "))
    if opc==1: 
        print("Lista entera de las paginas")
        print(historial)
        opc2=input("\nPrecione enter para continuar: ")
    if opc==2: 
        print("\nEsta es la ultima pagina visitada por el usuario: \n ",historial[-1])
        opc2=input("\nPrecione enter para continuar: ")
    if opc==3:
        print(len(historial))
        if len(historial) != 1:
            historial.pop()
            print("La pagina actual es: ",historial[-1])
        else:
            print("Ya no puedes volver, pila vacia")
        opc2=input("\nPrecione enter para continuar: ")
    if opc==4: 
        if len(historial)==0:
            print("El historial esta vacio ")
            opc2=input("\nPrecione enter para continuar: ")
        else:
            print("Las pafinas restantes son: ",historial)
        opc2=input("\nPrecione enter para continuar: ")
    if opc==5: 
        print("Gracias por usar nuestro proyecto C:")
        break



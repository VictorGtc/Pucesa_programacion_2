def recorrer_lista_binaria(obejeto, lista):
    # Inicializamos el índice del inicio de la búsqueda en la lista 
    inicio = 0
    # Inicializamos el índice del fin de la búsqueda en la lista 
    fin = len(lista) - 1

    # Mientras el índice de inicio sea menor o igual al índice de fin,
    # significa que todavía hay una porción de la lista donde buscar
    while inicio <= fin:
        # Calculamos el índice del elemento que está en la mitad de la porción actual de la lista
        # La división entera (//) asegura que "medio" sea un número entero
        medio = (inicio + fin) // 2

        # Comparamos el elemento que está en la mitad con el objeto que estamos buscando
        if lista[medio] == obejeto:
            # Si el elemento del medio es igual al objeto,
            # Retornamos el índice en el que se encontró el objeto
            return medio
        # Si el elemento del medio es menor que el objeto que estamos buscando,
        # significa que el objeto (si existe) debe estar en la mitad derecha de la lista
        elif lista[medio] < obejeto:
            # Ajustamos el índice de inicio para que comience después del medio
            inicio = medio + 1
        # Si el elemento del medio es mayor que el objeto que estamos buscando,
        # significa que el objeto (si existe) debe estar en la mitad izquierda de la lista
        else:
            # Ajustamos el índice de fin para que termine antes del medio
            fin = medio - 1

    # Si el bucle 'while' termina sin encontrar el objeto,
    # significa que el objeto no está presente en la lista
    # Retornamos -1 para indicar que no se encontró.
    return -1

# Definimos una lista de números enteros que deben estar ordenados
# para que la búsqueda binaria funcione correctamente
valores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Pedimos al usuario que ingrese un valor para buscar en la lista
# Convertimos la entrada del usuario a un entero usando int()
opcion = int(input("Ingrese el valor entre el 10 al 100 en intervalos de 10: "))

# Llamamos a la función "recorrer_lista_binaria" con el valor ingresado por el usuario
# y la lista de valores. El resultado 
# se guarda en la variable 'fun'
fun = recorrer_lista_binaria(opcion, valores)

# Verificamos si la variable 'fun' es diferente de -1
# Si es diferente de -1, significa que el valor se encontró en la lista
if fun != -1:
    # Imprimimos un mensaje indicando que el valor se encontró y la posición (índice) en la que está
    print(f"{opcion} se encontro en la posicion {fun}")
# Si 'fun' es igual a -1, significa que el valor no se encontró en la lista
else:
    # Imprimimos un mensaje indicando que el valor no se encontró en la lista
    print(f"{opcion} no se encontro en la lista ")
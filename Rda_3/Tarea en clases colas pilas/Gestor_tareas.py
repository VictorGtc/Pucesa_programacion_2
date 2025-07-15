print("/// Gestor de tareas Empleados \\\\n")

class PilaTareas:
    def __init__(self):
        self.items = []
        
    def agregar_tarea(self, tarea):
        self.items.append(tarea)
        print("Su tarea fue guardada con exito")
        
    def terminar_tarea(self):
        contar=len(self.items)
        if contar>=1:
            print(f"Su ultima tarea ///{self.items[-1]}\\\ ha sido completada \n")
            self.items.pop()
        else:
            print("Ya no tiene mas tereas pendientes")
    def ver_ultima_tarea(self):
        contar=len(self.items)
        if contar!=1:
            print(f"Su ultima tarea pendiente es: {self.items[-1]}")
    def lista_total(self):
        return(self.items)
    def tamaño(self):
        return len(self.items)
    
    def ingreso_tareas(self):
        try: 
            opc=int(input("\nIngrese la opcion a realizar: "))
        except ValueError:
            print("Valores incorrecto solo numeros")
            return self.ingreso_tareas()
        while opc>4 or opc<1 :
            print("Ingrese solo valores del 1 al 4")
            try: 
                opc=int(input("Ingrese la opcion a realizar : "))
            except ValueError:
                print("Valores incorrecto solo numeros")
        return opc
    def contunar(self):
        opc2=input("Precione enter para continuar: ")

clases_usar=PilaTareas()
while True:
    print("""Opciones a realizar en el programa:\n
          1. Ingresar nueva tarea
          2. Completar ultima tarea
          3. Consultar tarea actual
          4. Consultar todas las tareas
          5. Salir\n""")
    opcion=clases_usar.ingreso_tareas()
    if opcion==1: 
        tarea=input("\nIngrese la tarea a guardar: ")
        clases_usar.agregar_tarea(tarea)
        clases_usar.contunar()
    if opcion==2: 
        if clases_usar.tamaño()<1:
            print("No hay tareas que realizar\n")
        else:
            clases_usar.terminar_tarea()
        clases_usar.contunar()
    if opcion==3:
        if clases_usar.tamaño()<1:
            print("No hay tareas que realizar\n ")
        else:
            clases_usar.ver_ultima_tarea()
        clases_usar.contunar()
    if opcion==4:
        lista=clases_usar.lista_total()
        cont=0
        print("""Todas las tareas pendientes se mostraran a cotinuacion
              La tarea mas reciente ingresada el la primera de la lista\n""")
        for i in sorted(lista,reverse=True):
            cont+=1
            print(f"{cont}.{i}")
        clases_usar.contunar()
    if opcion==5:
        print("\nGracias por usar nuestro proyecto C:\n")
        break
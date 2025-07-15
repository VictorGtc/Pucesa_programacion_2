class NodoDoble:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None
        self.anterior=None

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, dato):
        nuevo = NodoDoble(dato)
        nuevo.siguiente = self.cabeza
        if self.cabeza is not None:
            self.cabeza.anterior = nuevo
        self.cabeza = nuevo

    def recorrer_adelante(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.dato, end=" <-> ") 
            actual = actual.siguiente       
        print("None")  

    def recorrer_atras(self):
        actual = self.cabeza
        if actual is None:
            print("Lista vacía")
            return
        while actual.siguiente is not None:
            actual = actual.siguiente
            
        while actual is not None:
            print(actual.dato, end=" <-> ") 
            actual = actual.anterior         
        print("None") 
        
    def funciones_interactivas(self):

        if self.cabeza is None:
            print("""La lista esata vacia, primero ingrese nuevas paginas\n""")
            return
        
        actual_interactivo=self.cabeza
        
        ultimo_nodo=self.cabeza
        
        if ultimo_nodo is not None:
            while ultimo_nodo.siguiente is not None:
                ultimo_nodo=ultimo_nodo.siguiente
                
        print("La pagina principal en el que se encuentra es: ",self.cabeza.dato)
        
        while True:
            
            comando=input("Ingrese la accion que desea realizar: ").lower().strip()
            
            if comando=="adelante":
                if actual_interactivo.siguiente is not None:
                    actual_interactivo=actual_interactivo.siguiente
                    print("Se ha movido ha la pagina: ", actual_interactivo.dato)
                else:
                    print("Ha llegado al limite de las paginas, no hay mas paginas")
            elif comando== "atras":
                if actual_interactivo.anterior is not None:
                    actual_interactivo=actual_interactivo.anterior
                    print("Se ha movido ha la pagina: ", actual_interactivo.dato)
                else:
                    print("Ha llegado al limite de las paginas, no hay mas paginas")
            elif comando== "fin":
                actual_interactivo=ultimo_nodo
                print("Has saldato hasta la ultima pagina de nuestra lista: ",actual_interactivo.dato)
            elif comando== "inicio":
                actual_interactivo=self.cabeza
                print("Ha saltado hacie el primero nodo de la lista, actualmente esta en: ", actual_interactivo.dato)
            elif comando== "salir":
                print("Gracias por usar nuestro programa, Vuelva pronto")
                break
    
    def eliminar_elemento(self, dato):
        actual = self.cabeza 
        if actual is None:
            print(f"La lista está vacía. No se puede eliminar '{dato}'.")
            return False 

        while actual is not None and actual.dato != dato:
            actual = actual.siguiente

        if actual is None:
            print(f"'{dato}' no se encontró en la lista. No se pudo eliminar.")
            return False 



        if actual == self.cabeza:
            self.cabeza = actual.siguiente 
            if self.cabeza is not None: 
                self.cabeza.anterior = None 
            print(f"'{dato}' eliminado de la cabeza de la lista.")
            return True 

        if actual.anterior is not None:
            actual.anterior.siguiente = actual.siguiente
        
        if actual.siguiente is not None:
            actual.siguiente.anterior = actual.anterior
        
        print(f"'{dato}' eliminado de la lista.")
        return True 

lista = ListaDobleEnlazada()


while True:
    
    print("""Bienvenidos al programa interactivo\n
          1. Ingresar datos
          2. Comenzar a navegar 
          3. Ver lista completa
          4. Elimnar dato 
          5. Salir
            """)
    
    opc=input("Ingrese una opcion a realizar: ")
    
    if opc=="1":
        entrada=input("Ingrese la pagina que necesite guardar:")
        lista.insertar_inicio(entrada)
        print("Se ha guardado con exito")
    if opc=="2":
        print("A continuacion, navegara por la paginas ingresadas")
        print("Comando que se peuden usar: adelante; atras; inicio; fin;\n")
        lista.funciones_interactivas()
    if opc=="3":
        print("Su historias de navegacion completa es: ")
        print("\nListado completo ")
        lista.recorrer_adelante()
        print(" ")
    if opc=="4":
        while True:
            elemento_a_eliminar_str = input("Ingresa la pagina a eliminar: ")
            try:
                elemento_a_eliminar = int(elemento_a_eliminar_str)
                lista.eliminar_elemento(elemento_a_eliminar)
                print("\nEstado actual de la lista:")
                lista.recorrer_adelante()
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número o 'salir'.")
    if opc=="5":
        print("Gracias por usar nuestro proyecto, vuelva pronto C:")
        break



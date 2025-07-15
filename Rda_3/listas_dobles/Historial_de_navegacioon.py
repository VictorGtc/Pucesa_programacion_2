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
        print("""Bienvenidos al programa interactivo\n
            Comando que se peuden usar: adelante; atras; inicio; fin;\n""")
        
        
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
            

lista = ListaDobleEnlazada()


lista.insertar_inicio("google.com")
lista.insertar_inicio("openai.com")
lista.insertar_inicio("firefox.com")
lista.insertar_inicio("chorme.com")
lista.insertar_inicio("office.com")
lista.insertar_inicio("github.com")
lista.insertar_inicio("Inicio")

print("\nListado completo ")
lista.recorrer_adelante()
print(" ")
lista.funciones_interactivas()

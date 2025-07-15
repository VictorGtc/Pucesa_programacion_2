
class NodoDoble:
    def __init__(self,estudiante,motivo,fecha):
        self.estudiante=estudiante
        self.motivo=motivo
        self.fecha=fecha
        self.siguiente=None
        self.anterior=None

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def insertar_inicio(self,estudiante,motivo,fecha):
        nuevo = NodoDoble(estudiante,motivo,fecha)
        nuevo.siguiente = self.cabeza
        if self.cabeza is not None:
            self.cabeza.anterior = nuevo
        self.cabeza = nuevo
    def recorrer_adelante(self):
        actual = self.cabeza
        while actual is not None:
            print(f"""
                  Nombre del estudiante:{actual.estudiante}
                  Motivo por la visita: {actual.motivo}
                  Fecha de la visita : {actual.fecha}
                  """) 
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
            print(f"""
                  Nombre del estudiante:{actual.estudiante}
                  Motivo por la visita: {actual.motivo}
                  Fecha de la visita : {actual.fecha}
                  """) 
            actual = actual.anterior         
        print("None") 
    def funciones_interactivas(self):
        if self.cabeza is None:
            print("""La lista esata vacia, primero ingrese nuevas registro\n""")
            return
        actual_interactivo=self.cabeza
        ultimo_nodo=self.cabeza
        
        if ultimo_nodo is not None:
            while ultimo_nodo.siguiente is not None:
                ultimo_nodo=ultimo_nodo.siguiente
                
        print(f"""El primer registro en el que se encuentra es: 
              Nombre del estudiante:{actual_interactivo.estudiante}
              Motivo por la visita: {actual_interactivo.motivo}
              Fecha de la visita : {actual_interactivo.fecha}
              
              """)
        
        while True:
            
            comando=input("Ingrese la accion que desea realizar: ").lower().strip()
            
            if comando=="adelante":
                if actual_interactivo.siguiente is not None:
                    actual_interactivo=actual_interactivo.siguiente
                    print(f"""Se ha movido ha al reguistro del estudiante: 
                          Nombre del estudiante:{actual_interactivo.estudiante}
                          Motivo por la visita: {actual_interactivo.motivo}
                          Fecha de la visita : {actual_interactivo.fecha}
                          """)
                else:
                    print("Ha llegado al limite de las paginas, no hay mas paginas")
            elif comando== "atras":
                if actual_interactivo.anterior is not None:
                    actual_interactivo=actual_interactivo.anterior
                    print(f"""Se ha movido ha al reguistro del estudiante: 
                          Nombre del estudiante:{actual_interactivo.estudiante}
                          Motivo por la visita: {actual_interactivo.motivo}
                          Fecha de la visita : {actual_interactivo.fecha}
                          """)
                else:
                    print("Ha llegado al limite de las paginas, no hay mas paginas")
            elif comando== "fin":
                actual_interactivo=ultimo_nodo
                print(f"""Se ha movido ha al reguistro del estudiante: 
                          Nombre del estudiante:{actual_interactivo.estudiante}
                          Motivo por la visita: {actual_interactivo.motivo}
                          Fecha de la visita : {actual_interactivo.fecha}
                          """)
            elif comando== "inicio":
                actual_interactivo=self.cabeza
                print(f"""Se ha movido ha al reguistro del estudiante: 
                          Nombre del estudiante:{actual_interactivo.estudiante}
                          Motivo por la visita: {actual_interactivo.motivo}
                          Fecha de la visita : {actual_interactivo.fecha}
                          """)
            elif comando== "salir":
                print("Gracias por usar nuestro programa, Vuelva pronto")
                break

lista=ListaDobleEnlazada()

while True:
    
    print("""Bienvenidos al programa interactivo\n
          1. Ingreso de registro medico
          2. Comenzar a navegar entre registros
          3. Ver registro completo de estudiantes
          4. Salir
            """)
    
    opc=input("Ingrese una opcion a realizar: ")
    
    if opc=="1":
        nombre_estudiante=input("Ingrese el nombre del estudiante: ")
        motivos_visita=input("Ingrese el motivo de la visita: ")
        fecha_visita=input("Ingrese la fecha de la visita DD/MM/AA: ")
        lista.insertar_inicio(nombre_estudiante,motivos_visita,fecha_visita)
        print("Se ha guardado con exito")
    if opc=="2":
        print("A continuacion, navegara por la paginas ingresadas")
        print("Comando que se peuden usar: adelante; atras; inicio; fin; salir\n")
        lista.funciones_interactivas()
    if opc=="3":
        print("Su historias de navegacion completa es: ")
        print("\nListado completo ")
        lista.recorrer_adelante()
    if opc=="4":
        print("Saliendo gracias por su uso")
        break
import time


class Incidente:
    def __init__(self,nombre,anio, tipo,id_estudiante):
        self.nombre=nombre
        self.anio=anio
        self.tipo=tipo
        self.id_estudiante=id_estudiante
        self.siguiente=None
        self.anterior=None
        

# Clase ListaBitacora
class ListaBitacora:
    def __init__(self):
        self.inicio = None
    def agregar_incidente(self,nombre,anio, tipo,id_estudiante):
        nodo_nuevo=Incidente(nombre, anio,tipo,id_estudiante)
        nodo_nuevo.siguiente=self.inicio
        self.inicio=nodo_nuevo

    def eliminar_incidente(self, nombre_buscar):
        actual=self.inicio
        while actual and actual.nombre !=nombre_buscar:
            actual=actual.siguiente
            
        if actual is None:
            print("La lista esta vacia, primeor ingrese valores :D")
            return
        if actual.anterior is None:
            self.inicio=actual.siguiente
            if self.inicio:
                self.inicio.anterior=None
        else:
            actual.anterior.siguiente=actual.siguiente
            if actual.siguiente:
                actual.siguiente.anterior=actual.anterior
        print(f"El reguistro del estudiante; {nombre_buscar} ha sido eliminado ")

    def buscar_incidente(self, nombre_encontrar):
        actual=self.inicio
        encontrado=False
        while actual:
            if actual.nombre==nombre_encontrar:
                print(f"""
                      Registro del estudiante buscado: 
                      Nombre del estudiante:{actual.nombre}
                      Año del del reguistro :{actual.anio}
                      Tipo de incidente: {actual.anio}
                      Id del estudiante: {actual.id_estudiante}
                      
                      """)
                encontrado=True
                break
            actual=actual.siguiente
        if not encontrado:
            print(f"El estudiante: {nombre_encontrar} no ha sido encontrado")
        

    def mostrar_incidentes(self):
        actual=self.inicio
        if self.inicio==None:
            print("La lista esta vacia, ingrese primero estudiantes")
            return
        
        while actual is not None:
            print("Los estudiantes que estan dentro de la lista para la evacuacion son los siguinetes: ")
            print(f"""
                  Nombre del estudiante: {actual.nombre}
                  ID del estudiante: {actual.id_estudiante}
                  Año del incidente: {actual.anio}
                  Tipo de incidente: {actual.tipo}
                  ----------------------------------------------
                  """)
            actual=actual.siguiente

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







class EstudianteEvacuacion:
    def __init__(self, nombre, aula, id_estudiante):
        self.nombre = nombre
        self.aula = aula
        self.id_estudiante=id_estudiante
        self.siguiente=None

class ColaDeAtencionSimple:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar(self, nombre, aula, id_estudiante):
        nuevo_nodo = EstudianteEvacuacion(nombre, aula, id_estudiante)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
    def avanzar(self):
        atendido=self.cabeza
        if self.cabeza is None:
            print("--- La cola está vacía. No hay nadie para atender. ---")
            return None
        while atendido is not None:
            print("Se simulara una evaciacion")
            print(f"""
                {time.sleep(1)}
                El estudiante: {atendido.nombre}
                Del Aula: {atendido.aula}
                Con su ID: {atendido.id_estudiante}
                {time.sleep(1)}
                Ha sido correctamente evacuados, continuando con los siguientes 
                """)
            
            atendido=atendido.siguiente

    def mostrar_en_espera(self):
        actual = self.cabeza
        if self.cabeza is None:
            print("La cola de atención está vacía.")
            return
        
        
        
        while actual is not None:
            print("Los estudiantes que estan en espera son los siquientes ")
            print(f"""
              
              El estudiante: {actual.nombre}
              Del Aula: {actual.aula}
              Con su ID: {actual.id_estudiante}
              ---------------------------------------
              """)
            actual=actual.siguiente
            
        







class nodo_reportes_medicos:
    def __init__(self,nombre, apellido,tipo, observacion):
        self.tipo=tipo
        self.observacion=observacion
        self.nombre=nombre
        self.apellido=apellido
        self.next=None
class reportes_paciente:
    def __init__(self):
        self.top=None
    def agregar_reportes(self,nombre,apellido, tipo, observacion):
        nuevo_nodo=nodo_reportes_medicos(nombre,apellido, tipo, observacion)
        nuevo_nodo.next=self.top
        self.top=nuevo_nodo
    
    def elimnar_reporte(self):
        if self.top==None:
            print("No hay Datos dentro de la lista de registros")
        else:
            opc4=input("Desea borrar el primero registro de la lista? ingrese esas opciones: Si o No: ").lower().strip()
            while opc4!="no" and opc4!="si":
                print("Ingrese una opcion valida")
                opc4=input("Desea borrar el primero registro de la lista? ingrese esas opciones: Si o No: ").lower().strip()
            
            if opc4=="si":
                plato_elimar=self.top
                print(f"""
                    El registro: 
                    Nombre: {plato_elimar.nombre}
                    Fecha: {plato_elimar.apellido}
                    Tipo de enfermedad: {plato_elimar.tipo}
                    Sintomas presentados: {plato_elimar.observacion}
                    
                    Ha sido eliminado de la lista 
                    """)
                self.top=plato_elimar.next
            if opc4=="no":
                print("Volviendo al inicio")
                opc5=input("Precione enter para coninuar")
                return
    
    def mostrar_registro(self):
        actual=self.top
        print("Reporte Medicos de los Estudiante")
        while actual is not None:
            print(f"""
                  \n
                  --------------------------------------------------
                  Nombre: {actual.nombre}
                  Fecha: {actual.apellido}
                  Tipo de enfermedad: {actual.tipo}
                  Sintomas presentados: {actual.observacion}
                  --------------------------------------------------
                  """)
            actual=actual.next
    
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
    def continar(self):
        opc2=input("Precione enter para continuar: ")













while True:
    print("""////Sistema de Gestión Escolar de Emergencia/////
        
        Bienvenidos a nuestro sistema de gestion 
        en donde podremos realizar diferentes tipos de listados
        para los diferente tipos de problemas que puede suceder
        dentro de un colegio o escuela 
        
        Las opciones que se pueden ralizar son los siguientes: 
        1. Reportes medicos Estudiantes
        2. Evacuacion escolar ordenada
        3. Ver los registros medicos de los estudiantes 
        4. Ver y almacenar bitacoras de incidentes escolares
        5. Salir
        """
        )

    opc=int(input("Ingrese una opcion que se desee realizar: "))

    while opc>=5 and opc<=1:
        print("Ingrese una opcion valida")
        opc=int(input("Ingrese una opcion que se desee realizar: "))


    clase_usar=reportes_paciente()
    cola_usar=ColaDeAtencionSimple()
    lista=ListaDobleEnlazada()
    cola_usar2=ListaBitacora()
    if opc==1:

        while True:
            print("""
                ========= MENÚ EVACUACION =========
                1. Ingreso nuevo pacinte
                2. Eliminar reporte 
                3. Ver todos los reportes 
                4. Salir
                """)
            opc3=clase_usar.ingreso_tareas()
            
            if opc3==1:
                nombre_paciente=input("Ingrese el nombre del estudiante: ")
                apelludo_pacinete=input("Ingresar el apellido del estudiante: ")
                tipo_paciente=input("Ingrese el tipo de enfermedad o problema de salud que presente el estudiante: ")
                descripcion_paciente=input("Ingrese los sintomas que ha tenido durante las ultimas 24 horas: ")
                clase_usar.agregar_reportes(nombre_paciente, apelludo_pacinete,tipo_paciente,descripcion_paciente)
                clase_usar.continar()
            if opc3==2:
                clase_usar.elimnar_reporte()
            if opc3==3:
                print("Mostrando todo los reportes meducos de los estudiantes")
                clase_usar.mostrar_registro()
                clase_usar.continar()
            if opc3==4:
                print("Saliendo........")
                time.sleep(2)
                break
            
    if opc==2:
        while True:
                print("""
        ========= MENÚ EVACUACION =========
        1. Agregar Estudiantes 
        2. Simular evacuacion
        3. Mostrar los estudiantes, en esta simulacion
        4. Sali""")
                opcion = input("Seleccione una opción: ").strip().lower()
                if opcion == "1":
                    nombre_estudiante= input("Ingrese el nombre del estudiante: ")
                    aula_estudiante=input("Ingrese el aula del estudiante: ")
                    id_estudiante=input("Ingrese el id del estudiante: ")
                    cola_usar.insertar(nombre_estudiante,aula_estudiante,id_estudiante)
                if opcion=="2":
                    cola_usar.avanzar()
                if opcion=="3":
                    cola_usar.mostrar_en_espera()
                if opcion=="4":
                    print("Saleindo.........")
                    time.sleep(2)
                    break
    if opc==3:
        while True:
            print("""
                ========= MENÚ EVACUACION =========\n
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
                print("Saliendo......")
                time.sleep(2)
                break
    if opc==4:
        while True:
            print("""
    ========= MENÚ EVACUACION =========
    1. Agregar incidente
    2. Eliminar incidente 
    3. Buscar indicente de los estudiantes 
    4. Mostrar todos los incidentes
    5. Salir """)
            
            opcion = input("Seleccione una opción: ").strip().lower()
            if opcion == "1":
                nombre_estudiante= input("Ingrese el nombre del estudiante: ")
                anio_incidente =input("Ingrese el año que sucedio el incidente: ")
                id_estudiante=input("Ingrese el id del estudiante: ")
                tipo_incidente=input("Ingrese el tipo de incidente que paso: ")
                cola_usar2.agregar_incidente(nombre_estudiante,anio_incidente,tipo_incidente,id_estudiante)
            if opcion=="2":
                nombre_eliminar=input("Ingrese el nombre del estudiante que quiere eliminar: ").lower().strip()
                cola_usar2.eliminar_incidente(nombre_eliminar)
            if opcion=="3":
                nombre_buscar=input("Ingrese el nombre del estudiante que quiero buscar: ")
                cola_usar2.buscar_incidente(nombre_buscar)
            if opcion=="4":
                cola_usar2.mostrar_incidentes()
            if opcion=="5":
                print("Saleindo.........")
                time.sleep(2)
                break
    if opc==5: 
        print("Gracias por usar nuestro proyecto, vuelva pronto :D")
        print("Saliendo.......")
        time.sleep(3)
        break
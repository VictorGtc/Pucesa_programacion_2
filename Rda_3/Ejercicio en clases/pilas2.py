"""PILAS PRINCIPIO LIFO"""

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

clase_usar=reportes_paciente()

while True:
    print("""
          GESTOR DE REPORTES MEDICOS
          1. INGRESO NUEVO PACIENTE
          2. ELIMNAR REPROTE
          3. VER TODOS LOS REPORTES
          4. SALIR
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
        print("Saliendo del programa")
        break
        
from paciente import Paciente
from paciente import Consulta


guardado_paciente=[]

def pacientes_ingresados():
    nombre=input("Ingrese el nombre del pacinete: ")
    while True: 
        try: 
            cedula=int(input("Ingrese el numero de cedula del paciente: "))
            break
        except ValueError: 
            print("Ingrese un numero valido") 
    edad=int(input("Ingrese la edad del paciente: "))
    tipo_sangre=input("Ingrese el tipo de sangre del paciente: ")
    enfermo=Paciente(nombre, cedula, edad, tipo_sangre)
    guardado_paciente.append(enfermo)
    print("El paciente ha sido registrado con exito")
    return enfermo

def buscar_paciente(nombre): 
    for pac in guardado_paciente: 
        if pac.nombre==nombre: 
            return pac
    return None

def datos_clinicos(paciente):
    print("\n Ingrese los datos clinicos del paciente")
    fecha=input("Ingrese la fecha: ")
    diagnostico=input("Cual es el diagnostico del paciente: ")
    tratamiento=input("Cual es el tratamiento del pacinete: ")
    curacion=Consulta(fecha,diagnostico,tratamiento, paciente)
    paciente.agregar_consulta(curacion)

def mostrar_datos_paciente():
    name=input("Ingrese el nombre del paciente: ")
    paciente_b=buscar_paciente(name)
    if paciente_b:
        paciente_b.mostrar_datos()
    else:
        print("El paciente no fue encontrado")
        
def mostrar_todo(): 
    if not guardado_paciente: 
        print("No hay estudiantes en la lista")
    for tod in guardado_paciente: 
        tod.mostrar_datos()
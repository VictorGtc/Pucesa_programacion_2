from funciones import pacientes_ingresados, buscar_paciente, datos_clinicos, mostrar_datos_paciente, mostrar_todo
def menu():
    while True:
        print("""
              ===Sistema de Gestión de Consultas Médicas===
              
              1. Ingreso de nuevo paciente al sistemaSA
              
              2. Mostrar datos del pacinete 
              
              3. Mostrar todos los pacientes ingresado 
              
              4 Salir
              
              """)
        opc=int(input("Ingrese su opcion a realizar: "))
        
        if opc ==1:
            nuevo_paciente=pacientes_ingresados()
            datos_clinicos(nuevo_paciente)
        if opc==2:
            mostrar_datos_paciente()
        if opc==3:
            mostrar_todo()
        if opc==4:
            print("Gracias por usar nuestro programa C:")
            break

if __name__=="__main__":
    menu()
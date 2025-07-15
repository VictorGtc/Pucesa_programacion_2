class Persona:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre=nombre
        self.eded=edad
        self.ocupacion=ocupacion
        

    
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.eded}, Ocupacion: {self.ocupacion}"

datos_usuarios=[]

while True:
    
    
    print("""
          
          Menu de nuestro servicion
          
          1. Ingresar nuevos usuarios
          
          2. Ver usuarios ingresados
          
          3. Salir
          
          
          """)
    opc=int(input("Ingrese la opcion a realizar: "))
    
    if opc==1:
        
        datos_usuarios.append(Persona(
            input("Nombre: "),
            int(input("Edad: ")),
            input("Ocupacion: ")
        ))
    if opc==2:
        for i in datos_usuarios:
            print("El usuario ")
class ColaPrioridadHospital:
    def __init__(self):
        self.items = []
    def encolar(self, paciente, prioridad):
        self.items.append((prioridad,paciente))
        print(f"El paciente: {paciente} con prioridad: {prioridad} fue registrado ")

    def esta_vacia(self):
        return len(self.items)==0
    
    def tamaño(self):
        return len(self.items)
    
    def mostrar_pendientes(self):
        if not self.esta_vacia():
            self.items.sort(key=lambda x: x[0])
            atendido=self.items.pop(0)
            
            print(f"Nombre del cliente: {atendido[1]} con su prioridad: {atendido[0]} ")
            return atendido
        else:
            print("No hay mas paciente por este dia")
            return None
    def ingreso_opcion(self):
        try: 
            opc=int(input("\nIngrese la opcion a realizar: "))
        except ValueError:
            print("Valores incorrecto solo numeros")
            return self.ingreso_opcion()
        while opc>4 or opc<1 :
            print("Ingrese solo valores del 1 al 4")
            try: 
                opc=int(input("Ingrese la opcion a realizar : "))
            except ValueError:
                print("Valores incorrecto solo numeros")
        return opc
    def prioridad(self):
        try:
            priori=int(input("""Ingrese la prioridad del cliente 
                              1 Critico
                              2 Urgente
                              3 Moderado
                              4 leve\n
                              : """))
        except ValueError:
            print("Solo valors numericos")
            return self.prioridad()
        while priori>4 or priori<1 :
            print("Ingrese solo valores del 1 al 4")
            try: 
                priori=int(input("Ingrese la prioridad nuevamente: "))
            except ValueError:
                print("Valores incorrecto solo numeros")
        return priori
    def lista_total(self):
        return self.items
        
cola_atencion_cliente=ColaPrioridadHospital()
while True:
    
    print("""
        //===Atención al cliente\\===\n
        1. Agregar cliente
        2. Atencion del ciente
        3. Mostrar clientes en espera
        4. Salir
        """)
    
    opc=cola_atencion_cliente.ingreso_opcion()
            
    if opc==1:
        nombre_cli=input("Ingrese el nombre del paciente: ").lower().strip()
        priori_cli=cola_atencion_cliente.prioridad()
        cola_atencion_cliente.encolar(nombre_cli,priori_cli)
    if opc==2:
        while not cola_atencion_cliente.esta_vacia():
            cola_atencion_cliente.mostrar_pendientes()
    if opc==3:
        print("//==Clientes que aun se encuentran en espera==\\\n")
        lista=cola_atencion_cliente.lista_total()
        cont=0
        if cola_atencion_cliente.tamaño()!=0:
            for i in lista:
                cont+=1
                print(f"Nombre del cleinte: {i[1]} su prioridad es {i[0]}")
        else:
            print("No hay mas clientes por este dia")
    if opc==4:
        print("Gracias por usar nuestro programa vuelva pronto C:")
        break
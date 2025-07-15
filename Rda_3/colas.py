class ColaPrioridadHospital:
    def __init__(self):
        self.items = []
    def encolar(self, paciente, prioridad):
        self.items.append((prioridad,paciente))
        print(f"El paciente: {paciente} con prioridad: {prioridad} fue registrado ")

    def desencolar(self):
        if not self.esta_vacia():
            self.items.sort(key=lambda x: x[0])
            atendido=self.items.pop(0)
            print(f"Se atendio al paciente: {atendido[1]} con su prioridad: {atendido[0]} ")
            return atendido
        else:
            print("No hay mas paciente por este dia")
            return None

    def esta_vacia(self):
        return len(self.items)==0
    def tamaño(self):
        return len(self.items)
    def mostrar_pendientes(self):
        if not self.esta_vacia():
            self.items.sort(key=lambda x: x[0])
            atendido=self.items.pop(0)
            
            print(f"Nombre del paciente: {atendido[1]} con su prioridad: {atendido[0]} ")
            return atendido
        else:
            print("No hay mas paciente por este dia")
            return None


cola_atencion_hospital=ColaPrioridadHospital()
while True:
    
    print("""
        //===Atención hospitalaria\\===\n
        1. Agregar pacientes
        2. Mostrar pacientbes en espera
        3. Atencion del paciente 
        4. Salir
        """)
    
    opc=int(input("Ingrese la opcion ha realziar: "))
    while opc<1 or opc>4:
        try:
            print("Ingrese solo numeros en el rango del 1 al 4\n")
            opc=int(input("Ingrese la opcion nuevamente: "))
        except ValueError:
            print("Solo numeros no ingrese letras, valor invalido ")
            
    if opc==1:
        nombre_paci=input("Ingrese el nombre del paciente: ").lower().strip()
        priori_paci=int(input("""Ingrese la prioridad dle paciente 
                              1 Critico
                              2 Urgente
                              3 Moderado
                              4 leve\n
                              : """))
        cola_atencion_hospital.encolar(nombre_paci,priori_paci)
    if opc==2:
        print("//==Pacientes que aun se encuentran en espera==\\\n")
        while not cola_atencion_hospital.esta_vacia():
            cola_atencion_hospital.mostrar_pendientes()
    if opc==3:
        while not cola_atencion_hospital.esta_vacia():
            cola_atencion_hospital.desencolar()
    if opc==4:
        print("Gracias por usar nuestro programa vuelva pronto C:")
        break
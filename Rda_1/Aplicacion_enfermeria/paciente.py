class Paciente: 
    def __init__(self, nombre, cedula, edad, tipo_sangre):
        self.nombre=nombre
        self.cedula=cedula
        self.edad=edad
        self.tipo_sangre=tipo_sangre
        self.historial_consulta=[]
        
    def agregar_consulta(self, consulta):
        self.historial_consulta.append(consulta)
    
    def mostrar_datos(self):
        print(f"""
              ===Informacion del paciente===
              
              Nombre del paciente : {self.nombre}
              Cedula del paciente : {self.cedula}
              Edad del paciente   : {self.edad}
              Tipo de sangre      : {self.tipo_sangre}
              """)
        if len(self.historial_consulta)==0:
            print("El historial del paciente esta vacia")
        else: 
            for i in self.historial_consulta:
                print(f"""
              ==Historial del paciente==
              Fecha       = {i.fecha}
              Diagnostico = {i.diagnostico}
              Tratamiento = {i.tratamiento}
                      """)
            

class Consulta: 
    def __init__(self, fecha, diagnostico, tratamiento, paciente):
        self.fecha=fecha
        self.diagnostico=diagnostico
        self.tratamiento=tratamiento
        self.paciente=paciente

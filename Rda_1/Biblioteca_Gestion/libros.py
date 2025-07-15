separador="*"*64
class Libros:
    def __init__(self, titulo, autor, ISBM, genero):
        self.titulo=titulo
        self.autor=autor
        self.isbm=ISBM
        self.genero=genero
    
    def mostrar_datos(self):
        print(f"""
              {separador}
              == Libro registrados en el sistema ==
              
              Titulo del libro: {self.titulo}
              Autor del libro : {self.autor}
              ISBN del libro  : {self.isbm}
              Genero del libro: {self.genero}
              
              """)
        
class Prestamo:
    def __init__(self, titulo, fecha, ISBM, cedula):
        self.titulo=titulo
        self.fecha=fecha
        self.isbm=ISBM
        self.cedula=cedula
    
    def mostrar_prestamo(self):
        print(f"""
              ==Libros prestados==
              
              Titulo del libro prestado: {self.titulo}
              Fecha del dia prestado :   {self.fecha}
              ISBM del libro prestado: {self.isbm}
              Cedula de la persona : {self.cedula}
              
              """)
        
        

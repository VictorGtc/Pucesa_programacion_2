from libros import Libros
from libros import Prestamo

libros_guardados=[]

def registrar_libro():
    titulo1 = input("Ingrese el titulo del libro: ")
    autor1 = input("Ingrese el autor del libro: ")
    isbm1 = int(input("Ingrese el ISBM del libro: "))
    genero1= input("Ingrese el genero del libro: ")
    
    libro1=Libros(titulo1,autor1,isbm1,genero1)
    libros_guardados.append(libro1)
    
    print("!!!!! Libro registrado con exito C: !!!!!")
    
def buscar_libro(busar):
    for lib in libros_guardados:
        if lib.isbm == busar:
            return lib
        
def mostrar_libros_registro():
    buscar=int(input("Ingrese el ISBM del libro para realizar la busqueda: "))
    libro_buscado=buscar_libro(buscar)
    if libro_buscado:
        libro_buscado.mostrar_datos()
    else:
        print("Libro no encontrado D:")
    
def mostrar_todos():
    if not libros_guardados:
        print("//// No existen libros registrados ////")
    else:
        for tod in libros_guardados:
            tod.mostrar_datos()
            
lista_prestamos=[]
def agregar_prestamo():
    titulo2=input("Ingrese el titulo del libro: ")
    fecha=input("Ingrese la fecha del día de hoy: ")
    isbm2=input("Ingrese el ISBM del libro prestado: ")
    cedula=int(input("Ingrese la cedula de la persona a quien se presta el lbro: "))
    prestamo1=Prestamo(titulo2,fecha,isbm2,cedula)
    lista_prestamos.append(prestamo1)
    
def mostrar_prestamo():
    for i in lista_prestamos:
        i.mostrar_prestamo()
    



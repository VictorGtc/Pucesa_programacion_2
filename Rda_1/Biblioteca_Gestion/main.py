
from funciones import registrar_libro,buscar_libro,mostrar_libros_registro,mostrar_todos,agregar_prestamo, mostrar_prestamo

separador="*"*64

def main():
    while True:
        print(F"""
            🧠 Sistema de Gestión de Biblioteca Personal
            
            1. Registrar un nuevo libro
            2. Registrar un préstamo
            3. Mostrar información de un libro
            4. Mostrar todos los libros
            5. Mostrar prestamos
            6. Salir del sistema
            
            
            """)
        opc=int(input("Ingrese la opcion a realizar: "))
        
        if opc == 1: 
            registrar_libro()
        
        if opc == 2: 
            agregar_prestamo()
        
        if opc == 3: 
            mostrar_libros_registro()
        
        if opc == 4: 
            mostrar_todos()
        
        if opc == 5: 
            mostrar_prestamo()
        if opc == 6: 
            print("Gracias por usar nuestro sistema Vuelva pronto :D ")
            break

if __name__ == "__main__":
    main()
    
class Vehiculo: 
    def moverse(self):
        print("El auto esta quieto sobre la calle ")
        
class Auto(Vehiculo):
    def moverse(self):
        print("El auto se mueve en sus cuatro llantas ")
        
mi_vehiculo=Vehiculo()
mi_vehiculo.moverse()

mi_vehiculo=Auto()
mi_vehiculo.moverse()

        
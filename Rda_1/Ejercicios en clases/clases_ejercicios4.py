class Pajaro:
    def sonido(self):
        print("Pio Pio")
        
class Gato:
    def sonido(self):
        print("Miauuuuuuu!!!!!")
        
def hace_sonido(animal):
    animal.sonido()
        
pajaro_anim=Pajaro()
gato_anim=Gato()

hace_sonido(pajaro_anim)
hace_sonido(gato_anim)
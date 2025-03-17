# AUTOR: RIQUISIMO

class Animal:
    def comer(self):
        print("El animal esta comiendo")

class Ave(Animal):
    def volar(self):
        print("El animal esta volando")
        
class Mamifero(Animal):
    def amamantar(self):
        print("El animal esta amamantando")
        
class Murcielago(Mamifero, Ave):
    pass

murcielago = Murcielago()
print("murcielago:")
murcielago.comer()
murcielago.volar()
murcielago.amamantar()
print(f"orden de metodos de clase murcielago: {Murcielago.mro()}")

otra_ave = Ave()
print("otra ave:")
otra_ave.comer()
otra_ave.volar()
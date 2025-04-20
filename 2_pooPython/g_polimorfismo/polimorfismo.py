# AUTOR: RIQUISIMO

"""
NOTA: En python todas las variables son polimorfas por el tipado dinamico, a esto se le conoce como
polimorfismo en tiempo de ejecucion o polimorfismo de inclusion
"""
# en los lenguajes de tipado dinamico no es necesario hacer herencia para implementar polimorfismo

"""
Para poder hacer polimorfismo de herencia se deberia hacer esto:
class Animal:
    def sonido(self):
        pass
en python funciona igual si lo ponen o no
"""

"""
para hacer sobrecarga de metodos en java se pone el mismo nombre y varios metodos
en python no se puede hacer eso, solo se usa *args para aceptar n argumentos
"""
class Gato:
    def sonido(self):
        return "miau"
    
class Perro:
    def sonido(self):
        return "guau"

def hacer_sonido(animal):
    print(animal.sonido())

perro = Perro()
gato = Gato()

# CADA UNO IMPRIME SU PROPIO SONIDO AUNQUE HACEN LA MISMA ACCION
hacer_sonido(perro)
hacer_sonido(gato)

# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
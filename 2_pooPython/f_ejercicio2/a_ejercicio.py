# AUTOR: RIQUISIMO

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def imprimir_nombre_edad(self):
        return f"nombre: {self.nombre}, edad: {self.edad}"
    
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad) # NO SE NECESITA PASARLE SELF
        self.grado = grado
    
    def imprimir_grado(self):
        return f"grado: {self.grado}"
    
# MAIN
ricky = Estudiante("Ricky", 32, 4)   
print(ricky.imprimir_nombre_edad() + " " + ricky.imprimir_grado())
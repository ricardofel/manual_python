# AUTOR: RIQUISIMO

"""
NOTA: SI DENTRO DE UNA CLASE SE USA "pass" LA CLASE QUEDA VACIA

- SI UNA CLASE HEREDA DE OTRA SE LLAMA "HERENCIA SIMPLE"

- SI VARIAS CLASES HEREDAN Y DEPENDEN DE UNA SOLA SE LLAMA "HERENCIA JERARQUICA"
"""

# CLASE PADRE O SUPERCLASE
class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad 
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print(f"HOLA, {self.nombre} esta hablando")
        
# CLASE HIJA O SUBCALSE
class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        # A SUPER YA NO SE LE PASA SELF
        super().__init__(nombre,edad,nacionalidad) # LLAMAR AL CONSTRUCTOR DE LA CLASE PADRE
        self.trabajo = trabajo
        self.salario = salario
        
# OTRA CLASE HIJA O SUBCALSE
class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,universidad,calificaciones):
        super().__init__(nombre,edad,nacionalidad) # LLAMAR AL CONSTRUCTOR DE LA CLASE PADRE
        self.universidad = universidad
        self.calificaciones = calificaciones
        
    def mostrar_calificaiones(self):
        for nota in self.calificaciones:
            print(f"NOTA: {nota}")
        


# MAIN
ricky = Empleado("Ricky", 32, "Malago","Desarrollador",2500)
ricky.hablar() # ESTE METODO ESTA EN LA CLASE PADRE, LO HEREDA

piter = Estudiante("Piter", 45, "chileno", "Universidad de Chile", [6,8,8.5])
piter.mostrar_calificaiones() # METODO PROPIO DE LA CLASE HIJA
# AUTOR: RIQUISIMO

"""
- cuando una clase hereda de varias clases se conoce como "herencia multiple"
"""

class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def mostrar_datos(self):
        return f"mi nombre es {self.nombre}, tengo {self.edad} años, soy {self.nacionalidad}"
        
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return f"mi habilidad es {self.habilidad}"

class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, empresa, salario):
        Persona.__init__(self,nombre,edad,nacionalidad) # LLAMAMOS AL CONSTRUCTOR DE LA CLASE PADRE (SE LE DEBE PASAR SELF)
        Artista.__init__(self,habilidad) # LLAMAMOS AL CONSTRUCTOR DE LA CLASE PADRE (SE LE DEBE PASAR SELF)
        self.empresa = empresa
        self.salario = salario
    
    def mostrar_datos_empleo(self):
        return f"trabajo en la empresa {self.empresa} y gano {self.salario} dolares"
        
    def presentarse(self):
        return f"{self.mostrar_datos()} {self.mostrar_habilidad()} {self.mostrar_datos_empleo()}"

# MAIN
gobelio = EmpleadoArtista("Gobelio",25, "Colombiano", "Bailar", "DanceBall", 3500.9)
print(gobelio.presentarse())

# SABER SI UNA CLASE HEREDA DE OTRA
herencia = issubclass(EmpleadoArtista,Artista) # DEVUELVE UN BOOLEANO
print(herencia)

# SABER SI UN OBJETO ES UNA INSTANCIA DE UNA CLASE ESPECIFICA
instancia = isinstance(gobelio,Persona) # DEVUELVE UN BOOLEANO
print(instancia)
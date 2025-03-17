# AUTOR: RIQUISIMO

"""
ESTRUCTURA PARA CREAR UNA CLASE CON SUS METODOS:

class NombreClase:
    # CONSTRUCTOR
    # SIEMPRE SE LE DEBE PASAR EL PARAMETRO self
    def __init__(self,nombre_atributo1,nombre_atributo2,...)
        self.nombre_atributo1 = nombre_atributo1
        self.nombre_atributo2 = nombre_atributo2
    
    # METODOS
    # SIEMPRE SE LE DEBE PASAR EL PARAMETRO self
    def nombre_metodo(self,otro_parametro,...)
        acciones
"""

# DEFINIR UNA CLASE CON SU CONSTRUCTOR ESPECIFICADO
class Celular:
    # CONSTRUCTOR
    # DENTRO DEL CONSTRUCTOR (__init__) SE INICIALIZAN LOS ATRIBUTOS
    # EL METODO __init__ SE EJECUTA SIEMPRE CADA VEZ QUE CREAMOS UN OBJETO
    # self es como el this en java APUNTA AL OBJETO QUE SE ESTA CREANDO
    def __init__(self,marca,modelo,camara):
        self.marca = marca # AQUI SE PUEDEN HACER CAMBIOS A LOS VALORES DE LOS ATRIBUTOS
        self.modelo = modelo
        self.camara = camara 
        
    # METODOS
    # SIEMPRE RECIBEN EL PARAMETRO SELF PARA QUE FUNCIONEN
    def llamar(self):
        print(f"Estas haciendo una llamada con el celular: {self.marca} {self.modelo}")
    
    def cortar(self):
        print(f"Cortaste la llamada del celular: {self.marca} {self.modelo}")

# INSTANCIAR UN OBJETO
# SE LE PASAN TODOS LOS PARAMETROS MENOS SELF
celular1 = Celular("Samsung","S23","48 mp")
celular2 = Celular("Apple","iphone 14 pro max","97 mp")

# IMPRIMIR INFORMACION DE LOS OBJETOS
# ESA FORMA NO ES OPTIMA PARA ACCEDER A LOS ATRIBUTOS DE LOS OBJETOS
print(f"CELULAR 1: {celular1.marca} {celular1.modelo}")
print(f"CELULAR 2: {celular2.marca} {celular2.modelo}")

# EJECUTAR METODOS DE OBJETOS
celular1.llamar()
celular1.cortar()

celular2.llamar()
celular2.cortar()
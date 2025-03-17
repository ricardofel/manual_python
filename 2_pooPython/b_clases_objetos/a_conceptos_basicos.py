# AUTOR: RIQUISIMO

""" 
NOTA:
Antes de llegar a la POO lo mas optimo que se podia era trabajar con matrices para guardar la info
es decir listas de listas, pero manejar la informacion de esta manera es tedioso y poco practico.
"""

"""
DEFINICION DE CLASE Y OBJETO:
CLASE: Plantilla para definir la logistica de un objeto, tanto sus atributos como metodos y restricciones.

OBJETO: Entidad que se crea para aprovechar su naturaleza, es decir sus atributos y comportamientos (metodos).

NOTA: Los objetos se crean a partir de las clases y a ese paso se lo conoce como "Instanciar", y tambien
cabe decir que se pueden instanciar varios objetos de la misma clase, son diferentes elementos, pero tienen
la misma naturaleza porque fueron instaciados de la misma clase.

EXTRA: Entonces a nivel profesional podemos definir a un objeto como "Una instancia de una clase"
"""

"""
ESTRUCTURA PARA DEFINIR UNA CLASE EN PYTHON:
NOTA: La nomenclatura estandar para pyhton es snake_case, pero para los nombres de clases se usa 
PascalCase, para el resto de cosas como atributos, metodos e instanciar objetos se puede usar con 
normalidad snake_case, ESTO RESPETA LA GUIA DE ESTILO PEP 8

NOTA: Cuando no se especifica un constructor python asigna un constructor por defecto 
que no realiza ninguna accion en especifico

class NombreClase:
    nombre_atributo = "contenido"  # Atributo de clase
    
    CUANDO YA SE LE DA UNA VALOR AL ATRIBUTO DIRECTO EN LA CLASE TODOS LOS OBJETOS
    QUE SE INSTANCIEN DE ESA CLASE VAN A TENER EL MISMO VALOR PARA ESE ATRIBUTO, POR ESO
    A ESE TIPO DE ATRIBUTOS SE LOS CONOCE COMO ESTATICOS
"""

# EJEMPLO SENCILLO
class Celular:
    # CUANDO YA SE LES ASIGNA VALOR DIRECTO EN LA CLASE SE LLAMAN "ATRIBUTOS ESTATICOS"
    marca = "Samsung"
    modelo = "S23"
    camara = "48 mp"

# INSTANCIAR UN OBJETO
celular1 = Celular() # OBJETO 1
celular2 = Celular() # OBJETO 2

print(celular1, celular2) # SI SE IMPRIME SOLO SE VE LA DIRECCION EN MEMORIA DEL OBJETO

# SI QUEREMOS ACCEDER A LOS ATRIBUTOS DE ESTOS OBJETOS
# EN ESTE CASO LOS DOS IMPRIMEN LO MISMO PORQUE TIENEN ATRIBUTOS ESTATICOS
print(f"MARCA CELULAR 1: {celular1.marca}\nMARCA CELULAR 2: {celular2.marca}")

# ACCEDER A LOS ATRIBUTOS DIRECTAMENTE:
celular1.camara = "50 mp" # ESTA NO ES UNA PRACTICA RECOMENDADA YA QUE VIOLA EUN PRINCIPIO BASICO DE POO (ENCAPSULAMIENTO)
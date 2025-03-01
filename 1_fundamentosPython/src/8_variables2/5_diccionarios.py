# AUTOR: RIQUISIMO

# CREANDO DICCIONARIOS

# USANDO DICT()
# RECIBE PARAMETROS CLAVE = VALOR
# RESTRICCION: EL TIPO DE DATO DE LAS CLAVES DEBEN SER NO MUTABLES, ES DECIR VALORES QUE NO SE PUEDEN MODIFICAR
# LAS CLAVES PUEDEN SER String, Double, Tuple, etc, pero no list por ejemplo, porque list es un tipo de dato modificable
# PARA METER UN CONJUNTO COMO CLAVE SE DEBE USAR frozenset()

# NOTA: SI SE CREA UN DICCIONARIO VACIO SE PUEDE AGREGAR CUALQUIER TIPO DE DATO EN SUS CLAVES Y VALORES
# DECLARAR DICCIONARIO VACIO:
people = dict()

# AGREGAR VALORES DE DISTINTOS TIPOS:
people["nombre"] = "Ricky"  # str
people["edad"] = 21  # int
people["altura"] = 1.75  # float
people["es_estudiante"] = True  # bool
people["hobbies"] = ["Programar", "Jugar", "Leer"]  # list
people["direccion"] = {"calle": "Av. Central", "numero": 123}  # otro dict

# CREAR UN DICCIONARIO VACIO PERO ESPECIFICANDO LOS TIPOS DE DATO:
from typing import Dict, Any # SE DEBEN IMPORTAR LOS TIPOS DE DATO PARA PODER USARLOS
people2: Dict[str, Any] = dict()
# AGREGAR VALORES DE CUALQUIER TIPO
people2["nombre"] = "Ricky"  # str
people2["edad"] = 21  # int
people2["altura"] = 1.75  # float

# CREAR UN DICCIONARIO SOLO ESPECIFICANDO LAS CLAVES CON dict.fromkeys
# RECIBE UN ITERABLE
diccionario12 = dict.fromkeys(["Clave1", "Clave2"])
print(diccionario12)
# SI LE PASO DOS VALORES dict-fromkeys("ABC", 1) VA A ITERAR EL PRIMER ELEMENTO E IGUALAR TODOS AL SEGUNDO
# ES DECIR: A = 1, B = 1, C = 1
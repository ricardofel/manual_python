#AUTOR: RIQUISIMO

"""
DATOS SIMPLES:
"""
# STRING:
"String", 'String' # CADENAS NORMALES
"""String""", '''String''' # CADENAS MULTILINEA

#NUMERICOS:
r = 10 # (int)
y = 10.56 # (float)
print("SUMA DE INT Y FLOAT: " + str(r / y))

# COMPLEJOS:
z = 2 + 3j  # NUMERO COMPLEJO
print("NUMEROS COMPLEJOS:")
print("PARTE REAL DEL NUMERO COMPLEJO: " + str(z.real))  # MUESTRA LA PARTE REAL
print("PARTE IMAGINARIA DEL NUMERO COMPLEJO: " + str(z.imag)) # MUESTRA LA PARTE IMAGINARIA

#BOOLEANOS:
True, False

# ANY: ANY ESPECIFICA UN CAMPO PARA METER CUALQUIER OTRO TIPO DE DATO, ES UN TIPO DE DATO GENERICO

"""
DATOS COMPUESTOS:
"""

from typing import List, Tuple # SE DEBEN IMPORTAR LOS TIPOS DE DATO PARA PODER USARLOS

# LISTAS (list):
# SE PUEDEN MODIFICAR LUEGO DE SU CREACION
numeros = [1, 2, 3, 4, 5]
nombres = ["Ricky", "Python", "Code"]
mezcla = [10, "Hola", True, 3.14]
numeros[1] = 100  # ACCEDE A LA POSCICION 1 Y CAMBIA EL ELEMENTO
print("LISTAS: ")
print("ELEMENTO POSICION 1 DE LA LISTA: " + str(numeros[1])) # ACCEDE A LA POSICION E IMPRIME EL ELEMENTO

# DECLARAR UNA LISTA VACIA ESPECIFICANDO EL TIPO DE DATO:
numeros2: List[int] = []  # Lista vacía que solo acepta enteros



# TUPLAS (tuple):
# NOTA: SE DECLARAN CON () Y NO CON []
# NO SE PUEDEN MODIFICAR SUS ELEMENTOS POR SEPARADO UNA VEZ CREADAS PERO SI SE PUEDE ACCEDER A ELLOS
coordenadas = (10, 20)
colores = ("rojo", "verde", "azul")
tupla = (12, "Ricky", True, 23.76) # LAS TUPLAS TAMBIEN PUEDEN TENER VARIOS TIPOS DE DATOS DENTRO
print(f"PRIMER ELEMENTO DE LA TUPLA COLORES: {colores[0]}")

# DECLARAR UNA TUPLA ESPECIFICANDO LOS TIPOS DE DATOS
persona: Tuple[int, str, bool, float] = (12, "Ricky", True, 23.76)



# CONJUNTOS (set):
# NOTA: SE DECLARAN CON {} Y NO CON []
# COLECCION DESORDENADA DE ELEMENTOS UNICOS, ES DECIR NO TOMA DUPLICADOS
# NO SE PUEDEN MODIFICAR SUS ELEMENTOS POR SEPARADO UNA VEZ CREADAS NI TAMPOCO ACCEDER A ELLOS USANDO SU INDICE
# PARA ACCEDER A LOS ELEMENTOS SE DEBE USAN UN BUCLE
frutas = {"manzana", "pera", "uva", "manzana", "pera", "uva", "manzana"}
print(f"CONJUNTO: {frutas}")  # IMPRIME ELIMINANDO DUPLICADOS


# NOTA: LAS TUPLAS Y CONJUNTOS SI SE PUEDEN MODIFICAR GLOBALMENTE COMO VARIABLES
# LO QUE NO SE PUEDE MODIDIFICAR SON SUS ELEMENTOS POR SEPARADO



# DICCIONARIOS (dict)
# COLECCION DE PARES CLAVE,VALOR (COMO LOS MAPAS EN SCALA)
persona = {
    "nombre": "Ricky",
    "edad": 21,
    "ciudad": "México"
}
print(f"ELEMENTO DEL DICCIONARIO: {persona["nombre"]}")  # ACCEDE AL VALOR USANDO LA CLAVE Y LO IMPRIME

# SABER UN TIPO DE DATO
tipoDato1 = type("Hola")
tipoDato2 = type(r)
tipoDato3 = type(z)
tipoDato4 = type(True)
tipoDato5 = type(nombres)
tipoDato6 = type(colores)
tipoDato7 = type(frutas)
tipoDato8 = type(persona)
tipoDato9 = type(y)

print(f"TIPO DE DATO 1: {tipoDato1}")
print(f"TIPO DE DATO 2: {tipoDato2}")
print(f"TIPO DE DATO 3: {tipoDato3}")
print(f"TIPO DE DATO 4: {tipoDato4}")
print(f"TIPO DE DATO 5: {tipoDato5}")
print(f"TIPO DE DATO 6: {tipoDato6}")
print(f"TIPO DE DATO 7: {tipoDato7}")
print(f"TIPO DE DATO 8: {tipoDato8}")
print(f"TIPO DE DATO 9: {tipoDato9}")
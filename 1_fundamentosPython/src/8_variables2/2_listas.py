# AUTOR: RIQUISIMO

"""
EN PYTHON LOS TIPOS DE DATO TAMBIEN SE CALSIFICAN EN:

MUTABLES: SE PUEDEN CAMBIAR UNA VEZ CREADOS
list (listas)
dict (diccionarios)
set (conjuntos)
bytearray (arreglos de bytes)
memoryview (vista de memoria)

INMUTABLES: NO SE PUEDEN CAMBIAR UNA VEZ CREADOS
int (enteros)
float (flotantes)
complex (números complejos)
bool (booleanos)
str (cadenas de texto)
tuple (tuplas)
frozenset (conjuntos inmutables)
bytes (secuencias de bytes)
NoneType (el tipo del valor None)
"""

"""
En Python, cuando asignas una lista que ya está en una variable a otra variable, 
ambas variables apuntan a la misma lista en memoria. Esto significa que cualquier 
cambio realizado en la lista a través de una de las variables se reflejará en la otra.
LISTAORIGINAL = [9,8,7,6]
LISTACOPIA = LISTAORIGINAL
LISTAORIGINAL.sort()
print(f"LISTA ORIGINAL: {holitap}, LISTA ORDENADA: {hola}")
EN EL PRINT LAS DOS LISTAS VAN A MOSTRAR LO MISMO, A PESAR DE QUE SE QUISO GUARDAR UNA COPIA
PARA GUARDAR UNA COPIA DE UNA LISTA SE USA .copy()

En Python, los tipos de datos que tienen el comportamiento de referencia en memoria 
(es decir, que al asignarlos a otra variable, ambas variables apuntan al mismo objeto 
en memoria) son los tipos de datos mutables. 
"""
# AUTOR: RIQUISIMO

"""
DESEMPAQUETADO: OBTENER ELEMENTOS DE UNA ESTRUCTURA DE DATOS
"""

# TUPLA
datos = ("Ricky", "Balboa", 32)

# DESEMPAQUETAR
nombre, apelllido, edad = datos

# MOSTRANDO DATOS
print(f"NOMBRE: {nombre}, APELLIDO: {apelllido}, EDAD: {edad}")
"""
SOLO FUNCIONA CUANDO SE ASIGNA EL MISMO NUMERO DE VARIABLES QUE ELEMENTOS DE LA LISTA
ESTO YA NO FUNCIONA:
nombre2, apellido2, edad2, genero = datos

- ESTO FUNCIONA CON:
LISTAS, TUPLAS, DICCIONARIOS

- PARA HACER ESTO CON CONJUNTOS PRIMERO SE DEBE CONVERTIR EN LISTA CON list()
"""
# AUTOR: RIQUISIMO

# FORMA PARA VER EN QUE DIRECTORIO SE ESTA TRABAJANDO
#import os
#print("Directorio de trabajo actual:", os.getcwd())

# LEER UN ARCHIVO .txt (COMPLETO)
# RETORNA LA INFO DEL ARCHIVO TAL CUAL
data = open("src/14_archivos/data.txt",encoding="UTF-8")
dataLista = data.read()
print(dataLista)
"""
NOTA: ESTA ES LA FORMA MAS LEGIBLE PARA ABRIR UN ARCHIVO, PRIMERO ABRIRLO EN UNA VARIABLE Y LUEGO LEERLO EN OTRA
"""
# SIEMPRE ES RECOMENDABLE LUEGO CERRARLO
data.close()

# NOTA: CUANDO YA SE LEE UNA VEZ EL ARCHIVO NO PERMITE LEERLO DE NUEVO
# LEER EL ARCHIVO POR LINEAS
# RETORNA UNA LISTA CON LAS LINEAS COMO ELEMENTOS
lineas = open("src/14_archivos/data.txt",encoding="UTF-8").readlines()
print(lineas)
# ACCEDER A UNA LINEA DEL ARCHIVO:
print(lineas[1]) # SE ACCEDE A LA POSICION DE LA LINEA COMO ELEMENTO

# LEER EL ARCHIVO POR CARACTERES, DEVUELVE LA CANTIDAD DE CARATERES ESPECIFICADOS
linea = open("src/14_archivos/data.txt",encoding="UTF-8").readline(24)
print(linea)

# LEER LA PRIMERA LINEA DEL ARCHIVO
# NOTA: EN ARCHIVOS MUY GRANDES PUEDE CONSUMIR TODA LA MEMORIA:
archivoxChars = open("src/14_archivos/data.txt",encoding="UTF-8").readline()
print(archivoxChars)


# AUTOR: RIQUISIMO

"""
PARA EVEITAR USAR .CLOSE A CADA RATO PYTHON NOS OFRECE TRABAJAR CON WITH-OPEN
ESTRUCTURA:
with open("ruta",formatoLectura) as variableDondeSeAbre:
    contenido = variableDondeSeAbre.read()
    print(contenido)

USANDO WITHOPEN YA NO ES NECESARIO CERRARLO CON CLOSE
"""
# ABRIR EL ARCHIVO
with open("src/14_archivos/data.txt",encoding="UTF-8") as archivo:
    # LEER EL ARCHIVO
    contenido = archivo.read()
    # MOSTRAR EL ARCHIVO
    print(contenido)
# AUTOR: RIQUISIMO

# CREAR UNA EXCEPCION PROPIA
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Increible chico, cometiste el siguiente error: {err}")

# EJECUTAR A PROPOSITO LA EXCEPCION
try:
    raise MiExcepcion("AQUI SE MUESTRA EL ERROR DEFINIDO POR MI")
except:
    print("EXCEPCION")
# AUTOR: RIQUISIMO

diccionario = {
    "nombre" : "Ricky",
    "apellido" : "Balboa",
    "edad" : 21
}

# KEYS
# DEVUELVE UN OBJETO DE TIPO DICT_KEYS
# DEVUELVE TODAS LAS CLAVES DEL DICCIONARIO
claves = diccionario.keys()
print(f"CLAVES DEL DICCIONARIO: {claves}")

# GET
# DEVUELVE EL VALOR UNA VEZ INGRESADA LA CLAVE
# SI NO LO ENCUENTRA LANZA UN OBJETO DE TIPO NONE
print(f"nombre: {diccionario.get("nombre")}")

# POP
# ELIMINA UNA CLAVE-VALOR DEL DICCIONARIO
diccionario.pop("edad")
print(f"DICCIONARIO ACTUALIZADO CON POP(): {diccionario}")

# CAMBIAR EL VALOR DE UN DICCIONARIO
diccionario["nombre"] = "Rodrigo"
print(f"VALOR ACTUALIZADO: {diccionario}")

# ITEMS
# DEVUELVE UN OBJETO DICT_ITEMS
# OBTIENE UN OBJETO ITERABLE DEL DICCIONARIO
iterable = diccionario.items()
print(f"ITERABLE: {iterable}")

# CLEAR
# ELIMINA TOPO DEL DICCIONARIO, LO DEJA SIN ELEMENTOS
diccionario.clear()
print(f"DICCIONARIO VACIADO CON CLEAR(): {diccionario}")
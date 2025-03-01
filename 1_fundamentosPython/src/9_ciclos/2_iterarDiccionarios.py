# AUTOR: RIQUISIMO

# EJEMPLO 1
diccionario = {
    "nombre": "Ricky",
    "apellido": "Balboa",
    "edad": 32
}

# ITEMS CONVIERTE AL INDICE EN UNA TUPLA (CLAVE, VALOR)
for key in diccionario.items():
    print(f"CLAVE: {key[0]}, VALOR: {key[1]}")
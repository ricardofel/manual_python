# AUTOR: RIQUISIMO
from string import printable

# CREANDO TUPLAS

# TUPLE()
# CONVERTIR OBJETOS(LISTAS, ETC) A TUPLAS
# ESPERA UNA LISTA
tupla = tuple(["Ricky", "Balboa", 56])
print(type(tupla),tupla)

# OTRAS FORMAS
# SOLO SEPARANDO CON COMAS
tupla2 = "Ricky", "Creed", 88
print(type(tupla2),tupla2)

# CUANDO SE CREA CON UN SOLO ELEMENTO
tupla3 = "Ricky", # DEBE TENER LA COMA AL FINAL
print(type(tupla3),tupla3)

"""
LAS TUPLAS SON MAS EFICIENTES AL TRABAJAR CON LA MEMORIA QUE LAS LISTAS
"""
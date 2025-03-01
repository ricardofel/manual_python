# AUTOR: RIQUISIMO

# CREANDO CONJUNTOS (SET)
# DELCARAR UN CONJUNTO VACIO
data = set()

conjunto = set(["Dato1", "Dato2"])
print(type(conjunto), conjunto)

# METER UN CONJUNTO DENTRO DE OTRO CONJUNTO
conjunto1 = frozenset(["Dato1", "Dato2", "Dato3"]) # LO CONVIERTE EN UN CONJUNTO INMUTABLE
conjunto2 = {conjunto1, "Dato4"}
print(conjunto2)

# VERIFICAR SI UN CONJUNTO ES SUBCONJUNT0 DE OTRO
conjunto3 = {1, 2, 3, 4, 5}
conjunto4 = {1, 2, 3}
verificacion = conjunto4.issubset(conjunto3)
verificacion2 = conjunto4 <= conjunto3 # OTRA FORMA DE HACER LA MISMA OPERACION
print(f"ES SUBCONJUNTO?: {verificacion}")
print(f"ES SUBCONJUNTO?: {verificacion2}")

# VERIFICAR SI UN CONJUNTO ES SUPERCONJUNTO DE OTRO
verificacion3 = conjunto3.issuperset(conjunto4)
verificacion4 = conjunto3 >= conjunto4 # OTRA FORMA DE HACER LA MISMA OPERACION
print(f"ES SUPERCONJUNTO?: {verificacion3}")
print(f"ES SUPERCONJUNTO?: {verificacion4}")

# VERFICAR SI HAY SOLO UN NUMERO EN COMUN
verificacion5 = conjunto3.isdisjoint(conjunto4)
print(f"LOS CONJUNTOS SON DISTINTOS?: {verificacion5}")
# SIEMPRE QUE NO HAYA NINGUN ELEMENTO EN COMUN DARA TRUE
# AUTOR: RIQUISIMO

"""
LAS FUNCIONES INTEGRADAS TAMBIEN CONOCIDAS COMO BUILD IN, SON FUNCIONES NATIVAS DE PYHTON QUE PODEMOS USAR
CUANDO LAS QUERRAMOS, NO HACE FALTA DEFINIRLAS NI TRABAJARLAS ANTES DE LLAMARLAS

- LA DIFERENCIA CON LOS METODOS ES QUE ELLOS SON PROPIOS DE UNA CLASE Y SE USAN SOLO CON OBJETOS DE ESA CLASE
- LANS FUNCIONES BUILD IN SON NATIVAS DE PYHTON

NOTA: A LO LARGO DE TODO EL APRENDIZAJE YA HEMOS USADO FUNCIONES PROPIAS AL TRABAJAR LOS EJEMPLOS EN LAS CARPETAS ANTERIORES
"""
cadena1 = "Holita soy Ricky"
# DIR
# DEVUELVE UNA LISTA DE ATRIBUTOS Y METODOS DISPONIBLES PARA EL OBJETO QUE LE PASAMOS
# FUNCIONA PARA CUALQUIER DATO, NO SOLO STRING
result1 = dir(cadena1)
print(f"LISTA DE ACCIONES DISPONIBLES PARA \"{cadena1}\": {result1}")
# FUNCIONA CON CUALQUIER TIPO DE DATO, NO SOLO CON STRING
result2 = dir(43.76)
print(f"LISTA DE ACCIONES DISPONIBLES PARA 43.76: {result2}")

# LEN
# DEVUELVE
# NOS DA LA LONGITUD EN CARACTERES DE UNA CADENA
result11 = len(cadena1)
print(f"Longitud de la cadena: \"{cadena1}\": {result11}")

# LIST
# CONVIERTE EL ELEMENTO QUE LE METAN A UNA LISTA
tupla = (3,4,5,7)
listaUnida = list(tupla)
print(f"LISTA CREADA: {listaUnida}")

lista1 = [1, 2, 3, 4, 5]
lista4 = [14, 7, 3, 9, 5]
# LEN
# DEVUELVE UN ENTERO
# DEVUELVE LA CANTIDAD DE ELEMENTOS DE LA LISTA
print(f"LONGITUD DE LA LISTA: {len(lista1)}")

# SORTED
# DEVUELVE UNA NUEVA LISTA
# ORDENA LA LISTA SIN MODIFICAR EL ORIGINAL
lista_ordenada = sorted(lista4)
print(f"LISTA ORIGINAL: {lista4}\nLISTA ORDENADA CON LA FUNCION SORTED(): {lista_ordenada}")
# TAMBIEN ADMITE EL PARAMETRO REVERSE
lista_ordenada = sorted(lista4, reverse=True)
print(f"LISTA ORDENADA CON LA FUNCION SORTED() + REVERSE: {lista_ordenada}")
"""
LA DIFERENCIA CON .SORT ES QUE ESTA FUNCION DEVUELVE UNA NUEVA LISTA
.SORT SOLO MODIFICA LA FUNCION ORIGINAL
"""

# MAX
# ENCONTRANDO EL NUMERO MAYOR DE UNA LISTA DE NUMEROS
# DEVUELVE UNA EXCEPCION SI ESTA MAL EL PARAMETRO
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numMasAlto = max(numeros)
print(f"NUMERO MAS ALTO DE LA LISTA {numeros}: {numMasAlto}")

# MIN
# ENCUENTRA EL MENOR DE UNA LISTA DE NUMEROS
# DEVUELVE UNA EXCEPCION SI ESTA MAL EL PARAMETRO
lista = [5, 10, 15, 20, 25, 30]
numMasBajo = min(lista)
print(f"NUMERO MAS BAJO DE LA LISTA {lista}: {numMasBajo}")

# ROUND
# REDONDEAR A UNA CANTIDAD DE DECIMALES DESEADA
numeroDecimal = 34.8974354
print(f"NUMERO REDONDEADO: {round(numeroDecimal, 2)}")

# CONVERTIR TIPOS DE DATO
# int()
num_str = "123"
num_int = int(num_str)
print(f"Convertido a entero: {num_int} (tipo: {type(num_int)})")

# float()
num_str = "123.45"
num_float = float(num_str)
print(f"Convertido a float: {num_float} (tipo: {type(num_float)})")

# bool()
num = 0
bool_val = bool(num)
print(f"Convertido a booleano: {bool_val} (tipo: {type(bool_val)})")

# list()
tupla = (1, 2, 3)
lista = list(tupla)
print(f"Convertido a lista: {lista} (tipo: {type(lista)})")

# set()
lista = [1, 2, 2, 3, 4]
conjunto = set(lista)
print(f"Convertido a conjunto: {conjunto} (tipo: {type(conjunto)})")

# tuple()
lista = [1, 2, 3]
tupla = tuple(lista)
print(f"Convertido a tupla: {tupla} (tipo: {type(tupla)})")

# str()
num = 123
cadena = str(num)
print(f"Convertido a cadena: {cadena} (tipo: {type(cadena)})")

# dict()
lista_pares = [("clave1", "valor1"), ("clave2", "valor2")]
diccionario = dict(lista_pares)
print(f"Convertido a diccionario: {diccionario} (tipo: {type(diccionario)})")

# ALL (COMPRUEBA SI TODOS LOS ELEMENTOS SON VERDADEROS)
# RECIBE UN ITERABLE
# DEVUELVE TRUE SI TODOS LOS ELEMENTOS SON VERDADEROS
# DEVUELVE FALSE SI SOLO UN ELEMENTO ES FALSO
# Lista con todos los elementos verdaderos
lista1 = [True, 1, "hola", [1, 2, 3]]
resultado1 = all(lista1)
print(f"Todos los elementos de lista1 son verdaderos?: {resultado1}")

# Lista con al menos un elemento falso
lista2 = [True, 0, "hola", [1, 2, 3]]
resultado2 = all(lista2)
print(f"Todos los elementos de lista2 son verdaderos?: {resultado2}")

# Lista vacía (se considera que todos los elementos son verdaderos)
lista3 = []
resultado3 = all(lista3)
print(f"Todos los elementos de lista3 son verdaderos?: {resultado3}")

# SUM
# SUMA TODOS LOS VALORES DE UN ITERABLE
# DEVUELVE UNA EXCEPCION SI ESTA MAL EL PARAMETRO
sumatoriaLista = sum(lista)
print(f"SUMATORIA DE TODOS LOS ELEMENTOS DE: {lista}: {sumatoriaLista}")
# AUTOR: RIQUISIMO

"""
UN CICLO O BUCLE EN PROGRAMACION ES UNA ESTRUCTURA DE CONTROL PARA PODER ITERAR ELEMENTOS
DE MANERA CONTROLADA (VALGA LA REDUNDANCIA), PARA QUE UN ELEMENTO SEA ITERABLE DEBE CONTENER
ELEMENTOS INDEPENDIENTES DENTRO DE SI PARA QUE SE PUEDA IR PASANDO UNO POR UNO

- EN PYTHON LOS TIPOS DE DATO ITERABLES SON:
Listas (list)
Tuplas (tuple)
Cadenas de texto (str)
Diccionarios (dict)
Conjuntos (set)
Rangos (range)
Archivos (objetos de archivo)
Generadores (objetos que implementan el protocolo del iterador)

PARA SABER SI UN OBJETO ES ITERABLE SE PUEDE USAR LA FUNCION iter()
NOTA: SI NO ES ITERABLE iter() lanza un error, controlar con excepciones

NOTA: ITERABILIDAD Y MUTABILIDAD SON CONCEPTOS INDEPENDIENTES
(LO ACLARO PORQUE LLEGUE A CONSIDERARLO)
"""

"""
BUCLE FOR

- ESTE CICLO NATURALMENTE NO PUEDE VOLVERSE INFINITO PORQUE SOLO ITERA ESTRUCTURAS FINITAS

ESTRUCTURA:
FOR "nombreVariable" IN "nombreIterable":
    ACCION 
"""
# EJEMPLO 1
animales = ["Condor Andino", "Oso de anteojos", "Piquero de patas azules", "Tigrillo", "Iguana"]
for animal in animales:
    print(f"ANIMAL ECUATORIANO: {animal}")

# EJEMPLO 2
nums = [1, 2, 3, 4, 5]
for current in nums:
    current *= 2
    print(f"NUMERO ACTUAL: {current}")

# EJEMPLO 3
# RECORRER DOS O MAS LISTAS A LA VEZ
# PARA USAR ZIP LAS DOS LISTAS DEBEN TENER EL MIMSO TAMAÑO
# NOTA: LAS DOS SE ITERAN AL MISMO TIEMPO
for numero, animal in zip(nums, animales):
    print(f"ANIMAL NUMERO {numero}: {animal}")

# USANDO RANGE
for num in range(10, 15): # NO TOMA EL EXTREMO SUPERIOR: ES DECIR NO IMPRIME EL 15
    print(f"NUMERO ACTUAL: {num}")
# NOTA: TAMBIEN SE LE PUEDE PASAR TRES PARAMETROS:
# range(desde, hasta, incremento)

# SI SOLO LE ENVIAMOS UN NUMERO ARRANCA DESDE 0 HASTA ESE NUMERO
for num in range(3):
    print(f"NUMERO: {num}")

# USANDO INDICES

# FORMA NO OPTIMA DE RECORRER LISTAS CON INDICES
# ESTO NO FUNCIONA CON CONJUNTOS PORQUE NO SE PUEDE ACCDER A ELLOS POR INDICE
for num in range(len(animales)):
    print(f"ANIMAL ECUATORIANO CHEVERE: {animales[num]}")

# FORMA OPTIMA DE RECORRER LISTAS CON INDICES
# enumerate CONVIERTE LA VARIABLE INDICE EN UNA TUPLA (INDICE, VALOR)
# FORMA PARA RECORRER CONJUNTOS
for num in enumerate(animales):
    print(f"INDICE: {num[0]}, VALOR: {num[1]}")

# USANDO ELSE
# SIEMPRE SE VA A EJECUTAR INDEPENDIENTEMENTE SI EL BUCLE SE EJECUTA O NO
# SI HAY UN BREAK YA NO SE EJECUTA
for num in enumerate(animales):
    print(f"INDICE: {num[0]}, ANIMAL: {num[1]}")
else:
    print(f"BUCLE COMPLETO")

# USANDO CONDICIONALES ANIDADOS

# continue
# CONTINUE HACE HACE QUE EL BUCLE IGNORE EL RESTO DE INSTRUCCIONES Y PASE A LA SIGUIENTE VUELTA
frutas = ["Ciruela", "Uva", "Manzana", "Pera", "Papaya"]
for fruta in frutas:
    if fruta == "Uva":
        continue # CUANDO ENTRE AQUI VA DIRECTO A LA SIGUIENTE VUELTA
    print(f"FRUTA: {fruta}")

# break
# ROMPE EL CICLO Y LO TERMINA
for fruta in frutas:
    print(f"FRUTITAS: {fruta}") # SOLO VA A IMPRIMRIR HASTA PERA
    if fruta == "Pera":
        break # SI ENTRA AQUI EL CICLO TERMINA
else:
    print("TERMINADO") # CUANDO HAY UN BREAK EL ELSE NO SE EJECUTA

# RECORRER STRINGS (TAMBIEN SON ITERABLES)
# SE RECORREN POR CARACTERES
count = 0
for letra in "Riquisimo":
    count += 1
print(f"CANTIDAD DE LETRAS EN LA CADENA \"Riquisimo\": {count}") # ESTO SE PUEDE HACER FACIL CON LEN() (YA LO SE)

# FOR EN UNA SOLA LINEA
# FORMA TRADICIONAL:
nums = [1, 2, 3, 4, 5]
numsDuplicados = list()
for num in nums:
    numsDuplicados.append(num * 2)
print(numsDuplicados)

# FORMA ABREVIADA EN UNA SOLA LINEA:
# VA DENTRO DE UNA LISTA []
numsDuplicados = [x * 2 for x in nums]
print(numsDuplicados)
"""
TODO LO ANTERIOR FUNCIONA EXACTAMENTE IGUAL PARA ITERAR LISTAS, TUPLAS Y CONJUNTOS
"""
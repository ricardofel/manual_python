# AUTOR: RIQUISIMO

lista1 = ["Ricky", 5, 6.8, True]
lista2 = [34, 32, 20, 15, 9, 7, 3, 1]
lista4 = [9, 8, 7, 6, 5, 4]

# NOTA: ALGUNOS METODOS QUE SON PARA STRINGS, TAMBIEN SIRVEN PARA LISTAS O TAMBIEN FUNCIONES COMO LEN()
# PARA ESTAR SEGURO DE QUE SE PUEDE HACER CON UN OBJETO USAR dir()

# LAS LISTAS SON ESTRUCTURAS DE DATOS QUE ENCIERRAN VARIOS ELEMENTOS DENTRO DE SI

# ZIP
# DEVUELVE UNA LISTA DE TUPLAS
# COMBINA LOS ELEMENTOS DE DOS LISTAS
numeros = [1, 2, 3, 4] # AL 4 LO IGNORA PORQUE NO ENCUENTRA UN ELEMENTO CORRESPONDIENTE EN "letras"
letras = ['a', 'b', 'c']
combinados = list(zip(numeros, letras))
print(f"LISTAS COMBINADAS CON zip(): {combinados}")

# METODOS

# APPEND
# NO DEVUELVE NADA, SOLO AGREGA EL ELEMENTO INTERNAMENTE
# AGREGA UN ELEMENTO AL FINAL DE LA LISTA
lista1.append("Holita")
print(f"ELEMENTO \"Holita\" AGREGADO CON APPEND: {lista1}")

# INSERT
# NO DEVUELVE NADA, SOLO AGREGA EL ELEMENTO INTERNAMENTE
# AGREGA UN ELEMENTO A LA LISTA EN UN INDICE ESPECIFICO
lista1.insert(2, "Hey") # INDICE, ELEMENTO
print(f"ELEMENTO \"Hey\" AGREGADO CON INSERT: {lista1}")

# EXTEND
# NO DEVUELVE NADA, SOLO AGREGA EL ELEMENTO INTERNAMENTE
# AGREGA LOS ELEMENTOS DE UNA LISTA AL FINAL DE OTRA LISTA (COMBINA DOS LISTAS)
listaExtra = [True, False, "Maria", 23.7]
lista1.extend(listaExtra) # LISTAORIGINAL.EXTEND(LISTAAGREGADA)
print(f"ELEMENTO \"{listaExtra}\" AGREGADO CON EXTEND: {lista1}")

# POP
# NO DEVUELVE NADA, SOLO AGREGA EL ELEMENTO INTERNAMENTE
# ELIMINA UN ELEMENTO DE LA LISTA POR SU INDICE
elementoEliminado = lista1[1]
lista1.pop(1)
print(f"ELEMENTO EN LA POSICION 1 \"{elementoEliminado}\": ELIMINADO CON POP: {lista1}")
# TECNICAS PARA ELIMINAR DATOS ESPECIFICOS
# ELIMINAR EL ULTIMO ELEMENTO DE LA LISTA SI NO SABEMOS QUE INDICE TIENE
lista1.pop(-1) # SE UBICA EL INDICE -1
print(f"ULTIMO ELEMENTO ELIMINADO CON POP: {lista1}")
# ELIMINAR EL PEULTIMO ELEMENTO DE LA LISTA SI NO SABEMOS QUE INDICE TIENE
lista1.pop(-2) # SE UBICA EL INDICE -2
print(f"PENULTIMO ELEMENTO ELIMINADO CON POP: {lista1}")

# REMOVE
# NO DEVUELVE NADA, SOLO AGREGA EL ELEMENTO INTERNAMENTE
# REMUEVE UN ELEMENTO DE LA LISTA POR SU VALOR
# SI SE LE PASA UN ELEMENTO QUE NO EXISTE BOTA UN ERROR
lista1.remove("Hey")
print(f"ELEMENTO \"Hey\" ELIMINADO CON REMOVE: {lista1}")

# COPY
# DEVUELVE UN NUEVO DATO Y CREA UNA NUEVA DIRECCION EN MEMORIA
listaCopia = lista2.copy()
print(f"LISTA CLONADA EN UNA NUEVA VARIABLE: {listaCopia}")
# NOTA: SI SOLO ASIGNO LA LISTA A LA VARIABLE, NO SE CREA UNA NUEVA DIRECCION EN MEMORIA
# POR LO TANTO SI HAGO UN CAMBIO LA NUEVA VARIABLE TAMBIEN SE VA A CAMBIAR


# SORT
# ORDENA LOS ELEMENTOS EN FORMA ASCENDENTE
# FUNCIONA SOLO CON LISTAS DE VALORES NUMERICOS
lista2.sort()
print(f"LISTA ORIGINAL: {listaCopia} \nLISTA ORDENADA CON SORT: {lista2}")
# REVERSE COMO PARAMETRO DE SORT
# ES UN BOOLEANDO QUE SE ACTIVA CON TRUE
# FUNCIONA CON SORT PARA ORDENARLOS ALREVES
lista2.sort(reverse=True)
print(f"LISTA ORDENADA CON SORT APLICANDO REVERSE: {lista2}")
"""
PARAMETROS QUE PUEDE RECIBIR .SORT()
key: Una función que sirve como clave para la comparación. Esta función toma un solo argumento y devuelve un valor 
que se usará para la comparación. 
Por ejemplo, key = lambda x: x[1] ordenará una lista de tuplas por el segundo elemento de cada tupla.  

EJEMPLO DE USO DE KEY:
# Lista de números
numeros = [1, -2, 3, -4, 5]

# Ordenar por el cuadrado de cada número
numeros.sort(key=lambda x: x**2)
print(f"Lista ordenada por el cuadrado de los números: {numeros}")

reverse: Un valor booleano que, si se establece en True, ordenará la lista en orden descendente. 
El valor predeterminado es False
"""


# REVERSE
# INVIERTE EL ORDEN DE LOS ELEMENTOS EN LA LISTA, NO LEE LOS VALORES, SOLO LOS INVIERTE POR INDICES
lista3 = [2, 6, 0, 1, 9, 7, 98, 24] # LISTA SIN UN ORDEN
lista3.reverse()
print(f"LISTA ORDENADA APLICANDO REVERSE COMO METODO: {lista3}")

# CLEAR
# NO DEVUELVE NADA, SOLO AGREGA EL ELEMENTO INTERNAMENTE
# ELIMINA TODOS LOS ELEMENTOS DE LA LISTA Y LA DEJA VACIA
lista1.clear()
print(f"LISTA VACIADA CON CLEAR: {lista1}")

"""
PARA MANIPULAR TUPLAS Y CONJUNTOS ES BASTANTE SIMILAR A LAS LISTAS
PERO HAY ALGUNOS QUE NO SE PUEDEN UTILIZAR POR LA NATURALEZA DE ESOS DATOS
RECORDANDO QUE LAS TUPLAS Y CONJUNTOS SON DATOS INMUTABLES
"""


# SLICING
# TECNICA PARA OBTENER PORCIONES DE SECUENCIAS DE DATOS USANDO [] Y :
# EJEMPLO:
ejemplo = [10,20,30,40,50]
print(ejemplo[1:3]) # IMPRIME 20 Y 30 (incluye el indice inferior, no inlcuye el indice superior)
# NOTA: secuencia[inicio:fin:paso] TAMBIEN SE PUEDE ESPECIFICAR EL INCREMENTO DEL INDICE
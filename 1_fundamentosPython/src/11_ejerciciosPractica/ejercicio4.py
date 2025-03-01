# AUTOR: RIQUISIMO

"""
IMPRIMIR LA SERIE DE FIBONACCI CON LA CANTIDAD DE ELEMENTOS ESPECIFICADOS
"""

# FORMA 1
def obtenerFibonacci(cantidad):
    listaFibo = [0, 1] # SE INICIALIZA LA LISTA CON EL PRIMER ELEMENTO DE LA SERIE
    a = listaFibo[0]
    b = listaFibo[1]
    for i in range(cantidad):
        current = a + b
        listaFibo.append(current)
        # SE CAMBIA LAS VARIABLES PARA QUE SE PUEDA CALCULAR EL SIGUIENTE NUMERO EN LA ITERACION QUE VIENE
        a,b = b,current # DESEMPAQUETADO
    return listaFibo

# FORMA 2
def obtenerFibonacci2(cantidad):
    listaFibo = [0, 1]
    for i in range(cantidad):
        listaFibo.append(
        listaFibo[-2] + listaFibo[-1]) # SE SUMA EL PENULTIMO MAS EL ULTIMO DE LA LISTA
    return listaFibo

cantidad = int(input("CUANTOS ELEMENTOS DE LA SERIE DE FIBONACCI DESEAS IMPRIMIR?? "))
print(obtenerFibonacci2(cantidad))
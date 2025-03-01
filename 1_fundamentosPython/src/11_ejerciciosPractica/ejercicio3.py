# AUTOR: RIQUISIMO

"""
IMPRIMIR LA SERIE DE FIBONACCI HASTA UN NUMERO DADO POR EL USER

"""

def obtenerFibonacci(numero):
    listaFibo = [0,1]
    for i in range(numero):
        valorPorAgregar = listaFibo[-2] + listaFibo[-1] # ALMACENA EL PROXIMO VALOR DE LA SERIE
        if valorPorAgregar > numero: # PREGUNTA SI EL PROXIMO VALOR ES MAYOR AL NUMERO DADO
            return listaFibo # SI ES MAYOR YA NO LO AGREGA Y RETORNA LA LISTA
        listaFibo.append(valorPorAgregar) # SI ES MENOR LO AGREGA Y SIGUE PREGUNTANDO

limite = int(input("IGRESA EL LIMITE NUMERICO PARA IMPRIMIR LA SERIE DE FIBONACCI:  "))
print(obtenerFibonacci(limite))
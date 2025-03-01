# AUTOR: RIQUISIMO

"""
EJERCICIO:
FALTO EL PROFESOR Y LOS ALUMNOS VAN A ARMAR LA CLASE
1. PEDIR EL NOMBRE Y LA EDAD DE LOS COMPAÑEROS QUE VINIERON HOY A CLASE
2. ORDENAR LOS ALUMNOS POR LA EDAD
3. UN COMPAÑERO SERA ASISTENTE (MENOR EDAD) Y OTRO HARA DE PROFESOR (MAYOR EDAD) IDENTIFIQUELOS
"""

# FUNCION PARA PEDIR LOS DATOS DE LOS COMPAÑEROS
def ingresarCompañeros(seguir):
    compañeros = list()
    contador = 0
    while(seguir):
        nombre = input("INGRESA EL NOMBRE:  ").strip().capitalize()
        edad = int(input("INGRESA LA EDAD:  ").strip())
        compañero = (nombre, edad)
        compañeros.append(compañero)
        contador+=1
        print(f"COMPAÑERO {nombre}, INGRESADO CON EXITO, VAS INGRESANDO {contador} COMPAÑERO(S)")
        seguir = bool(int(input("DESEAS INGRESAR A OTRO COMPAÑERO? (1: SI | 0: NO):  ")))
        if seguir == False:
            print(f"\nAGREGASTE UN TOTAL DE {contador} COMPAÑERO(S) CON EXITO!")
    return compañeros

# FUNCION PARA MOSTRAR LISTA EN CONSOLA
def mostrarlista(lista):
    print("\nTODOS LOS COMPAÑEROS ORDENADOS POR EDAD: ")
    for elemento in lista:
        print(f"COMPAÑERO: {elemento[0]}, EDAD: {elemento[1]}")

# PARTE 1: PEDIR QUE SE INGRESEN LOS COMPAÑEROS
print("BIENVENIDO AL PROGRAMA DE GESTION DE LA CLASE")
seguir = bool(int(input("DESEAS INGRESAR A LOS COMPAÑEROS QUE ASISTIERON?: (1: SI | 0: NO):  ")))
listaCompañeros = ingresarCompañeros(seguir)

# PARTE 2: ORDENAR LOS COMPAÑEROS POR EDAD Y MOSTRARLOS
listaCompañeros.sort(key = lambda x : x[1])
seguir = bool(int(input("DESEAS VER LA LISTA DE COMPAÑEROS ORDENADA?: (1: SI | 0: NO):  ")))
if seguir:
    mostrarlista(listaCompañeros)

# PARTE 3: IDENTIFICAR ASISTENTE Y PROFESOR ENCARGADOS
asistente = listaCompañeros[0][0] # OBTENER EL NOMBRE DEL PRIMER COMPAÑERO DE LA LISTA
profesor = listaCompañeros[-1][0] # OBTENER EL NOMBRE DEL ULTIMO COMPAÑERO DE LA LISTA
seguir = bool(int(input("DESEAS VER QUIENES SON ASISTENTE Y PROFESOR ENCARGADOS?: (1: SI | 0: NO):  ")))
if seguir:
    print(f"ASISTENTE: {asistente}\nPROFESOR: {profesor}")
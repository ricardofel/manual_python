# AUTOR: RIQUISIMO

"""
LAS FUNCIONES ANONIMAS (LAMBDA) SON FUNCIONES ABSTRACTAS QUE NO TIENEN NOMBRE Y PERMITEN TENER UNA MEJOR
CONSICION EN EL CODIGO Y SE LES PUEDE DAR UN USO MAS FLEXIBLE
- RETORNAN EL RESULTADO AUTOMATICAMENTE
- NO SON APTAS CUANDO NECESITAMOS PROGRAMAR MAS DE UNA INSTRUCCION
"""

# EJEMPLO 1
multiplicacionx2 = lambda x: x*2
print(f"RESULTADO DE LA OPERACION CON LA FUNCION ANONIMA: {multiplicacionx2(10)}")

# USANDO FUNCIONES DE ORDEN SUPERIOR CON FUNCIONES LAMBDA

# LAS FUNCIONES DE ORDEN SUPERIOR SON COMO UN BUCLE ARTIFICIAL

# FILTER
# DEVUELVE UN OBJETO FILTRANDO APLICANDO UNA CONDICION
# PARA USARLO DEBEMOS CONVERTIR SU RESULTADO A UNA LISTA
lista5 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
listaFiltrada = list(filter(lambda x : x >= 20, lista5))
print(f"LISTA FILTRADA, SOLO NUMEROS MAYORES O IGUALES A 20: {listaFiltrada}")
# COMO SERIA SIN FUNCION LAMBDA
def verificarNum(lista):
    listaNueva = list()
    for num in lista:
        if num >= 20:
            listaNueva.append(num)
    return listaNueva



print(f"LISTA FILTRADA (FORMA 2), SOLO NUMEROS MAYORES O IGUALES A 20: {verificarNum(lista5)}")
# MAP
#APLICA UN CAMBIO A TODOS LOS ELEMENTOS DE LA LISTA
listaMapeada = list(map(lambda x : x+2, lista5)) # SUMA 2 A TODOS LOS ELEMENTOS DE LA LISTA
print(f"LISTA ORIGINAL: {lista5}\nLISTA MAPEADA, SE SUMO 2 A TODOS LOS NUMEROS DE LA LISTA: {listaMapeada}")



# REDUCE
# APLICA UNA FUNCION QUE NOSOTROS LE ASIGNAMOS A UNA LISTA
from functools import reduce # SE DEBE IMPORTAR PARA USARLA
numeritos = [2, 3, 4, 5]
resultado = reduce(lambda a, b: a + b ** 2, numeritos, 0) # SUMA LOS CUADRADOS DE TODOS LOS NUMEROS
# NOTA: reduce(funcion, lista, valor inicial de la acumulacion (opcional))
# SOLO SIRVE CON FUNCIONES ACUMULATIVAS, ES DECIR QUE INVOLUCRAN A TODOS LOS NUMEROS
# COMO LA SUMA DE LOS CUADRADOS DE TODOS LOS NUMEROS, EL PRODUCTO DE TODOS LOS NUMEROS, ETC
print(f"LA SUMA DE LOS CUADRADOS DE LOS NUMEROS DE LA LISTA: {resultado}")
"""
- Inicialización: reduce comienza con el valor inicial 0.
- Primera iteración: a = 0, b = 2
a + b ** 2 = 0 + 2 ** 2 = 0 + 4 = 4
- Segunda iteración: a = 4, b = 3
a + b ** 2 = 4 + 3 ** 2 = 4 + 9 = 13
- Tercera iteración: a = 13, b = 4
a + b ** 2 = 13 + 4 ** 2 = 13 + 16 = 29
- Cuarta iteración: a = 29, b = 5
a + b ** 2 = 29 + 5 ** 2 = 29 + 25 = 54
"""
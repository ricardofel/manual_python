# AUTOR: RIQUISIMO

"""
PEDDIR UN NUMERO AL USER, E IMPRIMIR TODOS LOS NUMEROS PRIMOS DESDE EL 1 HASTA ESE NUMERO
"""
# FUNCIONES PARA VER SI UN NUMERO ES PRIMO

# FORMA 1
def esPrimo1(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# FORMA 2 (ESTA LA HICE YO)
# NO ES EFICIENTE PARA NUMEROS ALTOS PORQUE LOS RECORRE TODOS
def esPrimo2(num):
    countDivisible = 0
    if num == 1:
        return False
    for i in range(1, num+1): # SE SUMA 1 PORQUE RANGE NO TOMA EL EXTREMO SUPERIOR
        if num % i == 0:
            countDivisible+=1
        if countDivisible > 2:
            return False
    return True

# FORMA 3 (FORMA MAS OPTIMA)
def esPrimo3(num):
    if num < 2:
        return False  # EXCLUIR 0 Y 1 QUE NO SON PRIMOS
    if num in (2, 3):
        return True  # SI EL NUMERO INGRESADO ES 2 O 3 RETORNA TRUE PORQUE SON PRIMOS
    if num % 2 == 0 or num % 3 == 0:
        return False  # EXCLUIR MULTIPLOS DE 2 O DE 3 QUE NO SON PRIMOS

    # VERIFICAMOS DIVISIBILIDAD PARA EL RESTO DE NUMEROS
    # EMPIEZA DESDE 5 PORQUE 1, 2, 3 YA NO ESTAN Y 4 ES MUTIPLO DE 2 QUE TAMPOCO ESTA
    # ITERA DE DOS EN DOS PARA OPERAR SOLO CON LOS IMPARES, YA QUE LOS PARES YA FUERON VALIDADOS
    # OPERA CON LA RAIZ DEL NUMERO + 1 PARA PODER OPERAR CON NUMEROS GRANDES
    # SE SUMA UNO PORQUE INT() EXCLUYE DECIMALES Y QUEREMOS EVITAR QUE FALTEN DIVISORES
    for i in range(5, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# FUNCION PARA IMPRIMIR LOS NUMEROS PRIMOS DESDE EL 1 HASTA UN NUMERO DATO
def obtenerListaPrimos(num):
    primos = list()
    for i in range(1, num+1):
        if (esPrimo1(i)):
            primos.append(i)
    return primos

numero = int(input("HASTA QUE NUMERO DESEAS OBTENER LA LISTA DE PRIMOS??  "))
print(obtenerListaPrimos(numero))
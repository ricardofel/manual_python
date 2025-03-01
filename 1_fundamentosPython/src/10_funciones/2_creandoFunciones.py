# AUTOR: RIQUISIMO
"""
UNA FUNCION ES UN BLOQUE DE CODIGO QUE SE VA A EJECUTAR CADA VEZ QUE NOSOTROS LO LLAMEMOS
SE LE PUEDEN PASAR PARAMETROS QUE SERAN VARIABLES QUE SOLO EXISTEN DENTRO DE LA MISMA FUNCION
ESTRUCTURA;
def nombreFuncion(parametros):
    acciones
"""
from unicodedata import numeric


# CREANDO UNA FUNCION SIMPLE
def saludar():
    print("HOLITA!")
# LLAMANDO A LA FUNCION PARA QUE SE EJECUTE
saludar()

# CREANDO UNA FUNCION CON PARAMETROS
def saludar(nombre, genero):
    genero = genero.lower()
    if genero == "hombre":
        adjetivo = "TITAN"
        print(f"HOLITA {nombre}, ERES UN CHICO {adjetivo}")
    elif genero == "mujer":
        adjetivo = "PRECIOSA"
        print(f"HOLITA {nombre}, ERES UNA CHICA {adjetivo}")
    else:
        adjetivo = "INCREIBLE"
        print(f"HOLITA {nombre}, ERES ALGUIEN {adjetivo}")

# EJECUTAR LA FUNCION
saludar("RICKY", "Hombre")
saludar("GABRIELA", "Mujer")
saludar("ARIEL", "No especificado")

# CREAR UNA FUNCION QUE RETORNE VALORES
# CREAR UNA CONTRASEÑA ALEATORIA A PARTIR DE UN NUMERO
def crearContraseñaRandom(numero):
    chars = "abcdefghijklnmopqrstuvwxyz"
    especiales = "-*_|@$%&#!"
    numero = str(numero)
    numero = int(numero[0])
    num2 = numero + 1
    num3 = numero * 2
    num4 = numero + 5
    contraseña = f"{chars[numero]}{chars[num2]}{especiales[numero]}{chars[num3]}{chars[num4]}"
    return contraseña
    # TAMBIEN PUEDE RETORNAR MULTIPLES VALORES (SE LOS JUNTA EN UNA LISTA O TUPLA O LO QUE TE DE LA GANA)
password = crearContraseñaRandom(9)
print(f"CONTRASEÑA GENERADA: {password}")

# FUNCION QUE RECIBE PARAMETROS COMPUESTOS
# FORMA 1 (OPTIMA)
def sumarVariosNumeros1(lista):
    return sum(lista)
sumatoriaf1 = sumarVariosNumeros1([1, 2, 3, 4, 5])
print(f"SUMATORIA DE VARIOS NUMEROS (FORMA 1): {sumatoriaf1}")

# FORMA 2 (OPTIMA)
def sumarVariosNumeros2(lista):
    sumatoria = 0
    for num in lista:
        sumatoria += num
    return sumatoria
sumatoriaf2 = sumarVariosNumeros2([1, 2, 3, 4, 5])
print(f"SUMATORIA DE VARIOS NUMEROS (FORMA 2): {sumatoriaf2}")

# FORMA OPTIMA Y LEGIBLE CON PARAMETRO ARGS*
def sumarVariosNumeros3(*numeros):
    return sum(numeros)
sumatoriaf3 = sumarVariosNumeros3(1, 2, 3, 4, 5)
print(f"SUMATORIA DE VARIOS NUMEROS (FORMA 3 - OPTIMA): {sumatoriaf3}")
# NOTA: EL PARAMETRO ARGS* DEBE USARSE AL FINAL DE TODOS LOS ARGUMENTOS (EN CASO DE HABER MAS DE UNO)

# FORZANDO PARAMETROS (KEYWORD ARGUMENTS)
def crearFrase(nombre, apellido, adjetivo):
    return f"HOLA {nombre} {apellido}, ERES MUY {adjetivo}"
frase = crearFrase(adjetivo="LOCO", nombre="RICKY", apellido="BALBOA") # SE FUERZAN EL ORDEN DE LOS PARAMETROS
print(frase)

# MODIFICACION
def crearFrase2(nombre, apellido, adjetivo = "INCREIBLE"):
    return f"HOLA {nombre} {apellido}, ERES MUY {adjetivo}"
frase2 = crearFrase2("RICKY", "BALBOA") # SE FUERZAN EL ORDEN DE LOS PARAMETROS
print(frase2)
# EL ADJETIVO SERA POR DEFECTO "INCREIBLE"
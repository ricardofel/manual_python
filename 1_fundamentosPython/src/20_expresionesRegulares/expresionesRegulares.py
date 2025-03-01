# AUTOR: RIQUSIMO

# Son formatos de cadena que permiten buscar patrones con coincidencias
# EXPRESIONES REGULARES MAS USADAS
# \d	Cualquier dígito (0-9)
# \w	Cualquier letra o número (a-z, A-Z, 0-9, _) alfanumericos
# \s	Espacio en blanco y saltos de linea
# \n    Saltos de linea
# .	    Cualquier carácter menos saltos de linea
# ^	    Inicio de una línea
# $	    Fin de una línea
# *	    0 o más repeticiones (OSEA QUE SI NO ENCUENTRA LA EXPRESION LO DEJE PASAR Y SI LO ENCUENTRA QUE TOME TODAS LAS QUE HAYAN)
# +	    1 o más repeticiones (SI NO ENCUENTRA NINGUNA COINCIDENCIA NO LA DEJA PASAR)
# ?	    0 o 1 repetición (opcional) HACE QUE EL CARACTER ANTERIOR SEA OPCIONAL
# {n}	Exactamente n repeticiones
# {n,}	n o más repeticiones
# {n,m}	Entre n y m repeticiones
# |     Busca o la una cosa o la otra
# NOTA: PONIENDO LA EXPRESION EN MAYUSCULA BUSCA LOS CONTRARIOS
# ^ se llama acento circulnflejo

import re

texto = '''Hola maestro, esta es la cadena 1. Como estas mi capitan?,
Esta es la linea 254 de texto. aaaaabababab ababababbbb
Esta es la linea 3 de texto.'''


# BUSCA LA PRIMERA APARICION DE LA CADENA ESPECIFICADA
resultado = re.search('Hola',texto) # SEARCH DEVUELVE UN OBJETO TIPO MATCH Y SI NO ENCUENTRA NADA DEVULEVE NONE
#print(f"{type(resultado)}: {resultado}")

# BUSCA TODAS LAS VECES QUE LA CADENA ESPECIFICADA APARECE EN EL TEXTO
# FINDALL DEVUELVE UNA LISTA CON TODAS LAS APARICIONES DE LA EXPRESION EN EL TEXTO
resultado2 = re.findall('Hola',texto) # flags=re.IGNORECASE es para ignorar las mayusculas

# BUSCAR DIGITOS NUMERICOS DEL 0 AL 9
resultado3 = re.findall(r"\d",texto) # SE USAR LA r PREVIA ANTES DE LA CADENA PARA ESPECIFICAR EL USO DE EXPRESIONES R.

# HACER EL FILTRO ALREVEZ, TODITO MENOS DIGITOS NUMERICOS CON LA EXPRESION EN MAYUSCULA
# resultado4 = re.findall(r"\D",texto)

# CANCELAR COMANDOS ESPECIALES COMO POR EJEMPLO . ^ $
# SOLO SIRBE PARA UN CARACTER
resultado5 = re.findall(r"\.",texto) # SE PONE LA BARRA INVERTIDA ANTES
# SE CANCELA LA FUNCION ORIGINAL Y BUSCA EL CARACTER QUE NOSOTROS LE PONGAMOS EN ESTE CASO PUNTOS
# print(f"PUNTOS ENCONTRADOS: {len(resultado5)}: {resultado5}")

# ARMAR UNA EXPRESION QUE BUSQUE UN NUMERO SEGUIDO DE UN PUNTO Y UN ESPACIO
# EN CASO DE SOLO QUERER BUSCAR UNA COINCIDENCIA USAR SEARCH
resultado6 = re.findall(r"\d\.\s",texto)
# print(resultado6)

# VERIFICAR SI LA CADENA EMPIEZA CON HOLA
resultado7 = re.findall(r"^Hola",texto)
# print(resultado7) # SI LO IMPRIME ES PORQUE SI LO ENCUENTRA

# HACER QUE CADA LINEA SEA UN NUEVO COMIENZO DE CADENA
resultado8 = re.findall(r"^Esta",texto,flags=re.M) #re.M activa la multilinea
# print(resultado8)

# VERIFICAR SI ALGUNA LINEA TERMINA CON ALGUN CARACTER ESPECIFICO
resultado10 = re.findall(r"texto.$",texto,flags=re.M)
# print(resultado10)

# ENCONTRAR UN NUMERO DE COINCIDENCIAS ESPECIFICO
resultado11 = re.findall(r"\d{3}\s", texto) # BUSCAR 3 DIGITOS SEGUIDOS DE UN ESPACIO
# print(resultado11)

# ENCONTRAR UN RANGO DE CARACTERES ESPECIFICADO
resultado12 = re.findall(r"\d{1,3}",texto) # BUSCAR COINCIDENCIAS DONDE HAYA MINIMO 1 DIGITO, MAXIMO 3
# print(resultado12)

# AGRUPAR, BUSCAR GRUPOS DE CARACTERES
resultado13 = re.findall(r"(ab){1}",texto) # ME DEVUELVE LAS VECES QUE ENCONTRO "ab" dos veces esguidas
#print(resultado13)
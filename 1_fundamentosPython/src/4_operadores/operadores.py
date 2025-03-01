# AUTOR: RIQUISIMO

# OPERADORES ARITMETICOS
# SUMA Y RESTA (+,-)
suma = 12 + 5
resta = 12 - 5
print(f"SUMA: {suma}, RESTA: {resta}")

# MULTIPLICACION Y DIVISION (*,/)
multiplicacion = 10 * 2
division = 100 / 4 # LA DIVISION (/) SIEMPRE NOS DEVUELVE UN VALOR FLOAT
print(f"MULTIPLICACION: {multiplicacion}, DIVISION: {division}")

# POTENCIA (EXPONENTE) (**)
# 2 ELEVADO A LA 5ta POTENCIA
potencia = 2 ** 5
print(f"POTENCIA: {potencia}")

# DIVISION ENTERA O BAJA
# DIVIDE Y SOLO TOMA EL ENTERO IGNORANDO LOS DECIMALES
divisionEntera = 10 // 3
print(f"DIVISION ENTERA: {divisionEntera}")

# RESTO O MODULO (%)
residuo = 12 % 5
print(f"RESIDUO: {residuo}")

# OPERADORES DE ASIGNACION COMPUESTA
"""
+=	->  x = x + valor	Suma y asigna el valor a la variable
-=	->  x = x - valor	Resta y asigna el valor a la variable
*=	->  x = x * valor	Multiplica y asigna el valor
/=	->  x = x / valor	Divide y asigna el valor (resultado float)
//=	->  x = x // valor	División entera y asigna
%=	->  x = x % valor	Módulo y asigna (resto de la división)
**=	->  x = x ** valor	Exponencia y asigna (potencia)
"""


# OPERADORES DE COMPARACION:
# SIEMPRE NOS DEVUELVEN UN BOOLEANO
esIgual = 5 == 10 # TAMBIEN SIRVE PARA COMPARAR CADENAS
esDistinto = 5 != 20
esMayor = 5 > 2
esMenor = 10 < 100
esMayoroIgual = 10 <= 10
esMenoroIgual = 30 <= 40

print("RESULTADOS DE OPERADORES DE COMPARACION:") # SIEMPRE DEVUELVEN UN BOOLEANO
print(esIgual, esDistinto, esMayor, esMenor, esMayoroIgual, esMenoroIgual)

# OPERADORES LOGICOS:
# OPERAN CON BOOLEANOS Y DEVUELVEN BOOLEANOS

# AND
resultado1 = True & True # DEVUELVE TRUE
resultado2 = True & False # DEVUELVE FALSE
resultado3 = False & True # DEVUELVE FALSE
resultado4 = False & False # DEVUELVE FALSE
print(f"RESULTADOS DE AND: {resultado1}, {resultado2}, {resultado3}, {resultado4}")

# OR
resultado5 = True | True # DEVUELVE TRUE
resultado6 = True | False # DEVUELVE TRUE
resultado7 = False | True # DEVUELVE TRUE
resultado8 = False | False # DEVUELVE FALSE
print(f"RESULTADOS DE OR: {resultado5}, {resultado6}, {resultado7}, {resultado8}")

# NOT
resultado9 = not True # DEVUELVE FALSE
resultado10 = not False # DEVUELVE TRUE
print(f"RESULTADOS DE NOT: {resultado9}, {resultado10}")
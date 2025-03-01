# AUTOR: RIQUISIMO

# METODOS PARA MANIPULAR NUMEROS:

# AS INTEGER RATIO
# REPRESENTAR UN FLOAT COMO FRACCION
a = 2.75
print(a.as_integer_ratio())  # (11, 4) → 2.75 = 11/4

# IS INTEGER
# VERIFICAR SI UN FLOAT ES UN ENTERO:
b = 25.0
print(b.is_integer())  # True

# REAL E IMAG
# EXTRAER LA PARTE REAL Y LA PARTE IMAGINARIA DE UN NUMERO COMPLEJO (complex)
# SIEMPRE DEVUELVEN UN DOUBLE
c = 4 + 3j #complex
print(c.real)  # 4.0
print(c.imag)  # 3.0

# CONJUGATE
# CALCULAR EL CONJUGADO DE UN NUMERO COMPLEJO
print(c.conjugate())  # (4-3j)

# METODOS DE MATH:
import math

# ROUND
# REDONDEA DATOS TIPO FLOAT A UN NUMERO DE DECIMALES ESPECIFICO
print(round(3.14159, 2))  # 3.14

# FLOOR Y CEIL
# REDONDEAN HACIA ABAJO Y HACIA ARRIBA ESPECIFICAMENTE
print(math.floor(3.7))  # 3
print(math.ceil(3.1))   # 4

# CONSTANTES MATEMATICAS
# PI, E, INFINITO, ETC
# DEVUELVEN EL VALOR DE LAS CONSTANTES
print(math.pi)  # 3.141592653589793
print(math.e)   # 2.718281828459045
print(math.inf) # inf

# ABS
# DEVUELVE EL VALOR ABSOLUTO DEL NUMERO
d = -25
print(abs(d))  # 25

# POW
# DEVUELVE LA POTENCIA DEL NUMERO
print(pow(2, 3))  # 2^3 -> 8
# ES LO MISMO QUE:
print(2 ** 3)  # 8

# SQRT
# DEVUELVE LA RAIZ CUADRADA DEL NUMERO
print(math.sqrt(25))  # 5.0
# PARA SACAR RAICES DE CUALQUIER GRADO
print(27 ** (1/3))  # 3.0 → Raíz cúbica de 27

# LOG
# DEVUELVE EL LOGARITMO DEL NUMERO
print(math.log(8, 2))  # log₂(8) = 3
# LOGARITMO NATURAL
# NO SE ESPECIFICA LA BASE
print(math.log(10))  # 2.3025 → log(e)(10)

# EXP
# CALCULA EL EXPONENCIAL DEL NUMERO
print(math.exp(2))  # 7.389 → e^2

# FACTORIAL
# CALCULA EL FACTORIAL DEL NUMERO
print(math.factorial(5))  # 120 → 5! = 5 × 4 × 3 × 2 × 1

# GCD
# DEVUELVE EL MAXIMO COMUN DIVISOR ENTRE DOS NUMEROS
# OBLIGADO DEBEN SER ENTEROS
print(math.gcd(25, 10))  # 5

# FUNCIONES TRIGONOMETRICAS
# DEGREES Y RADIANS
# CONVIERTEN ANGULOS DE RADIANES A GRADOS Y VICEVERSA
print(math.degrees(math.pi))  # 180.0 → π radianes a grados
print(math.radians(180))      # 3.1415 → 180° a radianes

# SIN, COS Y TAN
# CALCULAN EL SENO COSENO Y TANGENTE
# SOLO RECIBEN ANGULOS EN RADIANES
angulo = math.radians(30)  # Convertir 30° a radianes
print(math.sin(angulo))  # 0.5
print(math.cos(angulo))  # 0.866
print(math.tan(angulo))  # 0.577

# ARCOS
valor = 0.5 # VALOR TIPO FLOAT
asin_result = math.asin(valor)  # Arco seno de 0.5
acos_result = math.acos(valor)  # Arco coseno de 0.5
atan_result = math.atan(valor)  # Arco tangente de 0.5
print(asin_result)  # Salida en radianes
print(acos_result)  # Salida en radianes
print(atan_result)  # Salida en radianes
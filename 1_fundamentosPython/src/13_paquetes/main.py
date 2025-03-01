# AUTOR: RIQUISIMO

from paquete.funciones import sumar,multiplicar
print(sumar(3,2))
print(multiplicar(4,5))

"""
PARA QUE UNA CARPETA SE CONSIDERE UN PAQUETE DEBE TENER EL ARCHIVO __init__.py
PARA QUE UNA CARPETA SE CONSIDERE SUBPAQUETE DEBE ESTAR DENTRO DE OTRO PAQUETE (ES DECIR QUE TENGA EL ARCHIVO __init__.py)
"""

"""
COMO SABER QUE DIRECTORIO ESTAMOS USANDO
import os
print("Directorio de trabajo actual:", os.getcwd())
"""
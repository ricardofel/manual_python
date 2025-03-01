# AUTOR: RIQUISIMO

"""
UN MODULO ES UN ARCHIVO .py QUE ALMACENA CODIGO EL CUAL PERMITE LLAMARLO DESDE OTROS MODULOS
PARA USARLO ALLA
ESTE MISMO ARCHIVO ES UN MODULO, Y LO USAREMOS PARA PRATICAR

TIPOS DE MODULOS:
- Módulos estándar (nativos): Son los módulos que vienen incluidos con la instalación de Python.
No necesitas instalarlos por separado. Ejemplos incluyen math, os, sys, entre otros.

- Módulos de terceros: Son módulos que no vienen con la instalación de Python y deben ser instalados por separado,
generalmente usando un gestor de paquetes como pip. Ejemplos incluyen requests, numpy, pandas, entre otros.

- Módulos propios: Son módulos creados por el propio usuario para ser utilizados en sus proyectos.
Estos módulos pueden ser archivos .py que contienen funciones, clases y variables que se pueden importar
y usar en otros archivos Python.
"""

# FUNCION
def Saludar(nombre):
    return f"HOLA {nombre.upper()} QUE TAL?"

# saludar = "jajajajaj"
"""
COMO VEMOS EN LA LINEA ANTERIOR SI TENEMOS UN OBJETO QUE SE LLAMA IGUAL QUE OTRO OBJETO
DENTRO DEL MISMO MODULO VAMOS A TENER PROBLEMAS AL MOMENTO DE IMPORTARLO

IMPORTANTE: DIFERENCIAR BIEN LOS NOMBRES DE TODOS NUESTROS OBJETOS 
TIP: PONER CON LA INICIAL MAYUSCULA LOS NOMBRES DE LAS FUNCIONES Y MINUSCULA LOS NOMBRES DE LAS VARIABLES
"""

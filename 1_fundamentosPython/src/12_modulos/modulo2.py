# AUTOR: RIQUISIMO

import modulo1 as primerModulo # SE IMPORTA EL MODULO PARA PODER USAR LA FUNCION QUE ESTA EN SU INTERIOR
# USANDO AS SE PUEDE CAMBIAR EL name_space DEL MODULO
"""
SI QUIERO IMPORTAR TODO EL MODULO:
    import nombre_modulo
SI QUIERO IMPORTAR TODO EL MODULO PONIENDOLE UN ALIAS PARA USARLO:
    import nombre_modulo as nombre_alias
SI QUIERO IMPORTAR SOLO UN OBJETO(VARIABLE, CLASE, FUNCION, ETC) DE UN MODULO ESPECIFICO:
    from nombre_modulo import nombre_objeto1, nombre_objeto2
AGREGADO ALIAS A FUNCIONES ESPECIFICAS
    from nombre_modulo import nombre_objeto1 as funcion1, nombre_objeto2 as funcion2
IMPORTAR TODAS LAS FUNCIONES DE UN MODULO
    from nombre_modulo import * (ESTO ES UNA MALA PRACTICA PORQUE DEBE RECORRER TODO EL MODULO Y CONSUME RECURSOS)
"""

print(primerModulo.Saludar("Mari"))
# NOTA: AL NOMBRE DEL MODULO SE LO CONOCE COMO NAMESPACE (name_space.funcion)
# EL name_space AYUDA A EVITAR CONFUSIONES CON OTROS MODULOS

# dir(primerModulo) CON LA FUNCION DIR PODEMOS VER TODOS LOS OBJETOS QUE TIENE NUESTRO MODULO
print(dir(primerModulo))

# USANDO __name__ SE PUEDE VER NOMBRE DEL MODULO
print(__name__) # VER NOMBRE DE ESTE MODULO
print(primerModulo.__name__) # VER NOMBRE DE OTRO MODULO

# ENRUTAMIENTO DE MODULOS

# LLAMAR A UN MODULO QUE ESTA EN UNA CARPETA EN LA MISMA RUTA
from carpeta.caminar import EjecutarCaminar
print(EjecutarCaminar())
# OTRA FORMA (NO OPTIMA)
# from paquete import caminar

# IMPORTAR MODULOS QUE ESTAN EN CUALQUIER OTRA RUTA
"""
import sys
sys.path.append('C:/Users/ricar/Desktop/personal/informatica/python/cursoDalto/src/10_funciones')
import 2_creandoFunciones.crearContraseñaRandom
print(cf.crearContraseñaRandom(9))

NOTA: EVITA NOMBRAR LOS PAQUETES Y MODULOS EMPEZANDO CON NUMEROS    
"""

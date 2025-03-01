# AUTOR: RIQUISIMO
"""
EN PYTHON LAS VARIABLES:
- 1 SE DECLARAN
- 2 SE DEFINEN
NO HACE FALTA AGREGAR TIPO DE DATO NI DOMINIO EN LA DECLARACION YA QUE TIENE TIPADO DINAMICO
"""
# EJEMPLOS
a = 10
b = 23.7
c = "Ricky"
d = True
e = (4 > 2)

# CONCATENAR CADENAS
nombre = "Ricky"
apellido = "Balboa"
completo = nombre + " " + apellido + " "

# CONCATENAR CADENAS CON NUMEROS
# SE DEBE CONVERTIR PRIMERO EL NUMERO A CADENA
edad = 20
info = completo + str(edad)
print("CADENA CONCATENADA CON STR: " + info)

# HACERLO CON FORMAT
info = completo + f"{edad}"
print("CADENA CONCATENADA CON FORMAT: " + info)
# NOTA: PARA IMPRIMIR CUALQUIER NUMERO EN PYTHON PRIMERO DE DEBE CONVERTIR A CADENA

# BORRAR UNA VARIABLE EN MEDIO DEL PROGRAMA:
del nombre # DESDE AQUI NOMBRE YA NO EXISTE EN EL PROGRAMA
print("CADENA DESPUES DE APLICAR EL DEL: " + info)
# IGUAL SE IMPRIME PORQUE LA VARIABLE YA ESTABA FORMADA

# BUSCAR TROZOS DE CADENAS (OPERADORES DE PERTENENCIA):
# CON IN PODEMOS PREGUNTAR SI UNA CADENA ESTA DENTRO DE OTRA
# DEVUELVE UN BOOLEANO
consulta = "Ricky" in info
consulta2 = "Ricky" not in info
consulta3 = "Tyler the Creator" in info
print(f"Esta \"Ricky\" dentro de: \"{info}\" ??: {consulta}")
print(f"No esta \"Ricky\" dentro de: \"{info}\" ??: {consulta2}")
print(f"Esta \"Tyler the Creator\" dentro de: \"{info}\" ??: {consulta3}")

# A PESAR DE QUE EL TIPADO ES DINAMICO, ASI ES COMO SE ASIGNA EL TIPO DE DATO UNA VARIABLE:
name: str = "Ricky"
age: int = 21
altura: float = 1.75
es_estudiante: bool = True
num: complex = 2 - 5j
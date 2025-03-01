# AUTOR: RIQUISIMO
"""
EL PARAMETRO "a" APPEND EN open() PERMITE AGREGAR INFO AL ARCHIVO SIN MODIFICAR LO QUE YA TIENE
"""
with open("src/14_archivos/data.txt", "a",encoding="UTF-8") as archivo:
    archivo.write("ESCRIBIENDO EL ARCHIVO CON APPEND\n ")
    # ESCRIBIENDO CON FOR
    for i in range(1,10+1):
        archivo.write(f"LINEA {i} ESCRITA CON FOR\n")
    # FORMA EN UNA SOLA LINEA
    # UTILIZANDO COMPRENSION DE LISTAS
    # archivo.writelines([f"LINEA {i} ESCRITA CON FOR\n" for i in range(1, 10+1)])

    # ESCRIBIENDO POR LINEAS
    archivo.writelines(["-- LINEA\n","-- ESCRITA\n","-- NORMAL\n"])
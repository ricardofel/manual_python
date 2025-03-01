# AUTOR: RIQUISIMO

# TENEMOS 2 LISTAS, UNA CON NOMBRES Y OTRA CON APELLIDOS
nombres = ["Ricky","JeanK","Antonia","Johan","Bryan"]
apellidos = ["Guevara","Garcia","Carrion","Mora","Romero"]

# ESCRIBIR ESTO EN UN .txt DE FORMA OPTIMA
with open("src/17_problemasArchivos/dataTXT.txt","w", encoding="UTF-8") as archivo:
    archivo.write("NOMBRES Y APELLIDOS DE PERSONAS: \n")
    [archivo.write(f"NOMBRE: {nombre}, APELLLIDO: {apellido}\n") for nombre, apellido in zip(nombres, apellidos)]
    print("ARCHIVO ESCRITO CORRECTAMENTE")
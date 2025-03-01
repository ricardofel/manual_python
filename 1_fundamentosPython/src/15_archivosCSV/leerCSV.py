# AUTOR: RIQUISIMO

# FORMA NORMAL DE LEER ARCHIVOS CSV
import csv

with open("src/15_archivosCSV/dataCSV.csv",encoding="UTF-8") as archivo:
    #csv.reader(nombreVariableLectura, delimiter="especificar delimitador")
    lectura = csv.reader(archivo, delimiter=";")
    # NOS DEVUELVE UN OBJETO CSV READER QUE ES UN ITERABLE (ES COMO UNA TUPLA DE LISTAS)
    # CADA FILA ES UNA LISTA
    for fila in lectura:
        print(fila)
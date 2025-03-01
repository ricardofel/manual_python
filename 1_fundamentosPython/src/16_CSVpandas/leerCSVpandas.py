# AUTOR: RIQUISIMO
# DESCOMENTAR PARA IR PROBANDO CADA FUNCION

# PARA IMPORTAR PANDAS SE LO HACE DESDE EL PIP (INSTALADOR DE MODULOS DE PYTHON) (py -m pip install pandas)
import pandas as pd

# df es data frame que es una matriz especial donde estan todos los datos del csv
# read_csv(ruta, delimitador, nuevos nombres de atributos)
# CON names = ESPECIFICAMOS UN NUEVO ENCABEZADO Y NO TOMAMOS EL QUE ESTA POR DEFECTO
# ,names=["name","lastname","age","coins"]
# SI YA TIENE ENCABEZADO POR DEFECTO LO DEJA COMO UNA FILA MAS

df = pd.read_csv("src/16_CSVpandas/dataCSV.csv",delimiter=";")

# MOSTRAR SOLO UNA COLUMNA DEL DATA FRAME
#print(df["nombre"])

# MOSTRAR EL DATA FRAME COMPLETO
print(df)

# ORDENAR EN BASE A UNA COLUMNA
# ORDENAR POR LA EDAD DE FORMA ASCENDENTE
dfOrdenadoAsc = df.sort_values("edad")
#print(dfOrdenadoAsc)

# ORDENAR POR LA EDAD DE FORMA DESCENDENTE
dfOrdenadoDesc = df.sort_values("edad", ascending=False)
#print(dfOrdenadoDesc)

# CUANDO TENEMOS 2 DATA FRAME
#df2 = pd.read_csv("src/16_CSVpandas/dataCSV.csv", delimiter=";")

# CONCATENAR 2 DATA FRAME
#dfConcatenado = pd.concat([df,df2])
#print(dfConcatenado) # CUANDO SON MUCHOS DATOS NO MUESTRA TODITO EN LA CONSOLA, LO ABREVIA

# ACCEDER A LAS PRIMERAS X CANTIDAD DE FILAS CON HEAD
primeras3Filas = df.head(3)
#print(primeras3Filas)

# ACCEDIENDO A LAS X ULTIMAS FILAS CON TAIL
ultimas4Filas = df.tail(4)
#print(f"\n{ultimas4Filas}")

# SABER EL NUMERO DE FILAS Y COLUMNAS DE MI DATA FRAME
# SHAPE DEVUELVE UNA TUPLA
filasYcolumnasTotales = df.shape
#print(filasYcolumnasTotales)
filas, columnas = filasYcolumnasTotales[0], filasYcolumnasTotales[1]
#print(f"FILAS TOTALES DEL ARCHIVO: {filas}\nCOLUMNAS TOTALES DEL ARCHIVO: {columnas}")

# OBTENIENDO DATOS ESTADISTICOS CON DESCRIBE
dfInfo = df.describe()
#print(dfInfo)

# ACCEDIENDO A ELEMENTOS ESPECIFICOS CON LOC
# loc[indiceFila,atributo]
elemento = df.loc[2,"edad"] # ACCEDER A LA EDAD DE LA FILA 2
#print(elemento)

# COMO SI FUERA UNA MATRIZ
# [indiceFila, indiceColumna]
elemento2 = df.iloc[2,3] # ACCEDER A LOS AHORROS (COLUMNA 3) DE LA FILA 2
#print(elemento2)

# USANDO ILOC CON SLICING

# MOSTAR TODA LA COLUMNA AHORROS
filaAhorros = df.iloc[:,3] # CON : INDICAMOS QUE QUEREMOS VER TODAS LAS FILAS
#print(filaAhorros)

# LO MISMO PERO CON FILAS
fila5 = df.iloc[4,:] # EL INDICE 4 REPRESENTA LA FILA 5
#print(fila5)

# FILTRAR REGISTROS
mayores30 = df.loc[df["edad"]>30,:]
print("MAYORES DE 30 AÑOS: ")
print(mayores30)
# AUTOR: RIQUISIMO
import pandas as pd

df = pd.read_csv("src/17_problemasArchivos/dataCSV.csv",delimiter=";",encoding="UTF-8")
print(df)

# CAMBIAR EL TIPO DE DATO DE UNA COLUMNA
#df["edad"] = df["edad"].astype(str)
#print(type(df.loc[0,"edad"])) # ES UNA STRING
# df["edad"][0] otra forma de acceder al primer elemento de el data frame

# REEMPLAZAR TODAS LAS VECES QUE APARECE UN DATO POR OTRO
df.loc[:, "nombre"] = df["nombre"].replace("Juan", "Felipito")
#print(df.loc[0,"nombre"])

# ELIMINAR FILAS QUE ESTAN INCOMPLETAS
#df.dropna()

# ELIMINAR LAS COLUMNAS CON DATOS FALTANTES
# POR DEFECTO PARA ELIMINAR LAS FILAS VIENE axis=0
#df.dropna(axis=1)

# ELIMINAR LAS FILAS CON DATOS DUPLICADOS
#df.drop_duplicates()

# FILTRAR DATOS PARA CREAR UN DATA FRAME NUEVO
df = df.loc[df["edad"]>30,:]

# ESCRIBIR UN DATA FRAME MODIFICADO EN UN NUEVO ARCHIVO CSV
df.to_csv("src/17_problemasArchivos/dataLimpiaCSV.csv",index=False, sep=";", encoding="UTF-8")
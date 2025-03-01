# AUTOR: RIQUISIMO

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# LEER EL CSV
df = pd.read_csv("src/18_graficos/ingresosCofla.csv",delimiter=";",encoding="UTF-8")

# CALCULANDO LOS INGRESOS TOTALES
ingresosTotales = df["ingresos"].sum()
# MOSTRANDO EN CONSOLA LOS INGRESOS TOTALES
print(f"INGRESOS TOTALES DE COFLA: {ingresosTotales}")

#GRAFICAR
# CREAR EL GRAFICO
sns.barplot(x="fuente",y="ingresos", data=df)
# MOSTRAR EL GRAFICO
plt.show()

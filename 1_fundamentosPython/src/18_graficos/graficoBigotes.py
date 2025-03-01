# AUTOR: RIQUISIMO
"""
NOTA: PARA QUE TODO FUNCIONE:
- NO DEBEN HABER ESPACIOS NI CARACTERES RAROS ESCAPADOS EN EL CSV
- LOS NOMBRES DELOS EJES X E Y DEBEN COINCIDIR CON EL ENCABEZADO DEL CSV
- SI EL ARCHIVO ES MUY GRANDE SE DEBE USAR JUNTO CON read_csv EL PARAMETRO chunksize
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# LEYENDO EN ARCHIVO
df = pd.read_csv("src/18_graficos/zcategorias.csv",delimiter=",",encoding="UTF-8")

# CREANDO EL GRAFICO
sns.boxplot(x="categoria",y="valor",data=df)
# MOSTRANDO EL GRAFICO
plt.show()
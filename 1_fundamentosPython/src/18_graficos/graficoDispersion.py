# AUTOR: RIQUISIMO

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# LEYENDO EN ARCHIVO
df = pd.read_csv("src/18_graficos/zdatos.csv",delimiter=",",encoding="UTF-8")

# CREANDO EL GRAFICO
sns.scatterplot(x="tiempo",y="dinero",data=df)
# MOSTRANDO EL GRAFICO
plt.show()
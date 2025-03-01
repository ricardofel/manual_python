# AUTOR: RIQUISIMO

import pandas as pd
# LIBRERIAS PARA TRABAJAR CON GRAFICOS
import matplotlib.pyplot as plt
import seaborn as sns

# LEER EL ARCHIVO
df = pd.read_csv("src/18_graficos/pedos.csv",delimiter=",",encoding="UTF_8")

# GRAFICAR
sns.lineplot(x="fecha",y="pedos",data=df) # GENERAR GRAFICO
plt.plot("2025-01-06",20,"o") # MARCAR PUNTO MAS ALTO
plt.show() # MOSTRAR GRAFICO
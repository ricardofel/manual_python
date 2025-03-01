# AUTOR: RIQUISIMO

# EJERCICIO DE DURACION DE CURSOS DE PYTHON

# PARTE 1
# DURACION EN HORAS DE CURSOS DE PYTHON
otrosCursosMin = 2.5
otrosCursosMax = 7
otrosCursosAvg = 4
cursoDalto = 1.5

# CALCULAR PORCENTAJE DE RAPIDEZ EN EXPLICACION DEL CURSO DE DALTO RESPECTO CON LOS OTROS CURSOS
diferencia1 = 100 - ((cursoDalto/otrosCursosMin)*100)
diferencia2 = 100 - cursoDalto * 1000 // otrosCursosMax / 10 # HACER LA MISMA OPERACION PERO QUE ME SALGA SOLO UN DECIMAL
diferencia3 = 100 - ((cursoDalto/otrosCursosAvg)*100)
print(f"EL CURSO FUE UN {diferencia1}% mas rapido que el minimo de otros cursos")
print(f"EL CURSO FUE UN {diferencia2}% mas rapido que el maximo de otros cursos")
print(f"EL CURSO FUE UN {diferencia3}% mas rapido que el promedio de otros cursos")

# PARTE 2
# DURACION EN HORAS DE CRUDOS DE CURSOS DE PYTHON
crudoAvg = 5
crudoDalto = 3.5

# CALCULAR PORCENTAJE DE TIEMPO VACIO REMOVIDO
tiempoVacioPromedio = 100 - otrosCursosAvg * 1000 // crudoAvg / 10
tiempoVacioDalto = 100 - cursoDalto * 1000 // crudoDalto / 10
print("------------------------------------------")
print(f"UN CURSO PROMEDIO ELIMINA UN {tiempoVacioPromedio}% DE TIEMPO VACIO")
print(f"EL CURSO DE DALTO ELIMINA UN {tiempoVacioDalto}% DE TIEMPO VACIO")

# CALCULAR CUANTAS HORAS DE OTROS CURSOS EQUIVALE A VER 10 HORAS DE ESTE CURSO
diferencia10Horas1 = otrosCursosAvg * 100 // cursoDalto / 10
diferencia10Horas2 = cursoDalto * 100 // otrosCursosAvg / 10
print("------------------------------------------")
print(f"VER 10 HORAS DE EL CURSO DE DATO EQUIVALE A VER {diferencia10Horas1} HORAS DE OTROS CURSOS")
print(f"VER 10 HORAS DE OTROS CURSOS EQUIVALE A VER {diferencia10Horas2} HORAS DEL CURSO DE DALTO")
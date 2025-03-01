# AUTOR: RIQUISIMO

# EJERCICIO DE DURACION DE CURSOS DE PYTHON

# PARTE 1
# DURACION EN HORAS DE CURSOS DE PYTHON
otrosCursosMin = 2.5
otrosCursosMax = 7
otrosCursosAvg = 4
cursoDalto = 1.5

# CALCULAR PORCENTAJE DE RAPIDEZ EN EXPLICACION DEL CURSO DE DALTO RESPECTO CON LOS OTROS CURSOS
diferencia1 =  100 - (cursoDalto / otrosCursosMin) * 100 # NO NECESITA REDONDEARSE
diferencia2 =  round(100 - (cursoDalto / otrosCursosMax) * 100, 2) # SE REDONDEA
diferencia3 = 100 - ((cursoDalto/otrosCursosAvg)*100) # NO NECESITA REDONDEARSE
print(f"EL CURSO DE DALTO FUE UN {diferencia1}% mas rapido que el minimo de otros cursos")
print(f"EL CURSO DE DALTO FUE UN {diferencia2}% mas rapido que el maximo de otros cursos")
print(f"EL CURSO DE DALTO FUE UN {diferencia3}% mas rapido que el promedio de otros cursos")

# PARTE 2
# DURACION EN HORAS DE CRUDOS DE CURSOS DE PYTHON
crudoAvg = 5
crudoDalto = 3.5

# CALCULAR PORCENTAJE DE TIEMPO VACIO REMOVIDO
tiempoVacioPromedio = 100 - (otrosCursosAvg / crudoAvg) * 100 # NO NECESITA REDONDEARSE
tiempoVacioDalto = round(100 - (cursoDalto / crudoDalto) * 100, 2) # SE REDONDEA
print("------------------------------------------")
print(f"UN CURSO PROMEDIO ELIMINA UN {tiempoVacioPromedio}% DE TIEMPO VACIO")
print(f"EL CURSO DE DALTO ELIMINA UN {tiempoVacioDalto}% DE TIEMPO VACIO")

# CALCULAR CUANTAS HORAS DE OTROS CURSOS EQUIVALE A VER 10 HORAS DE ESTE CURSO
diferencia10Horas1 = round(otrosCursosAvg * 10 / cursoDalto, 1) # SE REDONDEA
diferencia10Horas2 = round(cursoDalto * 10 / otrosCursosAvg, 1) # SE REDONDEA
print("------------------------------------------")
print(f"VER 10 HORAS DE EL CURSO DE DATO EQUIVALE A VER {diferencia10Horas1} HORAS DE OTROS CURSOS")
print(f"VER 10 HORAS DE OTROS CURSOS EQUIVALE A VER {diferencia10Horas2} HORAS DEL CURSO DE DALTO")
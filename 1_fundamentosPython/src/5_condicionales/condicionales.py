# AUTOR: RIQUISIMO

# EJEMPLO 1
# SE DEBE RESPETAR LA IDENTACION DENTRO DE LA ESTRUCTURA OBLIGATORIAMENTE
edad = int(input("INGRESA TU EDAD: "))
if edad >= 18:
    print("ERES UN ADULTO")
else:
    print("ERES MUCHACHO TODAVIA")

# EJEMPLO 2
contraseñaAlmacenada = "increible"
contraseñaEscrita = input("INGRESA LA CONTRASEÑA: ")
if contraseñaEscrita == contraseñaAlmacenada:
    print("CONTRASEÑA CORRECTA, TIENES ACCESO")
elif contraseñaEscrita == "coño":
    print("ERES UN PATAN") # PARA AGREGAR VARIAS CONDICIONES SE USA "elif"
else:
    print("CONTRASEÑA INCORRECTA, NO PUEDES PASAR")


# EJEMPLO 3
ingresoMensual = float(input("CUAL ES TU INRGESO MENSUAL?: "))
if ingresoMensual > 10000:
    gastoMensual = float(input("TIENES BUENOS INGRESOS, PERO CUENTAME TUS GASTOS MENSUALES:" ))
    if gastoMensual > 5000: # CONDICIONAL ANIDADO
        print("TIENES BUEN INGRESO PERO GASTAS MUCHO")
    else:
        print("ESTAS BIEN EN CUALQUIER PARTE DEL MUNDO")
elif ingresoMensual > 50000:
    print("ESTAS BIEN EN LATINOAMERICA")
elif ingresoMensual > 500:
    print("ESTAS BIEN")
elif ingresoMensual > 0:
    print("HAY QUE TRABAJAR ESOS INGRESOS")
elif ingresoMensual == 0:
    print("ESTAS BIEN HECHO PEDAZOS")
else:
    print("VALOR INCORRETO")

# EN PYTHON NO HAY ESTRUCTURAS COMO SWITCH EN JAVA
# PERO SE PUEDE LOGRAR ESE COMPORTAMIENTO USANDO DICCIONARIOS Y FUNCIONES
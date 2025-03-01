# AUTOR: RIQUISIMO

import re

# EJERCICIO 1
text  = "The quick brown fox jumps over the lazy dog"
x = re.search(r"^The.*dog$",text)
# VERIFICA QUE EL TEXTO EMPIECE CON "The" (^The)
# QUE LUEGO DE ESO ENCUENTRE CUALQUIER CARACTER MENOS SALTOS DE LINEA (.)
# LE DICE AL ANTERIOR (.) QUE SI NO ENCUENTRA NADA NO IMPORTA, Y QUE SI ENCUENTRA LOS PONGA TODOS (.*)
# QUE LUEGO DE TODITO ESO LA CADENA TERMINE CON "dog" (dog$)
if x:
    print("SI")
else:
    print("NO")

# EJERCICIO 2
text2 = "La fecha es 23/06/2021 y el telefono es +1-555-555-5555"
patron = r"\d{2}/\d{2}/\d{4}"
replacement = "Fecha oculta"
# ENCUENTRA UN PATRON Y LO REEMPLAZA POR OTRO TEXTO
newtext = re.sub(patron, replacement, text2)
print(f"TEXTO MODIFICADO: {newtext}")

# EJERCICIO 3
text3 = "reemplazaando todas las vocales por el asterisco"
newtext2 = re.sub(r"[aeiou]","*", text2)
print(newtext2)

# EJERCICIO 4 (VERIFICAR EMAIL)
email = "ricky@example.com"
patronEmail = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}" # DENTRO DE LOS CORCHETES SE PUEDE PONER TODOS LOS CARCATERES POR SEPARADO QUE BUSCA
emailValidado = re.match(patronEmail,email)
if emailValidado:
    print(f"EL EMAIL {email} ES VALIDO")
else:
    print(f"EL EMAIL {email} NO ES VALIDO")

# EJERCICIO 4
text4 = "Este es un ejemplo de email: https://www.example.com dale click maestro"
patron2 = "https?://[a-zA-Z0-9.-]+\.[A-Za-z]{2,}"
result = re.findall(patron2,text4)
print(result)

# EJERCICIO 5
# DETECTANDO UN NUMERO CABA Y OCULTANDOLO
textoNumero = "Hola hermano, como estas?, mi numero es: +54 22 4321-4321, y mi otro numero es: +98 22 4001-4321"
patron3 = r"\+\d{2}\s\d{2}\s\d{4}-\d{4}"
textoModificado = re.sub(patron3,"OCULTO",textoNumero)
print(textoModificado)



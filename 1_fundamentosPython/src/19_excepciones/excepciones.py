# AUTOR: RIQUISIMO
from tkinter import EXCEPTION


# FUNCION QUE SUMA DOS NUMEROS
def sumarDos():
    # INICIANDO BUCLE
    while True:
        # PIDIENDO NUMEROS POR CONSOLA
        a = input("Numero 1:  ")
        b = input("Numero 2:  ")
        # INTENTAR CONVERTIRLOS A ENTEROS Y SUMARLOS
        try:
            c = int(a) + int(b)
            # break YA NO ES NECESARIO CON EL ELSE
        # SI NO SE PUEDEN CONVERTIR ENVIAR UN MENSAJE Y VOLVER A PEDIRLOS
        # SE PUEDEN USAR VARIOS EXCEPT 
        except Exception as e: # SI EL EXCEPT SE EJECUTA, NO SE EJECUTA EL ELSE
            print(f"TIPO DE ERROR: {type(e).__name__}")
            print(f"ERROR: {e}")
            print("El dato ingresado no es valido, vuelve a ingresarlo")
        else:
            break # SI SE LOGRO CONVERTIRLOS Y SUMARLOS SE SALE DEL BUCLE
        #finally: # NO DE USO COTIDIANO
            #print("ESTO SE EJECUTA SIEMPRE")
    return c # SE RETORNA EL RESULTADO
print(sumarDos())
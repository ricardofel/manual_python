# AUTOR: RIQUISIMO

# DEFINIR LA CLASE ESTUDIANTE
class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad 
        self.grado = grado
    
    def estudiar(self):
        print(f"""
              HAS PUESTO A ESTUDIAR A: 
              
              nombre: {self.nombre} 
              
              edad: {self.edad}
              
              grado: {self.grado}
              
              CON MUCHO EXITO!""") 

# MAIN

# METODOS PARA PEDIR LA INFORMACION
def pedir_nombre():
    return input("INGRESA EL NOMBRE:  ")

def pedir_edad():
    while True:
        edad = input("INGRESA LA EDAD:  ")
        try:
            int(edad)
        except Exception as e:
            print(f"\nHA OCURRIDO UN ERROR:\n{e}")
            print("Intenta nuevamente")
        else:
            break # ELSE SE EJECUTA SIEMPRE QUE SE EJECUTO TRY
    return edad 

def pedir_grado():
    while True:
        grado = input("INGRESA EL GRADO (1 - 7):  ")
        try:
            grado = int(grado)
        except Exception as e:
            print(f"\nHA OCURRIDO UN ERROR:\n{e}")
            print("Intenta nuevamente")
        else:
            if grado in range (1,8):   # HACE LO MISMO QUE: (grado >= 1 | grado <=7)
                break
            else:
                print(f"{grado} no esta entre (0 - 7)\nVUELVE A INTENTAR")
    return grado

# METODO PARA HACERLO ESTUDIAR
def hacerlo_estudiar(estudiante):
    while True:
        estudiar = input(f"SI DESEAS QUE EL ESTUDIANTE {estudiante.nombre} ESTUDIE, TIPEA: \"estudia\"  ")
        if (estudiar.strip().lower() == "estudia"):
            estudiante.estudiar()
            break
        else:
            print("\nMAL TIPEADO!")
             
# DESDE AQUI SE EJECUTA EL PROGRAMA

# INSTANCIAR EL OBJETO
# PARA LLAMAR LOS METODOS NO TE OLVIDES DEL () LUEGO DEL NOMBRE
estudiante1 = Estudiante(pedir_nombre(),pedir_edad(),pedir_grado())

# LLAMAR AL METODO PARA HACER QUE ESTUDIE
hacerlo_estudiar(estudiante1)
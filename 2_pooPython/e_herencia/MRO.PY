# AUTOR: RIQUISIMO

"""
MRO: Method Resolution Order
Es el orden en el que Python busca los métodos y atributos en una jerarquía 
de clases cuando se usa herencia múltiple.
"""
class Z: # 3 LUEGO VA A BUSCAR EN Z YA QUE ES LA CLASE DE LA QUE HEREDA B
    def hablar(self):
        print("HOLA, desde Z")
        
class A:# 5 LUEGO VA A BUSCAR EN A YA QUE ES LA CLASE DE LA QUE HEREDA C
    def hablar(self):
        print("HOLA, desde A")

class B(Z): # 2 LUEGO VA A BUSCAR EN B YA QUE ES LA PRIMERA CLASE DE LA QUE HEREDA D
    def hablar(self):
        print("HOLA, desde B")
        
class C(A): # 4 LUEGO VA A BUSCAR EN C YA QUE ES LA SIGUIENTE CLASE DE LA QUE HEREDA A
    def hablar(self):
        print("HOLA, desde C")
        
class D(B,C): # 1 SI CREO UN OBJETO DE D PRIMERO EJECUTA SU PROPIO METODO (HABLAR)
    def hablar(self): 
        print("HOLA, desde D")

"""
SE PUEDE PENSAR COMO UN ARBOL, SI SE ENTRA A UNA RAMA SE SIGUE HASTA QUE SE TERMINE ESA RAMA 
Y LUEGO VA POR OTRA
"""

# PROBAR EL ORDEN DE EJECUCION DE METODOS (USAR PASS PARA VACIAR LAS CLASES)    
d = D()
d.hablar()

# SABER EL MRO DE UN OBJETO
print(D.mro()) # EL METODO ES DE LA CLASE NO DEL OBJETO

# UNA VEZ YA SABIENDO EL ORDEN DE EJECUCION PODEMOS EJECUTAR EL METODO DE UNA CLASE ESPECIFICA
B.hablar(d)
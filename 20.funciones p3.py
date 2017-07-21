#funciones anidadas


def division (v1,v2):
    def validacion():
        return v1>0 and v2>0

#    if validacion():
#        return v1/v2

resultado=division(30,0)

print(resultado)


#funciones closure
#funciones que crean otra funcion
def crear_funcion(v1,v2):
    print("Se ejecuta crear funcion")
    def validacion():
        print("Se ejectua validacion")
        return v1>0 and v2>0
    return validacion

#funciones que reciben funciones
def aplicar_funcion(func):
    print("se ejecuta aplicar_funcion")
    print(func())

nueva_funcion= crear_funcion(10,5)
aplicar_funcion(nueva_funcion)
#print(nueva_funcion())
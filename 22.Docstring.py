#Crear documentacion de cada metodo

def generador(*args):
    """Recibe n cantiad de numeros y lo regresa
    al igual si es mayor a 5 """
    for valor in args:
        yield valor ,True if valor > 5 else False

for valor,bolean in generador(1,2,3,4,5,6,7,8,9):
    print(valor,bolean)


nombre=generador.__name__
documentacion=generador.__doc__
print(nombre)
print(documentacion)

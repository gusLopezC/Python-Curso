#crear objetos sin necesidad de almazenar en memoria ram

def generador(*args):
    for valor in args:
        yield valor, True

for valor,bolean in generador(1,2,3,4,5,6,7,8,9):
    print(valor,bolean)
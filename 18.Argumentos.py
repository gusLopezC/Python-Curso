def suma(*argumento):
    resultado=0
    for valor in argumento:
        resultado=resultado+valor
    return resultado


resultado=suma(25,32.23)

print(resultado)


def oper(**kwargs):
    valor=kwargs.get('valor2','No tiene valor')
    print(valor)

# un * permite llamar a n valores al metodo en tupla
# con * permite con n valores pero con diccionarios e identificador

result=oper(valor='Gus',x=5,y=76.43)
print(result)
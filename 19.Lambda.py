mi_funcion = lambda v1,v2 : v1+v2
resultado=mi_funcion(29,56)
print(resultado)

formato = lambda sentencia : "¿{}?".format(sentencia)
resulado=formato('esto es una pregunta')
print(resulado)

no_valor = lambda :10
resultado=no_valor()
print(resultado)

no_resultado = lambda : print('debe haber datos')

resultado=no_resultado()
print(resultado)

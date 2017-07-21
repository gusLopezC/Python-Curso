#decorador es una funcion que recibe una una
#funciones y crea una funcion

#A recibe como parametro B para poder crear C
def decorado(valido):

    def fundecorado(func):#AyB
        def nueva_funcion(*args,**kwargs):#C
            print("Vamos a ejecutar la funcion")
            resultado = func(*args,**kwargs)
            print("se ejecuto la funcion")
            return resultado
        return nueva_funcion#C
    return fundecorado
@decorado
def saluda():
    print("Hola")


@decorado(valido= True)
def suma(n1,n2):
    return n1+n2
#saluda()
resultado=suma(5,4)
print(resultado)
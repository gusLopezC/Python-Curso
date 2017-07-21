 def suma(v1,v2,v3):
    return v1+v2+v3

def div(v1,v2):
    return v1/v2


def multiplicacion(v1,v2=10):#se pone 10 en v2 solo si el valor esta vacio
    return v1*v2

def mult_valores():
    return "String",1,True,3.13


resultado=suma(10,20,30)
print(resultado)
resultado=div(100,10)
print(resultado)
resultado=multiplicacion(6)
print(resultado)

resultado=mult_valores()
print(resultado)

string,entero,boleano,floa = mult_valores()

print(string)
print(entero)
print(boleano)
print(floa)





def mostrar_resul(funcion):
    print(funcion(6,8))

my_variable=multiplicacion
mostrar_resul(my_variable)



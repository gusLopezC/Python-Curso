import Calculadora

resultado =Calculadora.suma(5,45)
print(resultado)
resultado =Calculadora.resta(5,45)
print(resultado)


from Calculadora import multiplicacion,division as  operacion4

resultado=multiplicacion(5,6)
print(resultado)

resultado=operacion4(100,10)
print(resultado)

#--------------name--------------
from Calculadora import __name__ as __namecalcu__
print(__name__)
print(__namecalcu__)
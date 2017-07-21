def factorial(numero):

    factorial=1
    while numero>0:
        factorial=factorial*numero
        numero-=1
    print(factorial)
    return factorial

factorial(10)

resultado=factorial(4)
print(resultado)
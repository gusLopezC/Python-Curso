lista =[1,2,3,4,5,6,7,8,9,10]

for valor in lista:
    print(valor)
    pass
print("-----------------------")
nuevo_rango =range(0,21,5)

for valor in nuevo_rango:
    print(valor)
    pass

print("-----------------------")

for indice,valor in enumerate(lista):
    print(valor,"tiene el indice ",indice)
    pass

print("-----------------------")

for valor in range(0,len(lista)):
    print(valor)
    pass

print("-----------------------")
for valor in 'Gustavo Lopez callejas':
    print (valor)
    pass

print("-----------------------")

diccionario={'a':10 ,'b':20,'c':30}

for llave,valor in diccionario.items():
    print ("Llave es : ",llave , 'con valor de ',valor)
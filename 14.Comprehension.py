"""
lista=[]
for valor in range (0,101):
    lista.append(valor)

    print(lista)
"""
lista=[valor for valor in range (0,101) if valor %2==0]
#primero valor a agregar a lista
#ciclo for,
print(lista)
print('----------------------')

tupla=tuple((valor for valor in range (0,101) if valor %2==1))

print(tupla)
print('----------------------')

diccionario={indice:valor for indice,valor in enumerate(lista)}

print (diccionario)

nombre="Gustavo"
apellidos="Lopez Callejas"

""" Formato """
resul= '{} es {}'.format(nombre,apellidos)
resul2=nombre+" "+apellidos
resul3= '{a}  {b}'.format(b=nombre,a=apellidos)
resul3=resul3.lower() #minusculas
resul4=resul3.upper() #MAYUSCULA
resul5=resul4.title()#Modo oracion
#resul6=resul3.reverse();
print(resul)
print(resul2)
print(resul3)
print(resul4)
print(resul5)
print(resul6)


"""Busqueda"""


busqueda='{a}  {b}'.format(a=nombre,b=apellidos)
busqueda=busqueda.lower()

count=busqueda.count('a')

pos=busqueda.find('lopez')

cambia=busqueda.replace('a','x')

split=busqueda.split(' ')

print(pos)
print(busqueda[9])
print(count)
print(cambia)
print(split)
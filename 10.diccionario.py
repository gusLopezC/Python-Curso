diccionario ={'a':True,'b':55,5:"esto es un string",(1,2):False,'a':"HOLA",'a':False}
#claves inmutables siempre
diccionario['c']='Nueva cadena'
diccionario['a']=True

valor=diccionario.get('z',"Valor no existe")

del diccionario[5]
print(diccionario)
print(valor)

llaves=list(diccionario.keys())
valores = list(diccionario.values())

diccionario2={'z':23,'w':88}

#extender diccionario con otro diccionario

#diccionario['z']=diccionario2['z']
#diccionario['w']=diccionario2['w']

diccionario.update(diccionario2)
print(llaves)
print(valores)
print(diccionario)

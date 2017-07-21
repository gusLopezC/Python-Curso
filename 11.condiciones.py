fruta='manzana'
verdura='tomate'

if fruta == 'kiwi':
    print("EL valor es kiwi")
    pass
elif fruta=='manzana':
    print("es una manzana")
    pass
elif fruta=='manzana2':
    pass
else:
    print("El valor no es kiwi");
    pass

valor=1
valor2=20
if valor or valor2 >20:
    print("es verdad")
else:
    print("No es verdad")


mensaje='el valor es tomate' if verdura=='tomate' else 'no son igual'
print(mensaje)
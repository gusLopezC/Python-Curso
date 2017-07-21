contador=1

while contador<=10:
    print(contador)
    contador+=1

    if contador==5:
        print('Estamos en el numero 5')

        continue
        break
else:
    print("el while a terminado")
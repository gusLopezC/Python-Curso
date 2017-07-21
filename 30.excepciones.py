
try:

    lista=[1,2]
    print(lista[3])
    print(2/0)

except IndexError as ex:
    print(ex)
except ZeroDivisionError as ex:
    print(ex)
    print("Operacion no valida")
except Exception as ex:
    print("Exception total")
finally:
    print("Script terminado")

class Usuario:

    def __init__(self):
        self.__passowrd='Esto es un secreto'

    def mostrar_pass(self):
        print(self.__passowrd)
usuario= Usuario()
usuario.nombre='Eduardo'
usuario.__passowrd='Ya no lo es'
print(usuario.nombre)

print(usuario.__passowrd)
usuario.mostrar_pass()

print(usuario.__dict__)



##-------Metodos magicos-----


class User:
    def __new__(cls):
        print ("Este metodo es el primero")
        return super().__new__(cls)

    def __init__(self):
        print("Este es el segundo")

    def __str__(self):
        return "Esta mostrando un objeto"

    def __getattr__(self,nombre):
        print("NO se encontro el atributo")

user= User()
print(user)
print(user.apellido)
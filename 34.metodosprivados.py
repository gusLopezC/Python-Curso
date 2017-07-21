import crypt
class usuario:

    def __init__(self,user,password,email):
        self.user=user
        self.__password=self.__generar_password(password)##atributos privados
        self.email=email

    def __generar_password(self,password):
        ##se lo pone doble guion bajo para hacer el metodo privdo
        return password.upper()

    def get_password(self):
        return self.__password

Gustavo=usuario('gustavo','lopez1234','gusano0@hotmail.com')

print(Gustavo.user)
Gustavo.__password='Cambio de contraseña'
#print(Gustavo.password)
print(Gustavo.email)
print(Gustavo.get_password())
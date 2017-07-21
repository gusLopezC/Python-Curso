class usuario:

    def __init__(self,user,password,email):
        self.user=user
        self.__password=self.__generar_password(password)##atributos privados
        self.email=email

    def __generar_password(self,password):
        ##se lo pone doble guion bajo para hacer el metodo privdo
        return password.upper()

#------------Properties deja trabajar con los atributos privados
#------------de una clase o modificarlos

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self,valor):
        self.__password=self.__generar_password(valor)

Gustavo=usuario('gustavo','lopez1234','gusano0@hotmail.com')

print(Gustavo.password)
Gustavo.password='NuevaContraseña'
print(Gustavo.password)
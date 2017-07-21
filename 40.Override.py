class Animal:
   @property
   def terrest(self):
        return True

class Felino(Animal):

   @property
   def garras(self):
        return True
   def cazar(self):
        print("El felino esta cazando")

class Mascota:
    def __init__(self,nombre):
        self.nombre=nombre

    def mostrar_nombre(self):
        print(self.nombre)

class Gato(Felino,Mascota):
    def __init__(self,nombre):
        Mascota.__init__(self,nombre)
    def gatoCazador(self):
        self.cazar()

    def mostrar_nombre(self):#Aqui se realiza la sobreescritura
        Mascota.mostrar_nombre(self)
        print("El nombre del gato es "+self.nombre)
gato=Gato('Pulgas')
gato.mostrar_nombre()

#override sobre escritura de metodos
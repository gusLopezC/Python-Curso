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
   nombre=''
   def monstrar_nombre(self):
        print(self.nombre)

class Gato(Felino,Mascota):

    def gatoCazador(self):
        self.cazar()

#-----------Clae multiple permite importar de mas de 2 clases
#-----------no muchos lenjuages cuentan con esto
gato=Gato()
gato.nombre='Pulgas'

gato.monstrar_nombre()
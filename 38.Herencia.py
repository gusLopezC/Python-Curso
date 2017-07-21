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

class Gato(Felino):

    def gatoCazador(self):
        self.cazar()

class Jaguar(Felino):
    pass

gato = Gato()
jaguar = Jaguar()

print(gato.gatoCazador())
print(jaguar.garras)

print(gato.terrest)

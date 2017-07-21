class Circulo:

    @staticmethod
    def pi():
        return 3.1416

    def __init__(self,radio):
        self.radio=radio

    def area(self):#mETODOS DE INSTANCIA
        return self.radio*self.radio * Circulo.pi()

print(Circulo.pi())

C1=Circulo(4)
print(C1.area())

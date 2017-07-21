class Circulo:
    _pi=3.1416
    def __init__(self,radio):
        self.radio=radio

    def area(self):
        return self.radio*self.radio*self.pi

C1=Circulo(4)
C2=Circulo(6)

print(Circulo.pi)
print(C1.radio)
print(C2.radio)
print(C1.area())
print(C2.area())
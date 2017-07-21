class Lapiz:


    def __init__(self,color="Amarillo",borrador,grafito):
        self.color=color
        self.borrador=borrador
        self.usa_grafito=grafito

    def dibujar(self):
        print("El lapiz esta dibujando")

    def borrar(self):
        if self.si_borra():
            print("El lapiz esta borrando")
        else:
            print("No es posible borrar")
    def si_borra(self):
        return self.borrador

lapiz_generico = Lapiz("Verde",True,False)
lapiz_generico.dibujar()
lapiz_generico.borrar()
lapiz_generico.borrador= True
lapiz_generico.borrar()
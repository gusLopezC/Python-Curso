#from .gato import Gato
from .felinos import Gato


#buscara la clase que tengo el
#nombre despues del punto al mismo nivel

def creador_gato(nombre):
    return Gato(nombre)

CONSTANTE="Constante 1"

#------------------------------------------
#Init sirve para extablecer que queremos importar y
#patrones singleton
import random
import datetime
import sys


valor= random.randrange(1,10)
print (valor)

lista=[True,"String",23,5.43,False]
valor=random.choice(lista)
print(valor)

print(lista)
random.shuffle(lista)
print(lista)

##---------datetime----
print(datetime.datetime.now())

#-----------sys-----------
import time
for i in range(101):
    time.sleep(0.5)
    sys.stdout.write("\r%d %%" % i)
    sys.stdout.flush()
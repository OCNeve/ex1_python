#Faire un programme python indiquant si le nombre d’éléments égaux à un d’une séquence d’entiers binaires est pair ou non.
import random

liste = [random.randint(0, 1)for i in range(0,50)]
nombreDeUn = liste.count(1)
if nombreDeUn % 2 == 0:
     print("pair")
else:
    print("impair")
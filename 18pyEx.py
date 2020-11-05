#Faire un programme python : Avec une valeur saisie par un utilisateur,  le rayon d’un cercle, calculez et affichez le périmètre d’un cercle.

import math #il faut importer la librairie qui permet a python d'utiliser des foctionalitées mathématiques supplémentaire.

print("what radius ?")
rad = input()# float désigne un nombre a vigule, le contraire d'un entier.
circ = float(2)*float(rad)*float(math.pi)#float convertis la valeur en nombre a virgule afin de pouvoir le multiplier avec un autre float.
print(circ)


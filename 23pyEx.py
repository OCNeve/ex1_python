#Faire un programme python qui demande à un utilisateur un entier. Le programme fait la somme des carrées des entiers compris en 1 et la valeur donnée.
a = int(input("entier"))    
somme = 0
for nombre in range(0, a+1):#for créé une boucle dont la longueur est presdeffinit, contrairement a while
    somme += (nombre ** 2)

if a == 1:
    somme = 1
print(somme)


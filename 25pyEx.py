#Faire un programme python qui demande à un utilisateur d’entrer un entier positif. Le programme indique ensuite si l’entier positif est pair ou impair ? Le programme vérifie et redemande l’entier si ce n’est pas un entier positif.
a = int("Entier?")
while a < 0:
    a = int(input("veillez saisir un nombre positif"))
    
if a % 2 == 0:#a % 2 en informatique sert typiquement a savoir si quelque chose est pair
     print("pair")
else:
    print("impair")

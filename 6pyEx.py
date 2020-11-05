#Faire la saisie d’un entier qui sera une durée en secondes. Faire les instructions pour convertit cette valeur en heures, minutes, secondes.
print("how many seconds did it last ?")
time = input()
time = int(time)
minutes = time / 60
hours = minutes / 60
print(time) 
print(minutes)
print(hours)
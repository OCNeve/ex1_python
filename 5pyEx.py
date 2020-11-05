#Faire la saisie de plusieurs données dans des variables différentes et changer les valeurs  des variables uniquement avec l'opérateur =.
print("what is your name ?")
name = input()
print("how old are you ?")
age = input()
print("what is your gender ?")
sex = input()
# store the value for sex as backup
# sex becomes age, age become name, name becomes sex
backup = sex
sex = age
age = name
name = backup
print(name)
print(age)
print(sex)

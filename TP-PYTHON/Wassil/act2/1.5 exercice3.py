#on recherche la somme total quotidienne d'une caisse enregistreuse
s = 0 #variable s = somme
v = 0 #variable v = valeur
while True: #boucle infinie
    v=int(input("Donner chiffre : "))
    s = v+s #additionne la valeur avec la somme
    if v==0: #si la valeur donner est 0
        break #stop la boucle
print('la somme est :',(s))

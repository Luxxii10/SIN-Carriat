
x=int(input("Entrer chiffre : "))
y=x%2 #Le résultat est divisé par 2 jusqu'à ne plus pouvoir être divisable 
if y==0: #Si le résultat est égal à 0
    print("ce nombre est paire", y)
else:
    print("ce nombre est impaire", y)

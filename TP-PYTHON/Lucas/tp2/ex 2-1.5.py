somme=0
while True:
    valuer=0
    valeur=float(input("prix des courses ? "))
    somme=somme+valeur
    if valeur==0:
        print("Total Journalier",somme)
        break
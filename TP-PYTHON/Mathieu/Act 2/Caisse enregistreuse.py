somme=0
while True:
    valeur=0
    valeur=float(input("Prix des courses :")) 
    somme= somme+valeur
    if valeur==0:
        print("Total Journalier",somme)
        break

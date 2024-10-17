
# Définition de la fonction
def table (nb): #on définit la fonction table d'un nombre
    n = 0
    while n <11: #condition de la table jusqu'au nombre x 10 et on affiche chaque étape
        print(n*nb) 
        n = n + 1


# Appel de la fonction
n=int(input("table de ? ")) #on demande a l'utilisateur la table souhaitée
table(n)
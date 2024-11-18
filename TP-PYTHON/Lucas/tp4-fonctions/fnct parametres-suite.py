# Définition de la fonction
def tableMulti(nb,début,fin):
    n=début
    while n<fin+1:
        print(n*nb)
        n = n+1
        
début=int(input("le début de la table: ? "))
fin=int(input("la fin de la table: ? "))
# Appel de la fonction
nb=input ("table de ? ")
tableMulti(nb,début,fin)
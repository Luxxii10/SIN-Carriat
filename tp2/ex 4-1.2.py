#Calcul d'un polygone a n cotés 

n=int(input("Le nombre de cotés: "))

perimetre=0

for i in range(n):
    taille=float(input("la taille du coté " + str(i+1) + " : "))
    perimetre=perimetre+taille
   
print("le périmètre du polygone est ",perimetre)    
# Calcul du périmètre d'un polygone à n côtés

print("ATTENTION : utiliser la même unité pour les tailles")
nb_cotes = int(input("Nombre de côtés : "))
perimetre = 0
if nb_cotes != 0:
    for i in range(nb_cotes):
        taille = int(input("Donner la taille du côté " + str(i+1) + " : "))
        perimetre = perimetre + taille
    print("Le pérmiètre est de :", perimetre)
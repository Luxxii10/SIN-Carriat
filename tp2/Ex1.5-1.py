valeur = 20000
nb_annees = 0

while valeur>2000:
    valeur = valeur*0.8
    nb_annees = nb_annees + 1
print("La valeur de la voiture est descendue en dessous des 2 000 euros au bout de", nb_annees, "ans (", valeur, ")")

valeur = 20000
valeur_moitie = valeur / 2
nb_annees = 0

while valeur > valeur_moitie:
    valeur = valeur*0.8
    nb_annees = nb_annees + 1
print("La valeur est environ à la moitié au bout de", nb_annees, "ans", valeur)
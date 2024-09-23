# Pair ou impair ?
# Demande un nombre à l'utilisateur et indique s'il est pair ou non

def loop(): # pour exécuter le script en boucle
    x = int(input("Donne un nombre : ")) # demande le nombre à l'utilisateur 
    if x%2 == 0: #si le reste de la division x / 2 est nul
        print("Le nombre est pair")
    else: # si le reste n'est pas nul
        print("Le nombre est impair")
    loop()
loop()
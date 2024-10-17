#Déclaration des variables
largeur = 5

# Définition des fonctions 
def cube_1 (hauteur): #Déclaration de 2 variables locales, même si nom identique avec prog principal 
     profondeur=10
     largeur = 10
     return largeur*profondeur*hauteur #fomule du volume

def cube_2 (hauteur):        # Ici, largeur est pris au niveau du prog principal 
     profondeur=10
     return largeur*profondeur*hauteur #fomule du volume

def cube_3 (hauteur):    # La variable globale largeur sera modifiée dans la fonction 
     global largeur #la variable globale est largeur
     profondeur=10
     largeur = 7
     return largeur*profondeur*hauteur #fomule du volume


# Programme principal
print ("largeur : ", largeur)
print ("Vol cube 1 : ", cube_1 (2)) 
print ("Vol cube 2: ", cube_2 (2))
print ("Vol cube 3 : ", cube_3(2))
print ("La variable globale largeur à été modifiée par la fonction cube_3: ", largeur)
print ("Vol cube 2 : ", cube_2 (2))
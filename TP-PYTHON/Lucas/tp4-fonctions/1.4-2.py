import math #on importe le module MATH pour la fonction PI 

x=float(input("la taille du rayon de ton cercle ? ")) #on demande a l'utilsateur la taille du rayon du cercle

def surfCercle(R): #on définit la fonction surfcercle
    
    x=math.pi*(R)**2 # formule: pi x rayon²
    print(x)
    
surfCercle(x)
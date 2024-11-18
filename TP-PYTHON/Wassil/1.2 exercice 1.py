from random import *
liste=[]
for i in range(10):#Crée une liste de 10 valeur
    liste.append(randint(0,99))#La liste de nombre est compris entre 0 et 99
print(liste)#imprimer la liste
print(liste[4])#imprimer la 4eme valeur 
liste[1]=17#la première valeure est remplacer par 17
liste[3]=liste[2]+liste[4]#la 3eme valeure est remplacer par l'addition de la valeur 2 et 4
print(liste)#imprimer la liste

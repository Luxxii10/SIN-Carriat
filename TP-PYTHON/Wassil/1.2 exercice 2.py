from random import *

#Programme pour la Liste

liste=[]
for i in range(10):
    liste.append(randint(0,99))#Liste compris entre 0 et 99
liste[1]=17
liste[3]=liste[2]+liste[4]
print(liste)

# Programme 

x=int(input("Donner la première case à permuter : "))#demande la première valeur a permuter
value1 = liste[x]

y=int(input("Donner la deuxième case à permuter : "))#demande la deuxieme valeur a permuter
value2= liste[y]

liste[x]=value2#inverse l'emplacement des deux valeur
liste[y]=value1
print(liste)#imprimer liste final

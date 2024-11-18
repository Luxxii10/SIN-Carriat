from random import *

#Programme pour la Liste

liste=[]
for i in range(10):
    liste.append(randint(0,99))
liste[1]=17
liste[3]=liste[2]+liste[4]
print(liste)

# Programme 

x=int(input("Donner la première case à permuter : "))
value1 = liste[x]

y=int(input("Donner la deuxième case à permuter : "))
value2= liste[y]

liste[x]=value2
liste[y]=value1
print(liste)
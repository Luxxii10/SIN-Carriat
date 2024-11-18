from random import *
liste=[]
for i in range(10):
    liste.append(randint(0,99))
print(liste)
print(liste[4])
liste[1]=17
liste[3]=liste[2]+liste[4]
print(liste)
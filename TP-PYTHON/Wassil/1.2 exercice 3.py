#!/usr/bin/env python
#-*- coding: utf-8 -*-

# EModification d'une liste

# Import des librairies
from random import randint


# Déclaration des variables
liste = []

for i in range(10):#répète 10 fois
    liste.append(randint(0, 100))#choisie un nombre aléatoire entre 0 et 99
    print(liste)#imprimer la liste

print("\nEn ajoutant 1\n")#en ajoutant 1
for j in liste:
    liste[liste.index(j)] = j+1#ajoute de 1 la valeur de chaque nombre de la liste
    print(liste)#imprimer la liste

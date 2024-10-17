#Les liste

#Déclaration des variables
s = ['lundi', 'mardi', 230, 'mercredi', 'dimanche']

#Accès aux éléments d'une liste
#Accès simple
print(s)#Imprime la liste
print(s[0])#Imprime le premier choix de la liste
print(s[2])#Imprime le troisième choix de la liste
print(s[-1])#Imprime le cinquième choix de la liste
print(s[-2])#Imprime le quatrième choix de la liste

print("---------------")
#Découpage d'une liste
print(s[1:3])#Imprime le deuxième et troisième choix de la liste
print(s[1:-1])#Imprime le deuxième, troisième et quatrième choix de la liste
print(s[2:])#Imprime le reste de la liste depuis le toisième choix
'\n'
#Opération sur les listes
print(len(s))#donne le nombre de chose dans la liste
del(s[2])#supprime le troisième choix de la liste
print(s)
s = s+['jeudi', 'vendredi']#Ajoute jeudi et vendredi dans la liste
print(s)
print(s*2)#imprime la liste en 2 exemplaire
s[2] = 'bonjour'#ajoute bonjour ds la liste
print(s)
s[0:2] = ['jeudi', 38]#remplace lundi et mardi par jeudi, 38
print(s)
#Fonctions avancées
print("--------Fonctions avancées")
s.append('samedi')#ajoute samedi
print(s)
s.insert(3, 'tyty')#ajoute tyty en tant que quatrième choix de la liste
print(s)
s.remove('bonjour')#suprime bonjour
print (s)
s.pop (1)#supprime 38
print(s)
s.pop()#supprime samedi
print(s)
print(s.index('tyty'))
s.reverse()#inverse la liste
print(s)
s.sort()#change aléatoirement la liste
print (s)

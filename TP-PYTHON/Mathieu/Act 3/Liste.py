s=["lundi","mardi",230,"mercredi","dimanche"]  #variables declarer

print(s)
print(s[0])
print(s[2])
print(s[-1])
print(s[-2])

print("---------------------------------")
#Découpage d'une liste
print(s[1:3])   #Donne le 2e et 4e mot de la liste
print(s[2:])    #Donne du 2e a la fin de la liste

print("---------------------------------")
print("---------------------------------")

#Opérations sur une liste
print(len(s))           #Imprime le nombre de mot dans la liste 
del(s[2])               #Supprime le 3e mot de la liste
print(s)
print(s*2)
s[2]="bonjour"          #Donne au 3e mot dans la liste, bonjour(qui avait été supprimer)
print(s)
s[0:2]=["jeudi",38]     #Donne au 1er et 3e mot dans la liste, jeudi et 38 
print(s)

print("---------------------------------")
print("---------------------------------")

#Fonctions avancées
print("--------Fonction avancées--------")
s.append("samedi")          #Rajoute samedi à la liste
print(s)
s.insert(3, "tyty")         #Rajoute tyty dans la liste à la position 4
print(s)
s.remove("bonjour")         #Remove bonjour
print(s)
s.pop(1)                    #Fais disparaitre le mot en position 2
print(s)
s.pop()                     #Fais disparaitre le dernier mot
print(s)
print(s.index("tyty"))      #Imprime la position du mot tyty
s.reverse()                 #Inverse les mots de la liste
print(s)
s.sort()                    #Tri par ordre alphabétique
print(s)
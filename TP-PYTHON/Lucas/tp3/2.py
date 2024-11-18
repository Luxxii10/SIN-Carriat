
# Les listes
# Déclaration des variables
s=['lundi','mardi', 230, 'mercredi','dimanche']
# Accès aux éléments d'une liste
#Accès simple
print (s) #print de la liste vierge
print (s[0]) #print lundi
print (s[2]) #print 230
print (s[-1]) #print dimanche
print (s[-2]) #print mercredi
print("-----------------------------------------")
# Découpage d'une liste
print (s[1:3]) #print mardi et 230
print (s[1:-1]) #print mardi et 230 mercredi
print (s[2:]) #print 230 mercredi et dimanche
print("-----------------------------------------")
# Opérations sur les listes 
print(len(s))
del (s[2])
print(s)
s= s+['jeudi','vendredi']
print (s)
print(s*2)
s[2] ='bonjour'
print(s)
s[0:2] = ['jeudi',38]
print (s)
print("-----------------------------------------")
s.append('samedi')
print(s)
s.insert(3,'tyty')
print(s)
s.remove('bonjour')
print(s)
s.pop(1)
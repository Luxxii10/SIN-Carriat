n = int(input("Entrer nombre d'étage : "))#demande le nombre d'étage pour calculer le nombre d'orange nécessaire
nombre_orange = 0
for i in range(1, n+1):
    print (i, i**2)
    nombre_orange = nombre_orange + i**2

print (nombre_orange)
print('il vous faut', (nombre_orange), 'oranges')

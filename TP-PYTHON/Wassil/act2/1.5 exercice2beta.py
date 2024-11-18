n=int(input("Entrer chiffre : "))
c=0
for i in range(1,n+1):
    if n%i==0: #si la division en boucle est égale a 0
        c=c+1
        print(i)
if c==2: #si il y a 2 résultats
    print('le chiffre est un nombre premier')
else:
    print('le chiffre n_est pas un nombre premier')

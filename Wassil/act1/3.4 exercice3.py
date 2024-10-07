x=float(input("Entrer le nombre de km: "))#vous demande le nombre de km parcourue
if x<100: #si le véhicule a parcouru moins de 100km
    c=0.35*x+60
else:#sinon
    c=0.45*(x-100)+100+60
print("Cout de la location: ", c)

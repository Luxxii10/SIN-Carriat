total = 0
print("Ajout de nombres - 0 pour quitter")

while True:
    n = int(input(str(total) + " + "))
    if n == 0:
        print("Le total enregistré est :", total)
        break
    total = total + n

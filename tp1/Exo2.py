def loop():
    n = int(input("Entrer n : "))
    x = 80 + 10.5*n
    y = 17*n
    if x<y:
        print("Le tarif A est le plus aventageux")
    else:
        print("Le tarif B est le plus avantageux")
    loop()
loop()
def loop():
    x = float(input("Entrer le nombre de km : "))
    if x <= 100:
        c = 60+(0.35+x)
    else:
        c = 60+35+(0.45*(x-100))
    print("Coût de a location : ", c, " euros")
    loop()
loop()
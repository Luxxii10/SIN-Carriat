def loop():
    x = float(input("Donner un nombre : "))
    y = -x
    print("L'opposé est : ", y)
    loop()
loop()
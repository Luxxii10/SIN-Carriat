def loop():
    x = int(input("Donner une année de naissance : "))
    y = 2024-x
    print("Tu as", y, "ans")
    loop()
loop()
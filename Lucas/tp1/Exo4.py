def loop():
    x = float(input("x = "))
    y = x**2
    z = x**3
    if y>z:
        print("Le plus grand nombre est y (x au carré) qui vaut : ", y)
    else:
        print("Le plus grand nombre est z (x au cube) qui vaut : ", z)
    loop()
loop()
a=int(input("Donner le premier nombre "))
b=int(input("Donner le deuxième nombre "))

r=a%b

while True :
    while r==0:
        print(b)
        break
    else:
        a=b
        b=r
from re import I


n=int(input("Donner un nbr:"))
x=1
y=0
for i in range(1,n+1):
    x=x*I
    print(x)
    y=y+x
print("La factorielle est égale", y)

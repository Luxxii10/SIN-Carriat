x=float(input("x="))
y=x**2
z=x**3
if y<z: #si x**2 est stritement plus pêtit que x**3
    print("le plus grand nombre est x**3 qui vaut : ", y)
else: #sinon
    print("le plus grand nombre est x**2 qui vaut : ", z)

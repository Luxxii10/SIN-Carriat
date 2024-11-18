def loop():
   
    nombre=int(input("donne ton nombre !  "))
    resultat=nombre%2
    
    if resultat==0:
        print("ton nombre est pair")
    else:
        print("ton nombre est impair")
         

    loop()
loop()
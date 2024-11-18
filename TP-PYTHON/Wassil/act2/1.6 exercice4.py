x = int(input("Entrer un nombre : "))#Demande un nombre
y = int(input("Entrer début intervalle : "))#Demande le début de l'intervalle
z = int(input("Entrer fin intervalle : "))#demande la fin de l'intervalle
while (x):#le nombre doit être compris entre y et z
    if x>y and x<z:#si le nombre est bien compris dans l'intervalle
        print('Votre nombre est bien dans l`intervalle proposer')
        break#casser la boucle
    else:#sinon
        print('Votre nombre n`est pas compris dans votre intervalle proposer')
        a = int(input("Voulez vous réessayer taper 1-oui, 2-non : "))
        if a==2:
            print('programme terminer')
            break
        else:
            print('Pour continuer taper F5')
            break


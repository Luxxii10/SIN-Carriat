x=float(input("\nla longeur de ta boite ? ")) #on définit les côtes de notre boite avec x,y,z 
y=float(input("\nla largeur de ta boite ? "))
z=float(input("\nla hauteur de ta boite ? "))


def volBoite(x,y,z):
    
    résultat=x*y*z
    print("\n",résultat)
    
volBoite(x,y,z)
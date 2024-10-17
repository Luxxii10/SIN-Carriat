a=float(input("\n1er nombre: ")) #on définit les nombres choisis avec a,b,c
b=float(input("\n2e nombre: "))
c=float(input("\n3e nombre: "))

def maximum(a,b,c):
    if a>b:
        print(a,"est plus grand que",b)
    else:
        print("\n","\n",a,"est plus petit que",b) 
    
    if b>c:
        print("\n",b,"est plus grand que",c)
    else:
        print("\n",b,"est plus petit que",c)
        
    if c>a:
        print("\n",c,"est plus grand que",a)
    else:
        print("\n",c,"est plus petit que",a)
    
maximum(a,b,c)
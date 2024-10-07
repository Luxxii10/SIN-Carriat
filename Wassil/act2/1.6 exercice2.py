x = int(input("Entrer x :"))
i = int(input("Entrer début intervalle :"))
f = int(input("Entrer fin intervalle :"))
p = int(input("Entrer nombre pas"))
for i in range (i, f):
    rés = i**2-2*i-2
    print ('f(', (x), ')=',(rés), 'dans l`intervalle [', (i), ',', (f), ']')


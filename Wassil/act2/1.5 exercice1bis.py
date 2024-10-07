#On recherche en combien d'année la valeur du véhicule proposer baissera jusqu'a la valeur demander

v_final = int(input("Le prix du véhicule neuf :  "))
n = float(input("taux de diminution de la valeur de base : "))
nombre_année = 0
while v_final > 6000 :#la boucle continue si la valeur final est toujours supérieur a 2000€
    v_final = v_final*n
    nombre_année = nombre_année + 1
    print('Le véhicule aura une valeur de', (v_final), '€ au bout de', (nombre_année), 'ans') 

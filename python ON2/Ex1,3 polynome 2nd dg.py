"""
Exercice 1.3 :
Écrire un code permettant de déterminer les racines d’un polynôme du second degré ax2+bx+c. On fournira
les 3 nombres « a », « b » , « c » et on calculera le discriminant « delta ». 
Selon la valeur négative, nulle ou positive de « delta », calculer et afficher les 
racines réelles du trinôme : « x12 » si racine double, « x1 » et « x2» 
si racines distinctes. Attention au cas « a = 0 » ...
Essayer avec (a=10,b=20,c=30) , (a=4,b=12,c=9) , (a=1,b=16,c=4) , (a=0,b=1,c=-1)
"""
from math import *

def polynome(a,b,c):
    delta = (b**2) - (4*a*c)
    
    if a == 0: 
        print("La solution est X1 =", -c/b)
    
    elif delta == 0:
        racine = -b/(2*a)
        print("La solution est x =", racine)
    elif delta > 0:
        racine1 = (-b-(sqrt(delta)))/(2*a)
        racine2 = (-b+(sqrt(delta)))/(2*a)
        print("Les deux racines sont x1 = {} et x2 = {}".format(racine1, racine2))
        
    elif delta < 0:
        print("Pas de solution réelle")


a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

polynome(a,b,c)
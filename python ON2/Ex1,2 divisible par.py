"""
Exercice 1.2
Écrire dans un script un test permettant de savoir si « z », un nombre entier donné par l’utilisateur, 
est divisible par 2, par 3 ou par 5. Préciser aussi si « z » n’est divisible ni par 2, ni par 3, 
ni par 5. Tester avec 24, 35, 49 et 60.
Pour aller plus loin : généraliser le code pour gérer une liste de diviseurs quelconque.
"""

def divisible(z,n):
    liste = []
    for i in range(n):
        elem = int(input("diviseur{}: ".format(i+1)))
        liste.append(elem)
    for elem in liste:
        if z%elem==0:
            print("\n{} est divisible par:".format(z), elem)
        else: print("\n{} n'est pas divisible par:".format(z), elem)


z = int(input('z: '))
n = int(input("nb de diviseurs: "))

divisible(z,n)
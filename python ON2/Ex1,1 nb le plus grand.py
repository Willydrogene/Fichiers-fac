"""
Exercice 1.1
Écrire un code qui trouve les n nombres les plus grands dans une liste donnée.
Pour aller plus loin - ré-écrire le code en utilisant une fonction qui prend en argument la liste et le nombre
n
"""


def fonction(nb_liste, n):
    liste = []
    for i in range(nb_liste):
        elem = int(input())
        liste.append(elem)
    print("ta liste:", liste)
    liste = sorted(liste)
    
    liste2 = []
    while n > 0:
        liste2.append(liste[n+1])
        n -= 1
    liste2 = sorted(liste2)
    print(liste2)

nb_liste = int(input("nb d'elements dans la liste':"))
n = int(input("nb d'elems max="))

fonction(nb_liste, n)
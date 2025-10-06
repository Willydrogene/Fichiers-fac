"""
Exercice 1.4
Lire le fichier “objets_systeme_solaire.txt” qui est disponible sur la page Moodle du cours et qui 
contient une liste d’objets du système solaire. Écrire un script qui parcourt la liste et 
qui indique si l’objet est une planète tellurique 
(c’est-à-dire si l’objet fait partie de la liste Mercure, Venus, Terre, Mars), 
ou bien gazeuse (l’objet fait partie de la liste Jupiter, Saturne, Uranus, Neptune) ; 
sinon, indiquer que l’objet est une planète naine et donner leur nombre.
"""

fichier = open("objets_systeme_solaire.txt", 'r')

liste = fichier.readlines()
liste1 = []
for elem in liste:
    elem = elem.split()
    liste1.append(elem[0])
    

for elem in liste1:
    if elem in ['Mercure', 'Venus', 'Terre', 'Mars']:
        print(elem + " est une planète tellurique.\n")
    else: 
        print(elem + " est une planète gazeuse.\n")
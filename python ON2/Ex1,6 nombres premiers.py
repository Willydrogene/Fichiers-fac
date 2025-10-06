"""
Exercice 1.6 *
Écrire un programme qui donne la liste des nombres premiers entre deux entiers choisis par 
l’utilisateur.
"""

def nb_premier(n1,n2):
    nb_de_nb_premier = 0
    liste = []
    for i in range(n1,n2+1):
        n = 0
        for a in range(2,i):
            if i%a==0:
                n += 1
        if n == 0 and i!=0 and i!=1:
            nb_de_nb_premier += 1
            liste.append(i)
    print("Il y a entre {} et {}: {} de nombres premiers\nIls sont: {}".format(n1,n2,nb_de_nb_premier,
                                                                               liste))
                
    
    
n1 = int(input("n1 = "))
n2 = int(input("n2 = "))

nb_premier(n1,n2)
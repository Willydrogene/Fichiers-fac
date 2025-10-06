#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercice 1.5
Écrire un code qui compte les occurrences de chaque valeur dans une liste. On utilisera le code 
suivant pour générer une liste de 100 entiers entre 0 et 9 inclus :
import random as rd 
rand_list = rd.choices(range(0, 10), k=100)
Pour aller plus loin - ré-écrire le code en utilisant une fonction qui prend la liste d’entiers en argument, et
qui rend une liste qui compte les occurrences de chaque valeur.
"""

import random as rd 
rand_list = rd.choices(range(0, 10), k=100)

def occurence(rand_list):
    rand_list = sorted(rand_list)
    print("La liste générée est:\n", rand_list)
    liste = []
    m = 0
    for elem in rand_list:
        if elem not in liste:
            liste.append(elem)
        else: m += 1
    print("\nIl y a {} occurences".format(m))

occurence(rand_list)
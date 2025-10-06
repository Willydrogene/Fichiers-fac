#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 08:02:50 2025

@author: grw4219a
"""

import numpy as np
import random as rd
import math
import matplotlib.pyplot as plt

# p = 0.3, N = 100, R = 100 et plus tard on peut augmenter R = 500, 1000 etc.

def tirage1(p):
    if rd.random() < p:
        return 1
    else:
        return 0

def tirageN(p,N):
    somme = 0
    for i in range(N):
        somme += tirage1(p)
    return somme

def Rfois(p, N, R):
    return [tirageN(p, N) for i in range(R)]



p = 0.3
N = 100
R = 100

N1 = Rfois(p, N, R)

N2 = N1
N2.sort()  #Faut compter les répétitions et les mettre peut-etre dans un dictionnaire ou liste pour immiter le plt.hist()

moyenne = sum(N1) / len(N1)
var = np.var(N1)

print("Notre premier tirage donne : ", tirage1(p))
print("moyenne = ", moyenne, "\nVariance = ", var)
    
print(N1)
print("\n")
print(N2)


# Tracé de l'histogramme
plt.hist(N1, bins=max(N1)-min(N1), density=True, edgecolor='black', alpha=0.7)
plt.xlabel('Nombre de fois que 1 apparaît')
plt.ylabel('Fréquence normalisée')
plt.title('Histogramme de la somme des tirages')
plt.show()

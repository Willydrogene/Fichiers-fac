import numpy as np
import matplotlib.pyplot as plt

def func_vitesse_particule(t):
    return 10 * t**2 - 5 * t + 2


# Ma fonction un peu plus précise d'intégrale
def rectangle_point_milieu(a, b, n):
    h = (b-a) / n
    somme = 0
    for i in range(n):
        somme += func_vitesse_particule(a + (i+0.5)*h)
    somme *= h
    return somme


tmin = 0
tmax = 2
dt = 0.1
Nt = int((tmax-tmin)/dt)
print(Nt)



resultat_milieu = rectangle_point_milieu(tmin, tmax, Nt)

print("La distance parcourue par la particule est de: {} mètres.".format(resultat_milieu))



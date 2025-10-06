#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:21:54 2024

@author: Willy

sources: https://destination-orbite.net/exploration/vaisseaux-spatiaux/les-vaisseaux-du-programme-apollo
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
import fonc_principales, terre_lune


############################### constantes : système Terre - Vaisseau ###############################
tmin = 0
tmax = 3600*3
dt = 1

masse_terre = 5.972*10**(24)
masse_vaisseau = 14.7*10**3
masse_lune = 7.36*10**(22)
rayon_terre = 6371000
G = 6.67*10**(-11)
g = 9.81
Fp = masse_vaisseau * g + 39840
T_lune = 29*24*3600 + 12*3600 + 44*60 # 29j 12h 44min

#####################################################################################################
Nt = int((tmax - tmin) / dt) + 1
t = np.linspace(tmin, tmax, Nt)

# CI
z = np.zeros(Nt)
z_point = np.zeros(Nt)
zero = np.zeros(Nt)

z[0] = rayon_terre
z_point[0] = 0

fonc_principales.verlet_method(t, masse_vaisseau, g, Fp, z, z_point, dt, Nt)
nb_jours, nb_y, liste_x, liste_y, liste_x_point, liste_y_point = terre_lune.terre_lune()

#z -= rayon_terre

# Vérification de la conversion en minutes si nécessaire
seuil_minutes = 60
if max(t) > seuil_minutes:
    t = t / 60  # Conversion en minutes
    unite_temps = 'Temps t (minutes)'
else: unite_temps = 'Temps t (secondes)'

"""
seuil_km = 1000
if max(z) > seuil_km:
    z = z / 1000  # Conversion en minutes
    unite_z = 'Altitude z (km)'
else: unite_z = 'Altitude z (m)'
"""
z_point *= 3.6

#plt.figure(figsize=(8, 6), dpi=100)

for i in range(nb_jours):
    plt.subplot(1, 2, 1)
    plt.plot(liste_x[i], liste_y[i])
    plt.plot(liste_x[0][0], liste_y[0][0], 'ro')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.subplot(1, 2, 2)
    plt.plot(liste_x_point[i], liste_y_point[i], 'r')
    plt.plot(liste_x_point[0][0], liste_y_point[0][0], 'bo')
    plt.xlabel('Vitesse x')
    plt.ylabel('Vitesse y')

print('nb_y =', nb_y)
ax1 = plt.subplot(1, 2, 1)
# plt.plot(0, 0, 'bo')
# Tracer un cercle représentant la Terre
terre = Circle((0, 0), 6371000, color='blue', alpha=0.5)  # Centre en (0,0), rayon de 6571000m
ax1.add_patch(terre)

plt.subplot(1, 2, 1)
plt.plot(liste_x[-1][-1], liste_y[-1][-1], 'go')

print(liste_x[-1][-1], liste_y[-1][-1])

############### fusée verticale d'où le zéro en x ######################
plt.subplot(1,2,1)
plt.plot(zero, z)

plt.subplot(1,2,2)
plt.plot(zero, z_point)
########################################################################
plt.tight_layout()  # Ajuster automatiquement les espacements entre les sous-graphiques
plt.show()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:18:44 2024

@author: grw4219a
"""

import matplotlib.pyplot as plt
import numpy as np
import fonc_lots
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation


def terre_lune_soleil():
    ############################### constantes : système Terre - Vaisseau ###############################
    tmin = 0
    tmax = 3600*24 + (11*3600)/27
    dt = 1000
    nb_jours = 361

    masse_soleil = 2*10**30
    masse_terre = 5.972 * 10 ** 24
    masse_vaisseau = 14.7*10**3
    masse_lune = 7.36 * 10 ** 22
    rayon_terre = 6371*10**3
    dist_terre_lune = 384400*10**3
    dist_terre_soleil = 149597870 * 10 ** 3
    G = 6.67*10**(-11)
    g = 9.81
    Fp = masse_vaisseau * g + 39840
    T_lune = 29*24*3600 + 12*3600 + 44*60 # 29j 12h 44min
    T_terre = 365.25*24*3600

    #####################################################################################################
    Nt = int((tmax - tmin) / dt) + 1
    t = np.linspace(tmin, tmax, Nt)

    # CI
    x_lune = np.zeros(Nt)
    x_point_lune = np.zeros(Nt)
    y_lune = np.zeros(Nt)
    y_point_lune = np.zeros(Nt)
    x_terre = np.zeros(Nt)
    x_point_terre = np.zeros(Nt)
    y_terre = np.zeros(Nt)
    y_point_terre = np.zeros(Nt)

    x_lune[0] = dist_terre_lune
    x_point_lune[0] = 0
    y_lune[0] = 0
    y_point_lune[0] = np.sqrt((G*masse_terre)/(dist_terre_lune)) #3683.590215 / 3
    x_terre[0] = dist_terre_soleil
    x_point_terre[0] = 0
    y_terre[0] = 0
    y_point_terre[0] = np.sqrt((G * masse_soleil) / (dist_terre_soleil))

    liste_x_terre, liste_y_terre, liste_x_point_terre, liste_y_point_terre, nb_y_vide, nb_y_terre = fonc_lots.lots(t, masse_soleil, G, nb_jours, x_terre, x_point_terre, y_terre, y_point_terre, dt, Nt)
    liste_x_lune, liste_y_lune, liste_x_point_lune, liste_y_point_lune, nb_y_lune, nb_y_vide2 = fonc_lots.lots(t, masse_terre, G, nb_jours, x_lune, x_point_lune, y_lune,
                                                                          y_point_lune, dt, Nt)


    liste_x_lune = [x + y for x, y in zip(liste_x_lune, liste_x_terre)]
    liste_y_lune = [x + y for x, y in zip(liste_y_lune, liste_y_terre)]
    liste_x_point_lune = [x + y for x, y in zip(liste_x_point_lune, liste_x_point_terre)]
    liste_y_point_lune = [x + y for x, y in zip(liste_y_point_lune, liste_y_point_terre)]

    plt.figure(figsize=(10, 6), dpi=100)

    """for i in range(nb_jours):
        plt.subplot(1,2,1)
        plt.plot(liste_x[i], liste_y[i])
        plt.plot(liste_x[0][0], liste_y[0][0], 'ro')
        plt.xlabel('x')
        plt.ylabel('y')

        plt.subplot(1,2,2)
        plt.plot(liste_x_point[i], liste_y_point[i], 'r')
        plt.plot(liste_x_point[0][0], liste_y_point[0][0], 'bo')
        plt.xlabel('Vitesse x')
        plt.ylabel('Vitesse y')

    print('nb_y =',nb_y)
    ax1 = plt.subplot(1,2,1)
    #plt.plot(0, 0, 'bo')
    # Tracer un cercle représentant la Terre
    terre = Circle((0, 0), 6371000, color='blue', alpha=0.5)  # Centre en (0,0), rayon de 6571000m
    ax1.add_patch(terre)

    plt.subplot(1,2,1)
    plt.plot(liste_x[-1][-1], liste_y[-1][-1], 'go')

    print(liste_x[-1][-1], liste_y[-1][-1])

    plt.tight_layout()  # Ajuster automatiquement les espacements entre les sous-graphiques
    plt.show()"""
    return nb_jours, nb_y_lune, liste_x_lune, liste_y_lune, liste_x_point_lune, liste_y_point_lune, nb_y_terre, liste_x_terre, liste_y_terre, liste_x_point_terre, liste_y_point_terre



nb_jours, nb_y_lune, liste_x_lune, liste_y_lune, liste_x_point_lune, liste_y_point_lune, nb_y_terre, liste_x_terre, liste_y_terre, liste_x_point_terre, liste_y_point_terre = terre_lune_soleil()

for i in range(nb_jours):
    plt.subplot(1, 2, 1)
    plt.plot(liste_x_terre[i], liste_y_terre[i], 'b')
    plt.plot(liste_x_terre[0][0], liste_y_terre[0][0], 'bo')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.subplot(1, 2, 1)
    plt.plot(liste_x_lune[i], liste_y_lune[i], 'r')
    plt.plot(liste_x_lune[0][0], liste_y_lune[0][0], 'ro')
    plt.xlabel('x')
    plt.ylabel('y')


    plt.subplot(1, 2, 2)
    plt.plot(liste_x_point_terre[i], liste_y_point_terre[i], 'b')
    plt.plot(liste_x_point_terre[0][0], liste_y_point_terre[0][0], 'bo')
    plt.xlabel('Vitesse x')
    plt.ylabel('Vitesse y')
    plt.subplot(1, 2, 2)
    plt.plot(liste_x_point_lune[i], liste_y_point_lune[i], 'r')
    plt.plot(liste_x_point_lune[0][0], liste_y_point_lune[0][0], 'ro')
    plt.xlabel('Vitesse x')
    plt.ylabel('Vitesse y')

print('nb_y_lune =', int(nb_y_lune[0]/2))
print('nb_y_terre =', int(nb_y_terre[0]))

"""
ax1 = plt.subplot(1, 2, 1)
# plt.plot(0, 0, 'bo')
# Tracer un cercle représentant la Terre
terre = Circle((0, 0), 6371000, color='blue', alpha=0.5)  # Centre en (0,0), rayon de 6571000m
ax1.add_patch(terre)
"""
ax1 = plt.subplot(1, 2, 1)
# plt.plot(0, 0, 'bo')
# Tracer un cercle représentant la Terre
soleil = Circle((0, 0), 696340000, color='yellow', alpha=0.5)  # Centre en (0,0), rayon de 6571000m
ax1.add_patch(soleil)

plt.subplot(1, 2, 1)
plt.plot(liste_x_lune[-1][-1], liste_y_lune[-1][-1], 'mo')
plt.plot(liste_x_terre[-1][-1], liste_y_terre[-1][-1], 'go')
plt.text(-(149597870 * 10 ** 3)/2, 0, int(nb_y_lune[0]/2), fontsize=12)
plt.text((149597870 * 10 ** 3)/2, 0, int(nb_y_terre[0]/8), fontsize=12)
print('lune:', liste_x_lune[-1][-1], liste_y_lune[-1][-1])
print('terre:', liste_x_terre[-1][-1], liste_y_terre[-1][-1])

plt.tight_layout()  # Ajuster automatiquement les espacements entre les sous-graphiques
plt.show()


"""
# Initialiser la figure et l'axe
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], lw=2)

# Fonction d'initialisation de l'animation
def init():
    ax.set_xlim(0, 384400*10**3 + 149597870 * 10 ** 3)
    ax.set_ylim(0, 384400*10**3 + 149597870 * 10 ** 3)
    return line, line2

# Fonction à appeler à chaque frame pour mettre à jour les données
def update(frame):
    line.set_data(liste_x_lune[0][:frame], liste_y_lune[0][:frame])
    line2.set_data(liste_x_terre[0][:frame], liste_y_terre[0][:frame])
    return line, line2

# Créer l'animation
for i in range(nb_jours):
    ani = FuncAnimation(fig, update, frames=len(liste_x_lune[0]), init_func=init, blit=True)

# Afficher l'animation
plt.show()
"""
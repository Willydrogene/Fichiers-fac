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

def terre_lune():
    ############################### constantes : système Terre - Vaisseau ###############################
    tmin = 0
    tmax = 3600*24 + (11*3600)/27
    dt = 100
    nb_jours = 27

    masse_terre = 5.972 * 10 ** 24
    masse_vaisseau = 14.7*10**3
    masse_lune = 7.36 * 10 ** 22
    rayon_terre = 6371*10**3
    dist_terre_lune = 384400*10**3
    G = 6.67*10**(-11)
    g = 9.81
    Fp = masse_vaisseau * g + 39840
    T_lune = 29*24*3600 + 12*3600 + 44*60 # 29j 12h 44min

    #####################################################################################################
    Nt = int((tmax - tmin) / dt) + 1
    t = np.linspace(tmin, tmax, Nt)

    # CI
    x = np.zeros(Nt)
    x_point = np.zeros(Nt)
    y = np.zeros(Nt)
    y_point = np.zeros(Nt)

    x[0] = dist_terre_lune
    x_point[0] = 0
    y[0] = 0
    y_point[0] = np.sqrt((G*masse_terre)/(dist_terre_lune)) #3683.590215 / 3

    liste_x, liste_y, liste_x_point, liste_y_point, nb_y, nb_y_t = fonc_lots.lots(t, masse_terre, G, nb_jours, x, x_point, y, y_point, dt, Nt)

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
    return nb_jours, nb_y, nb_y_t, liste_x, liste_y, liste_x_point, liste_y_point
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 08:48:47 2025

@author: grw4219a
"""


import matplotlib.pyplot as plt
import random as rd
from math import *

## ----> decommenter sur spyder, dans un terminal il faut le commenter !!!!
# %matplotlib

## ----> commenter la ligne suivante si on est en spyder !!!!
fig, (ax1, ax2) = plt.subplots(2, constrained_layout=True)


def faire_plot(x, v, xarg, pxth, varg, pvth, t, beta):
    nbx = 20  ## nombre de boites de l'histogramme de x
    nbv = 16  ## nombre de boites de l'histogramme de v
    t_pause = 0.1  ## temps d'affichage pour un plot
    ## ----> decommenter la ligne suivante si on est en spyder !!!!!
    # fig, (ax1,ax2) = plt.subplots(2,constrained_layout=True)
    ax1.cla()
    ax1.hist(x, bins=nbx, color='white', edgecolor='blue', density=True, \
             label='histogramme')
    ax1.set(title='distribution des positions', xlabel='x', ylabel='p(x)')
    ax1.plot(xarg, pxth, 'y', label='theorie')
    ax1.legend()

    ax2.cla()
    ax2.hist(v, bins=nbv, color='white', edgecolor='blue', density=True, \
             label='histogramme')
    ax2.set(title='distribution des vitesses', xlabel='v', ylabel='p(v)')
    ax2.plot(varg, pvth, 'y', label='theorie')
    ax2.legend()
    fig.suptitle('N = {0:d}   t = {1:g}   T = {2:.5g}'.format(len(x), t, 1 / beta))
    plt.pause(t_pause)


### propostion de parametres

np = 120  ## nombre de particules
vmax = 1
xmax = 2
m = 1
g = 1
dt = 0.05
vsolmax = 1
niter = 20  # nombre d'iterations globales de pas "ntherm*dt"
ntherm = 40  # nombre d'iterations de pas "dt" entre les plots et echanges aleatoires de vitesses
Hmax = 4        # hauteur du plafond chaud
vplafmax = 1.5  # vitesse maximale après rebond du plafond
T0 = 0.5  # Température imposée



x = []
v = []

for i in range(np):
    x.append(rd.random() * xmax)
    v.append(-vmax + 2 * vmax * rd.random())

t = 0


def unpas_de_dt():
    for j in range(np):
        v[j] -= g*dt/2 
        x[j] += v[j] * dt
        
        if x[j] < 0:
            xj = x[j]
            vj = v[j]
            x[j] = 0
            v[j] = math.sqrt(vj**2 + 2*g * abs(xj))
        
        v[j] -= g*dt/2

def echange_vitesse():
    E_avant = sum(0.5 * m * vj ** 2 for vj in v)
    for j in range(np):
    E_apres = sum(0.5 * m * vj ** 2 for vj in v)
    for j in range(np):


def E_moyen():
    e = 0
    for j in range(np):
        e += m * g * x[j] + 0.5 * m * v[j] ** 2
    return e / np


def fonc_pxth(x, beta):
    return beta * m * g * exp(-beta * m * g * x)


def fonc_pvth(v, beta):
    return sqrt(beta * m / (2 * pi)) * exp(-beta * m * v ** 2 / 2)


TT = []  # Tableau de la température
tt = []  # Tableau de temps

Nplot = 100
xarg = [0 for i in range(Nplot)]
pxth = [0 for i in range(Nplot)]
varg = [0 for i in range(Nplot)]
pvth = [0 for i in range(Nplot)]

# boucle 1
for l in range(niter):
    # boucle 2
    for k in range(ntherm):
        t += dt
        unpas_de_dt()
    echange_vitesse()
    emoyen = E_moyen()
    beta = 3 / (2 * emoyen)
    # pour préparer plot T en fonction de t (à la fin)
    tt.append(t)
    TT.append(1 / beta)

    dx = max(x) / Nplot
    vmax2 = max(max(v), -min(v))
    for j in range(Nplot):
        xarg[j] = dx * j
        pxth[j] = fonc_pxth(xarg[j], beta)
        pvth[j] = fonc_pvth(varg[j], beta)
    faire_plot(x, v, xarg, pxth, varg, pvth, t, beta)

plt.figure()
plt.plot(tt, TT)
plt.xlabel('temps')
plt.ylabel('Température T')
plt.title('Évolution de la température')
plt.grid()
plt.show()

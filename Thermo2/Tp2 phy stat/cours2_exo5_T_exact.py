#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import random as rd
from math import *

fig, (ax1, ax2) = plt.subplots(2, constrained_layout=True)

def faire_plot(x, v, xarg, pxth, varg, pvth, t, beta):
    nbx = 20
    nbv = 16
    t_pause = 0.1
    ax1.cla()
    ax1.hist(x, bins=nbx, color='white', edgecolor='blue', density=True, label='histogramme')
    ax1.set(title='distribution des positions', xlabel='x', ylabel='p(x)')
    ax1.plot(xarg, pxth, 'y', label='theorie')
    ax1.legend()

    ax2.cla()
    ax2.hist(v, bins=nbv, color='white', edgecolor='blue', density=True, label='histogramme')
    ax2.set(title='distribution des vitesses', xlabel='v', ylabel='p(v)')
    ax2.plot(varg, pvth, 'y', label='theorie')
    ax2.legend()
    fig.suptitle('N = {0:d}   t = {1:g}   T = {2:.5g}'.format(len(x), t, 1 / beta))
    plt.pause(t_pause)

np = 120
vmax = 1
xmax = 2
m = 1
g = 1
dt = 0.05
niter = 20
ntherm = 40
T0 = 0.5

x = []
v = []

for i in range(np):
    x.append(rd.random() * xmax)
    v.append(-vmax + 2 * vmax * rd.random())

t = 0

def unpas_de_dt():
    for j in range(np):
        v[j] -= g * dt / 2
        x_old = x[j]
        x[j] += v[j] * dt

        if x[j] < 0:
            E_avant = 0.5 * v[j]**2 + g * x_old
            x[j] = 0
            v[j] = sqrt(2 * E_avant)  # vers le haut
            if v[j] < 0:
                v[j] = -v[j]

        v[j] -= g * dt / 2


def E_moyen():
    e = 0
    for j in range(np):
        e += g * x[j] + 0.5 * v[j] ** 2
    return e / np

def fonc_pxth(x, beta):
    return beta * g * exp(-beta * g * x)

def fonc_pvth(v, beta):
    return sqrt(beta / (2 * pi)) * exp(-beta * v ** 2 / 2)

TT = []
tt = []

Nplot = 100
xarg = [0 for i in range(Nplot)]
pxth = [0 for i in range(Nplot)]
varg = [0 for i in range(Nplot)]
pvth = [0 for i in range(Nplot)]

for l in range(niter):
    for k in range(ntherm):
        t += dt
        unpas_de_dt()
    emoyen = E_moyen()
    beta = 3 / (2 * emoyen)
    tt.append(t)
    TT.append(1 / beta)

    dx = max(x) / Nplot
    vmax2 = max(max(v), -min(v))
    dv = 2 * vmax2 / Nplot
    for j in range(Nplot):
        xarg[j] = dx * j
        pxth[j] = fonc_pxth(xarg[j], beta)
        varg[j] = -vmax2 + dv * j
        pvth[j] = fonc_pvth(varg[j], beta)
    faire_plot(x, v, xarg, pxth, varg, pvth, t, beta)

plt.figure()
plt.plot(tt, TT)
plt.xlabel('temps')
plt.ylabel('Température T')
plt.title('Évolution de la température')
plt.grid()
plt.show()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercice 2.1 : On veut tracer la déviation D du rayon lumineux lorsqu’il traverse un prisme d’angle au
sommet A = π/3 en fonction de l’angle d’incidence i. Les lois du prisme sont i variant de 0 à π/2, 
r est obtenu par sin(i) = n × sin(r), r′ par r′ = A − r et finalement lorsque c’est possible, 
i′ par sin(i′) = n × sin(r′). La déviation D du prisme que l’on veut tracer vaut : D = i + i′ − A.
Dans un premier temps, considérer une seule longueur d’onde (donc n = 1.5 pour le rouge par exemple) 
et accepter d’avoir un avertissement de la fonction arcsin lorsque l’argument est supérieur à 1 
(dans ce cas, elle retourne nan pour “not a number” qui se manipule comme un nombre). 
On affichera la courbe avec les angles en degrés (faire une simple multiplication dans le np.plot).
Dans un second temps, si on a un peu plus de temps, ajouter une seconde longueur d’onde 
(n = 1.6 pour le bleu par exemple) et modifier le programme pour ne plus avoir de message 
d’avertissement (nan s’obtient avec np.nan).
Pour aller plus loin Ajouter plusieurs longueurs d’onde, et afficher toutes les courbes 
ensembles avec une légende par courbe.
"""

import numpy as np
import matplotlib.pyplot as plt

lambdas = [650, 450, 401]
ns = [1.5, 1.6, 1.7]
A = np.pi/3
i = np.linspace(0, np.pi/2, 1000)

plt.figure()

for lambda_, n in zip(lambdas, ns):
    r = np.arcsin(n*np.sin(i))
    r_ = A - r
    i_ = np.arcsin(np.clip(n*np.sin(r_), -1, 1))
    D = np.degrees(i + i_ - A)
    plt.plot(np.degrees(i), D, label='lambda = {} nm'.format(lambda_))


plt.grid()
plt.xlabel('Angle d\'incidence (degrés)')
plt.ylabel('Déviation (degrés)')
plt.title('Déviation d\'un rayon lumineux dans un prisme')
plt.legend()
plt.show()

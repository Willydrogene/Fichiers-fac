"""
Exercice 4.1 : Fonction pour une interpolation linéaire : Écrire une fonction qui prend 
comme argument x1, x2, y1, y2 et x et qui renvoie la valeur y issue d’une interpolation linéaire.
"""

import matplotlib.pyplot as plt


# On place deux points qu'on n'affiche pas afin de délimiter l'étendue des axes
plt.figure(figsize=(6, 4), dpi=100) 
plt.plot(-1, -1, 'P')
plt.plot(2, 2, 'P')
plt.axis('equal')  # Trace un repère orthonormé

def f(x):
    return x**2

x = [1, 1.2]
y = [1, 1.44]
titre = ['A1', 'A2', 'A3']
couleur = ['b','r', 'y']

xx = 1.1
yy = f(xx)
print('xx = {} et yy = {}'.format(xx,yy))

x.append(xx)
y.append(yy)

for i in range(len(x)):
    plt.quiver(0, 0, x[i], y[i], angles = 'xy', scale_units = 'xy', scale = 1, 
               label=titre[i], color=couleur[i])  # Tracé d'un vecteur

plt.plot(x, y)
plt.grid()
plt.legend()
plt.show()

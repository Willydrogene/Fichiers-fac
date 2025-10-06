"""
Exercice 4.1 : Fonction pour une interpolation linéaire : Écrire une fonction qui prend 
comme argument x1, x2, y1, y2 et x et qui renvoie la valeur y issue d’une interpolation linéaire.
"""

import matplotlib.pyplot as plt


# On place deux points qu'on n'affiche pas afin de délimiter l'étendue des axes
plt.figure(figsize=(6, 4), dpi=100) 
plt.plot(-2, -2, 'P')
plt.plot(15, 15, 'P')
plt.axis('equal')  # Trace un repère orthonormé

x1 = 1
x2 = 3
y1 = 3
y2 = 9
x = 6

def f(x1, x2, y1, y2, x):
    coeff = y1 / x1
    if coeff == (y2/x2):
        print('y =', x*coeff, '\nLe coeff directeur est : ', coeff)
        return x*coeff
    else: 
        print('Pas linéaire')
        return x*(y2/x2)

x_liste = [0, x1, x2, x]
y_liste = [0, y1, y2]
titre = ['A1', 'A2', 'A3']
couleur = ['b','r', 'y']

y_liste.append(f(x1, x2, y1, y2, x))


for i in range(len(x_liste)-1):
    plt.quiver(0, 0, x_liste[i+1], y_liste[i+1], angles = 'xy', scale_units = 'xy', scale = 1, 
               label=titre[i], color=couleur[i])  # Tracé d'un vecteur

plt.plot(x_liste, y_liste)
plt.grid()
plt.legend()
plt.show()

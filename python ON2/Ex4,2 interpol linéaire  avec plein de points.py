"""
Exercice 4.1 : Fonction pour une interpolation linéaire : Écrire une fonction qui prend 
comme argument x1, x2, y1, y2 et x et qui renvoie la valeur y issue d’une interpolation linéaire.
"""

import matplotlib.pyplot as plt
import random

# On place deux points qu'on n'affiche pas afin de délimiter l'étendue des axes
plt.figure(figsize=(6, 4), dpi=100) 
plt.plot(-2, -2, 'P')
plt.plot(15, 15, 'P')
plt.axis('equal')  # Trace un repère orthonormé

x_liste = [0.0]
y_liste = [0.0]
couleurs = ['g','y', 'b']
couleur = []
titre = []

n = 10
p = 0
for i in range(n):
    x_liste.append(random.uniform(x_liste[i], x_liste[i]+2))
    y_liste.append(random.uniform(1.0, 10.0))
    titre.append('A'+str(i+1))
    if p>2:
        p = 0
    couleur.append(couleurs[p])
    p += 1
    if i == n-1:
        couleur.append(couleurs[p])
        titre.append('A'+str(i+2))

"""  
x1 = 1
x2 = 3
y1 = 7
y2 = 8
x = 10
"""

xj = x_liste[-2]
yj = y_liste[-2]
xj_1 = x_liste[-1]
yj_1 = y_liste[-1]

x = 5
x_liste.append(x)

def f(xj, xj_1, yj, yj_1, x):
    y = yj + (x-xj)*(yj_1-yj)/(xj_1-xj)
    print('y =', y)
    return y

#x_liste = [0, x1, x2, x]
#y_liste = [0, y1, y2]
#titre = ['A1', 'A2', 'A3']
#couleur = ['g','y', 'b']

y_liste.append(f(xj, xj_1, yj, yj_1, x))

x_liste = sorted(x_liste)
y_liste = sorted(y_liste)


# A commenter si on veut pas les vecteurs tracés
for i in range(len(x_liste)-1):
    plt.quiver(0, 0, x_liste[i+1], y_liste[i+1], angles = 'xy', scale_units = 'xy', scale = 1, 
               label=titre[i], color=couleur[i])  # Tracé d'un vecteur


print(x_liste, '\n', y_liste, '\n', couleur, '\n', titre)

plt.plot(x_liste, y_liste, color='r', label='x,y')
plt.grid()
plt.legend()
plt.show()

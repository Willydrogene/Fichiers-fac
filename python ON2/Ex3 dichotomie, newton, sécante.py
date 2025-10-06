#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercice 3.1
Trouver la racine positive de x² − 2 = 0 en utilisant la méthode de la dichotomie
Comme indiqué plus haut, la méthode de dichotomie nécessite deux valeurs de départ qui encadrent la
solution. Elle a l’avantage de converger systématiquement mais le désavantage de converger lentement. 
Nous allons maintenant nous intéresser à d’autres méthodes, appelées “méthodes ouvertes”.
Les méthodes ouvertes peuvent démarrer avec une seule valeur (ou deux valeurs qui n’encadrent 
pas forcément la solution) et convergent plus rapidement. Cependant, et contrairement à la méthode
de dichotomie, ces méthodes peuvent diverger.
"""

from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

fenetre = Tk()

###################################DICHOTOMIE##################################
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 4), dpi=100) 

# Définir la fonction
def f(x):
    return x ** 2 - 2

def dichotomie(f, a, b, précision):
    test_points = []
    
    while (b-a)/2 > précision:
        c = (a + b) / 2
        test_points.append(c) # Ajouter le point de test
        if f(c) == 0:
            return c, test_points
        elif f(a)*f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2, test_points

a = 0.0 # borne inférieure
b = 2.0 # borne supérieure
précision = 1e-6 # précision
racine, test_points = dichotomie(f, a, b, précision)

x = np.linspace(-2, 2, 1000)
y = f(x)
plt.plot(x, y, label='f(x)', color='m')

plt.plot(racine, 0, 'ro', label='racine')

plt.plot(test_points, f(np.array(test_points)), 'ko', label='points de test')

print(f"La racine positive de l'équation x^2 - 2 = 0 est : {racine}")

plt.legend()
plt.grid()
plt.show()





###################################NEWTON######################################

plt.figure(figsize=(6, 4), dpi=100) 

def f_prime(x):
    return 2 * x

def newton(f, f_prime, x0, précision):
    xn = x0
    while abs(f(xn)) > précision:
        xn = xn - f(xn) / f_prime(xn)
    return xn

# Trouver la racine positive de f(x) = x^2 - 2 avec la méthode de Newton
x0 = 1.0 # valeur initiale
racine = newton(f, f_prime, x0, précision)

x = np.linspace(-2, 2, 1000)
y = f(x)
plt.plot(x, y, label='f(x)', color='y')

plt.plot(racine, 0, 'ro', label='racine')

print(f"La racine positive de l'équation x^2 - 2 = 0 est : {racine}")


plt.legend()
plt.grid()
plt.show()





###################################SÉCANTE#####################################

import numpy as np
import matplotlib.pyplot as plt

# Définir la fonction
def f(x):
    return x**2 - 2

# Définir la méthode de la sécante
def secante(f, x0, x1, précision, max_iter):
    """
    Implémente la méthode de la sécante pour trouver la racine d'une fonction f à partir des deux points x0 et x1, avec une précision de tol et un nombre maximal d'itérations max_iter.
    """
    for i in range(max_iter):
        x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
        if abs(x2 - x1) < précision:
            return x2
        x0, x1 = x1, x2
    return x1

# Trouver la racine positive de f(x) = x^2 - 2 avec la méthode de la sécante
x0 = 1.0
x1 = 2.0
précision = 1e-6
max_iter = 100
racine = secante(f, x0, x1, précision, max_iter)

# Afficher la valeur numérique de la racine
print(f"La racine positive de l'équation x^2 - 2 = 0 est : {racine}")

fenetre.title("Méthode Sécante")
fig = plt.figure(figsize=(6, 4), dpi=100) 


# Tracer la fonction f(x) = x^2 - 2 ainsi que la droite sécante utilisée dans la méthode de la sécante
x = np.linspace(-2, 2, 1000)
y = f(x)
x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
y2 = f(x2)
plt.plot(x, y, label='$f(x) = x^2 - 2$')
plt.plot([x0, x1], [f(x0), f(x1)], 'ko--', label='Droite sécante')
plt.plot([x2], [y2], 'ro', label='Nouvelle approximation')
plt.legend()
plt.grid()
plt.show()



canvas = FigureCanvasTkAgg(fig, master=fenetre)
canvas.draw()
canvas.get_tk_widget().pack()

fenetre.mainloop()
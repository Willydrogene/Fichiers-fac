import numpy as np
import matplotlib.pyplot as plt
import random


def lj(x, j, x_liste):
    L=1
    for i in range(len(x_liste)):
        if j != i:
            L = L * (x - x_liste[i]) / (x_liste[j] - x_liste[i])
    return L


def lagrange(x, x_liste, y_liste):
    s = 0.0
    for j in range(len(x_liste)):
        s += y_liste[j] * lj(x, j, x_liste)
    return s


x_interp = np.linspace(0, 8, 100)
y_interp = []


x_liste = [0.0]
y_liste = [0.0]
for i in range(8):
    x_liste.append(random.uniform(x_liste[i], x_liste[i]+2))
    y_liste.append(random.uniform(1.0, 10.0))

"""x_liste = [2, 3, 6,]
y_liste = [4, -10, 36]"""



for i in range(len(x_interp)):
    y_interp.append(lagrange(x_interp[i], x_liste, y_liste))



print('', x_liste, '\n', y_liste)


plt.plot(x_liste, y_liste, color='r', label='Points de données')
plt.plot(x_interp, y_interp, color='g', label='Interpolation de Lagrange')
plt.grid()
plt.legend()
plt.show()

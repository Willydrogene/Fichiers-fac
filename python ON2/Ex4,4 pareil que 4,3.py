import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.cos(x)

x = np.linspace(0, 2*np.pi, num=100)
y = f(x)

x_interp = np.linspace(0, 2*np.pi, num=100)

y_interp = np.interp(x_interp, x, y)

plt.plot(x, y, 'go', label='Points d\'origine')
plt.plot(x_interp, y_interp, 'r-', label='Fonction interpolée')
plt.legend(loc='best')
plt.show()

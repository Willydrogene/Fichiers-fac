import matplotlib.pyplot as plt
import numpy as np


def f(t, k, m):
    return 0.01 * np.cos((k/m) * t)


def func_1er_ordre(t, x_point):
    dx_dt = x_point
    return dx_dt


def func_2eme_ordre(t, g, omega, x, Q, x_point, xo):
    dx_point_dt = - omega/Q * x_point -omega**2 * x -g
    return dx_point_dt


# Méthode Verlet d'ordre 2 (plus précise qu'Euler logiquement)
def verlet_method(x_verlet, x_point_verlet, dt, Nt, m, g, xo, k, t):
    for i in range(1, Nt):
        x_half = x_verlet[i - 1] + x_point_verlet[i - 1] * dt / 2  # Il faut imaginer la méthode trapèzes des intégrales
        temp_x_point_verlet = x_point_verlet[i - 1] + func_2eme_ordre(t, g, omega, x_half, Q, x_point_verlet[i - 1], xo) * dt
        x_verlet[i] = x_half + temp_x_point_verlet * dt / 2
        x_point_verlet[i] = temp_x_point_verlet
    return x_verlet, x_point_verlet

tmin = 0
tmax = 10
dt = 0.01
k = 10*10**-4
m = 0.00001
g = 9.8
Nt = int((tmax - tmin) / dt) + 1
t = np.linspace(tmin, tmax, Nt)
omega = np.sqrt(k/m)
amort = 3*np.pi*(1.8*10**(0))*0.1
Q = omega/amort

# CI
x = np.zeros(Nt)
x_point = np.zeros(Nt)
x2 = np.zeros(Nt)
x_point2 = np.zeros(Nt)
xo = 2  # 1 mètre
l = 2
l_point = 0

x[0] = l
x_point[0] = l_point

x2[0] = l
x_point2[0] = l_point

for i in np.arange(Nt - 1):
    x_point[i + 1] = x_point[i] + dt * func_2eme_ordre(t[i], g, omega, x[i], Q, x_point[i], xo)
    x[i + 1] = x[i] + dt * func_1er_ordre(t[i], x_point[i])

verlet_method(x2, x_point2, dt, Nt, m, g, xo, k, t)

plt.figure(figsize=(12, 8))
plt.plot(t, x, color='b', label='Euler')
plt.plot(t, x2, color='r', label='Verlet', alpha=0.5)
plt.xlabel("Temps [s]", size=20)
plt.ylabel("x [m]", size=20)
plt.title("Oscillateur Harmonique x", size=30)
plt.legend(loc='best')

plt.show()
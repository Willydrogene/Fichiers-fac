import matplotlib.pyplot as plt
import numpy as np


def func_1er_ordre(t, teta_point):
    dTeta_dt = teta_point
    return dTeta_dt


def func_2eme_ordre(t, omega, teta):
    dTeta_point_dt = -omega ** 2 * teta
    return dTeta_point_dt


def f(t, omega):
    return teta[0] * np.sin(omega*t)


tmin = 0
tmax = 100
g = 9.8
l = 1
omega = np.sqrt(g/l)
dt = 0.001

Nt = int((tmax - tmin) / dt) + 1
t = np.linspace(tmin, tmax, Nt)

# CI
teta = np.zeros(Nt)
teta_point = np.zeros(Nt)
teta[0] = (np.pi) / 20
teta_point[0] = 0

for i in np.arange(Nt - 1):
    teta[i + 1] = teta[i] + dt * func_1er_ordre(t[i], teta_point[i])
    teta_point[i + 1] = teta_point[i] + dt * func_2eme_ordre(t[i], omega, teta[i])

plt.figure(figsize=(12, 8))
plt.plot(t, teta, color='b', label='theta numérique')
plt.plot(t, f(t, omega), color='r', label="solution analytique", alpha=0.5)
plt.xlabel("Temps [s]", size=20)
plt.ylabel("Angle [rad]", size=20)
plt.title("Oscillateur Harmonique theta", size=30)
plt.legend()

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import numpy as np


def func_1er_ordre(t, teta_point):
    dTeta_dt = teta_point
    return dTeta_dt


def func_2eme_ordre(t, omega, teta):
    dTeta_point_dt = -omega**2 * teta
    return dTeta_point_dt


def func_sin(t, omega, teta):
    dTeta_point_dt_sin = -omega**2 * np.sin(teta)
    return dTeta_point_dt_sin


tmin = 0
tmax = 100
omega = 1
dt = 0.001




Nt = int( (tmax-tmin) / dt ) + 1
t = np.linspace(tmin, tmax ,Nt)


# CI
teta = np.zeros(Nt)
teta_sin = np.zeros(Nt)
teta_point = np.zeros(Nt)
teta_point_sin = np.zeros(Nt)
teta[0] = (np.pi)/20
teta_sin[0] = (np.pi)/20
teta_point[0] = 0
teta_point_sin[0] = 0


for i in np.arange(Nt-1):
    teta[i+1] = teta[i] + dt * func_1er_ordre(t[i], teta_point[i])
    teta_sin[i+1] = teta_sin[i] + dt * func_1er_ordre(t[i], teta_point_sin[i])
    teta_point[i+1] = teta_point[i] + dt * func_2eme_ordre(t[i], omega, teta[i])
    teta_point_sin[i+1] = teta_point_sin[i] + dt * func_sin(t[i], omega, teta_sin[i])
    
    


plt.figure(figsize=(12,8))
plt.plot(t, teta, color='b')
plt.plot(t, teta_sin, color='r', alpha=0.5)
plt.xlabel("Temps [s]", size=20)
plt.ylabel("Angle [rad]", size=20)
plt.title("Oscillateur Harmonique theta", size=30)

plt.figure(figsize=(12,8))
plt.plot(t, teta_point, color='b')
plt.plot(t, teta_point_sin, color='r', alpha=0.5)
plt.xlabel("Temps [s]", size=20)
plt.ylabel("Angle [rad]", size=20)
plt.title("Oscillateur Harmonique theta point", size=30)
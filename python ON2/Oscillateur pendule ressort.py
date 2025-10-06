import matplotlib.pyplot as plt
import numpy as np


def func_1er_ordre_l(t, l_point):
    dl_dt = l_point
    return dl_dt


def func_2eme_ordre_l(t, m, g, mu, d, k, l0, l, l_point, theta, theta_point):
    dl_point_dt = g*np.cos(theta) - (k*(l - l0))/m - (3*np.pi*mu*d*l_point)/m + l*(theta_point**2)
    return dl_point_dt


def func_1er_ordre(t, theta_point):
    dTheta_dt = theta_point
    return dTheta_dt


def func_2eme_ordre(t, m, g, mu, d, k, l, l_point, theta, theta_point):
    dTheta_point_dt = -(g*np.sin(theta))/l - (3*np.pi*mu*d*theta_point)/m - (2*l_point*theta_point)/l
    return dTheta_point_dt


def verlet_method(t, m, g, mu, d, k, l0, l, l_point, theta, theta_point, dt, Nt):
    for i in range(1, Nt):
        theta_half = theta[i - 1] + theta_point[i - 1] * dt / 2  # Il faut imaginer la méthode trapèzes des intégrales
        temp_theta_point_verlet = theta_point[i - 1] + func_2eme_ordre(t[i], m, g, mu, d, k, l[i-1], l_point[i-1], theta_half, theta_point[i-1]) * dt
        theta[i] = theta_half + temp_theta_point_verlet * dt / 2
        theta_point[i] = temp_theta_point_verlet

        l_half = l[i - 1] + l_point[i - 1] * dt / 2  # Il faut imaginer la méthode trapèzes des intégrales
        temp_l_point_verlet = l_point[i - 1] + func_2eme_ordre_l(t[i], m, g, mu, d, k, l0, l_half, l_point[i - 1], theta[i-1], theta_point[i - 1]) * dt
        l[i] = l_half + temp_l_point_verlet * dt / 2
        l_point[i] = temp_l_point_verlet
    return theta, theta_point, l, l_point



tmin = 0
tmax = 10
dt = 0.0001
m = 0.1
g = 9.8
frottements_en_plus = 5000
mu = 1.8*10**(-5) * frottements_en_plus
d = 0.05
l0 = 0.5
k = 10

Nt = int((tmax - tmin) / dt) + 1
t = np.linspace(tmin, tmax, Nt)

# CI
theta = np.zeros(Nt)
l = np.zeros(Nt)
theta_point = np.zeros(Nt)
l_point = np.zeros(Nt)
theta[0] = (np.pi) / 2
l[0] = 0.35
theta_point[0] = 0
l_point[0] = 0

verlet_method(t, m, g, mu, d, k, l0, l, l_point, theta, theta_point, dt, Nt)

plt.figure(figsize=(12, 8))

plt.subplot(3,1,1)
plt.plot(t, theta, color='b', label='angle')
plt.plot(t, l, color='r', alpha=0.5, label='longueur')
plt.xlabel("Temps [s]", size=15)
plt.ylabel("Angle [rad]", size=15)
plt.title("Pendule avec ressort / position", size=20)
plt.legend(loc="best")

plt.subplot(3,1,2)
plt.plot(t, theta_point, color='b', label='vitesse angulaire')
plt.plot(t, l_point, color='r', alpha=0.5, label='vitesse longueur')
plt.xlabel("Temps [s]", size=15)
plt.ylabel("Angle [rad]", size=15)
plt.title("Pendule avec ressort / vitesse", size=20)
plt.legend(loc="best")

plt.subplot(3,1,3)
plt.plot(l * np.sin(theta), l * np.cos(theta), color='b', label='position')
plt.xlabel("x [m]", size=15)
plt.ylabel("y [m]", size=15)
plt.gca().invert_yaxis()
plt.title("Pendule avec ressort / position", size=20)
plt.legend(loc="best")

plt.show()
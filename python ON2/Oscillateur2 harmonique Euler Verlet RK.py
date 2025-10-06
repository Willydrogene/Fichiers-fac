import matplotlib.pyplot as plt
import numpy as np


# dθ/dt = θ_point
def func_1er_ordre(t, theta_point_euler):
    dTheta_dt = theta_point_euler
    return dTheta_dt


# d²θ/dt = - (g * θ) / l   sans frottement en prenant le sin(θ)
def func_2eme_ordre(t, g, l, theta):
    dTheta_point_dt = -(g / l) * np.sin(theta)
    return dTheta_point_dt


# Méthode Euler d'ordre 1
def euler_method(theta_euler, theta_point_euler, dt, Nt):
    for i in np.arange(Nt - 1):
        theta_euler[i + 1] = theta_euler[i] + dt * func_1er_ordre(t[i], theta_point_euler[i])
        theta_point_euler[i + 1] = theta_point_euler[i] + dt * func_2eme_ordre(t[i], g, l, theta_euler[i])
    return theta_euler, theta_point_euler


# Méthode Verlet d'ordre 2 (plus précise qu'Euler logiquement)
def verlet_method(theta_verlet, theta_point_verlet, dt, Nt):
    for i in range(1, Nt):
        theta_half = theta_verlet[i - 1] + theta_point_verlet[i - 1] * dt / 2  # Il faut imaginer la méthode trapèzes des intégrales
        temp_theta_point_verlet = theta_point_verlet[i - 1] + func_2eme_ordre(t[i], g, l, theta_half) * dt
        theta_verlet[i] = theta_half + temp_theta_point_verlet * dt / 2
        theta_point_verlet[i] = temp_theta_point_verlet
    return theta_verlet, theta_point_verlet


# Méthode Runge-Kutta d'ordre 4
def runge_kutta_method(theta_rk, theta_point_rk, dt, Nt):
    for i in range(Nt - 1):
        t = i * dt
        k1_theta = dt * func_1er_ordre(t, theta_point_rk[i])
        k1_theta_point = dt * func_2eme_ordre(t, g, l, theta_rk[i])

        k2_theta = dt * func_1er_ordre(t + dt / 2, theta_point_rk[i] + k1_theta / 2)
        k2_theta_point = dt * func_2eme_ordre(t + dt / 2, g, l, theta_rk[i] + k1_theta / 2)

        k3_theta = dt * func_1er_ordre(t + dt / 2, theta_point_rk[i] + k2_theta / 2)
        k3_theta_point = dt * func_2eme_ordre(t + dt / 2, g, l, theta_rk[i] + k2_theta / 2)

        k4_theta = dt * func_1er_ordre(t + dt, theta_point_rk[i] + k3_theta)
        k4_theta_point = dt * func_2eme_ordre(t + dt, g, l, theta_rk[i] + k3_theta)

        theta_rk[i + 1] = theta_rk[i] + (k1_theta + 2 * k2_theta + 2 * k3_theta + k4_theta) / 6
        theta_point_rk[i + 1] = theta_point_rk[i] + (k1_theta_point + 2 * k2_theta_point + 2 * k3_theta_point + k4_theta_point) / 6

    return theta_rk, theta_point_rk
################################################ Conditions de l'experience ############################################

######################## Conditions initiales ########################
tmin = 0.0           # début de l'expérience  en s
tmax = 100.0         # fin de l'expérience    en s
dt = 0.0001          # temps infinitésimal pour la précision
g = 9.8              # pesanteur
l = 1.00             # longueur de la tige   en  mètre
masse = 0.001        # masse                 en  kg
d = 0.20             # diamètre de ma spĥère en  mètre
mu = 1.8 * 10**(-5)  # viscosité du fluide   en  Pa.s

hauteur_du_laché_initial = np.pi / 2
vitesse_angulaire_initiale = 0


######################## Création de tableaux ########################

Nt = int((tmax - tmin) / dt) + 1
t = np.linspace(tmin, tmax, Nt)

theta_euler = np.zeros(Nt)          # Méthode Euler
theta_point_euler = np.zeros(Nt)    # Méthode Euler
theta_verlet = np.zeros(Nt)         # Méthode Verlet
theta_point_verlet = np.zeros(Nt)   # Méthode Verlet
theta_rk = np.zeros(Nt)             # Méthode Runge-Kutta
theta_point_rk = np.zeros(Nt)       # Méthode Runge-Kutta

theta_euler[0] = hauteur_du_laché_initial           # Méthode Euler
theta_point_euler[0] = vitesse_angulaire_initiale   # Méthode Euler
theta_verlet[0] = hauteur_du_laché_initial          # Méthode Verlet
theta_point_verlet[0] = vitesse_angulaire_initiale  # Méthode Verlet
theta_rk[0] = hauteur_du_laché_initial              # Méthode Runge-Kutta
theta_point_rk[0] = vitesse_angulaire_initiale      # Méthode Runge-Kutta



################################################## Appel des fonctions #################################################

theta_verlet, theta_point_verlet = verlet_method(theta_verlet, theta_point_verlet, dt, Nt)
theta_euler, theta_point_euler = euler_method(theta_euler, theta_point_euler, dt, Nt)
runge_kutta_method(theta_rk, theta_point_rk, dt, Nt)


######################################################### PLOTS ########################################################

plt.figure(figsize=(12, 8))

# Premier sous-graphique : Position Euler et Verlet
plt.subplot(2, 1, 1)  # Grille de 2 lignes, 1 colonne, sous-graphique 2
plt.plot(t, theta_verlet, color='b', label='Position Verlet')
plt.plot(t, theta_euler, color='r', label='Position Euler', alpha=0.5)
plt.plot(t, theta_rk, color='g', label='Position Runge-Kutta')
plt.xlabel("Temps [s]", size=20)
plt.ylabel("Angle [rad]", size=20)
plt.title("Oscillateur Harmonique: position", size=30)
plt.legend(loc="upper right", ncol=3)

# Deuxième sous-graphique : Vitesse angulaire Euler et Verlet
plt.subplot(2, 1, 2)  # Grille de 2 lignes, 1 colonne, sous-graphique 2
plt.plot(t, theta_point_verlet, color='b', label='v. ang. Verlet')
plt.plot(t, theta_point_euler, color='r', label='v. ang. Euler', alpha=0.5)
plt.plot(t, theta_point_rk, color='g', label='v. ang. Runge-Kutta')
plt.xlabel("Temps [s]", size=20)
plt.ylabel("Vit. Ang. [rad/s]", size=20)
plt.title("Oscillateur Harmonique: vitesse angulaire", size=30)
plt.legend(loc="upper right", ncol=3)

plt.tight_layout()  # Ajuster automatiquement les espacements entre les sous-graphiques
plt.show()

"""
plt.figure(figsize=(12,8))
plt.plot(t, x_verlet, color='b')
plt.plot(t, theta_euler, color='r', alpha=0.5)
plt.xlabel("Temps [s]", size=20)
plt.ylabel("Angle [rad]", size=20)
plt.title("Oscillateur Harmonique x_verlet", size=30)

plt.figure(figsize=(12,8))
plt.plot(t, theta_point, color='b')
plt.plot(t, theta_point_euler, color='r', alpha=0.5)
plt.xlabel("Temps [s]", size=20)
plt.ylabel("Angle [rad]", size=20)
plt.title("Oscillateur Harmonique x_verlet point", size=30)
plt.show()"""

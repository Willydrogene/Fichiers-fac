import matplotlib.pyplot as plt
import numpy as np


# dθ/dt = θ_point
def func_1er_ordre(t, teta_point):
    dTeta_dt = teta_point
    return dTeta_dt


# d²θ/dt = - (g * θ) / l   sans frottement et en prenant une approximation sin(θ)=θ
def func_2eme_ordre(t, g, l, teta):
    dTeta_point_dt = -(g / l) * teta
    return dTeta_point_dt


# d²θ/dt = - (g * θ) / l   sans frottement en prenant le sin(θ)
def func_sin(t, g, l, teta):
    dTeta_point_dt_sin = -(g / l) * np.sin(teta)
    return dTeta_point_dt_sin


# Méthode Euler d'ordre 1
def euler_method(teta, teta_sin, teta_point, teta_point_sin, Nt):
    for i in np.arange(Nt - 1):
        teta[i + 1] = teta[i] + dt * func_1er_ordre(t[i], teta_point[i])
        teta_sin[i + 1] = teta_sin[i] + dt * func_1er_ordre(t[i], teta_point_sin[i])
        teta_point[i + 1] = teta_point[i] + dt * func_2eme_ordre(t[i], g, l, teta[i])
        teta_point_sin[i + 1] = teta_point_sin[i] + dt * func_sin(t[i], g, l, teta_sin[i])
    return teta, teta_sin, teta_point, teta_point_sin


# Techniquement c'est la même chose que la fonction: 'func_2eme_ordre()'
def equation_pendule(theta, l, g):
    d2theta_dt2 = -g * np.sin(theta) / l  # d²θ/dt²
    return d2theta_dt2


# Méthode Verlet d'ordre 2 (plus précise qu'Euler logiquement)
def verlet_method(theta_verlet, theta_point_verlet, dt, Nt):
    for i in range(1, Nt):
        theta_half = theta_verlet[i - 1] + theta_point_verlet[i - 1] * dt / 2
        theta_point_verlet[i] = theta_point_verlet[i - 1] + equation_pendule(theta_half, l, g) * dt
        theta_verlet[i] = theta_half + theta_point_verlet[i] * dt / 2
    return theta_verlet, theta_point_verlet


################################################ Conditions de l'experience ############################################

######################## Conditions initiales ########################
tmin = 0.0           # début de l'expérience  en s
tmax = 100.0         # fin de l'expérience    en s
dt = 0.001           # temps infinitésimal pour la précision
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

teta = np.zeros(Nt)
teta_sin = np.zeros(Nt)
teta_point = np.zeros(Nt)
teta_point_sin = np.zeros(Nt)
theta_verlet = np.zeros(Nt)  # Méthode Verlet
theta_point_verlet = np.zeros(Nt)  # Méthode Verlet

teta[0] = hauteur_du_laché_initial
teta_sin[0] = hauteur_du_laché_initial
teta_point[0] = vitesse_angulaire_initiale
teta_point_sin[0] = vitesse_angulaire_initiale
theta_verlet[0] = hauteur_du_laché_initial  # Méthode Verlet
theta_point_verlet[0] = vitesse_angulaire_initiale  # Méthode Verlet



################################################## Appel des fonctions #################################################

theta_verlet, theta_point_verlet = verlet_method(theta_verlet, theta_point_verlet, dt, Nt)
teta, teta_sin, teta_point, teta_point_sin = euler_method(teta, teta_sin, teta_point, teta_point_sin, Nt)


######################################################### PLOTS ########################################################

plt.figure(figsize=(12, 8))

# Premier sous-graphique : Position sans sinus et avec sinus
plt.subplot(4, 1, 1)  # Grille de 2 lignes, 1 colonne, sous-graphique 1
plt.plot(t, teta, color='b', label='Position sans sinus Euler')
plt.plot(t, teta_sin, color='r', label='Position avec sinus Euler', alpha=0.5)
plt.xlabel("Temps [s]", size=20)
plt.ylabel("Angle [rad]", size=20)
plt.title("Oscillateur Harmonique: position", size=30)
plt.legend(loc="upper right")

# Deuxième sous-graphique : Vitesse angulaire sans sinus et avec sinus
plt.subplot(4, 1, 2)  # Grille de 2 lignes, 1 colonne, sous-graphique 2
plt.plot(t, teta_point, color='b', label='v. ang. sans sinus, Euler')
plt.plot(t, teta_point_sin, color='r', label='v. ang, avec sinus Euler', alpha=0.5)
plt.xlabel("Temps [s]", size=20)
plt.ylabel("Vit. Ang. [rad/s]", size=20)
plt.title("Oscillateur Harmonique: vitesse angulaire", size=30)
plt.legend(loc="upper right")

# Troisième sous-graphique : Position Euler et Verlet
plt.subplot(4, 1, 3)  # Grille de 2 lignes, 1 colonne, sous-graphique 2
plt.plot(t, theta_verlet, color='b', label='Position Verlet')
plt.plot(t, teta_sin, color='r', label='Position Euler', alpha=0.5)
plt.xlabel("Temps [s]", size=20)
plt.ylabel("Angle [rad]", size=20)
plt.title("Oscillateur Harmonique: position verlet", size=30)
plt.legend(loc="upper right")

# Quatrième sous-graphique : Vitesse angulaire Euler et Verlet
plt.subplot(4, 1, 4)  # Grille de 2 lignes, 1 colonne, sous-graphique 2
plt.plot(t, theta_point_verlet, color='b', label='v. ang. Verlet')
plt.plot(t, teta_point_sin, color='r', label='v. ang. Euler', alpha=0.5)
plt.xlabel("Temps [s]", size=20)
plt.ylabel("Vit. Ang. [rad/s]", size=20)
plt.title("Oscillateur Harmonique: vitesse verlet", size=30)
plt.legend(loc="upper right")

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

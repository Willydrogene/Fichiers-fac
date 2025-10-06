import matplotlib.pyplot as plt
import numpy as np


# dθ/dt = θ_point
def func_1er_ordre(t, teta_point):
    dTeta_dt = teta_point
    return dTeta_dt


# d²θ/dt = - (g * θ) / l   sans frottement et en prenant une approximation sin(θ)=θ
def func_2eme_ordre(t, omega, teta):
    dTeta_point_dt = -omega ** 2 * teta
    return dTeta_point_dt


# d²θ/dt = - (g * θ) / l   sans frottement en prenant le sin(θ)
def func_sin(t, omega, teta):
    dTeta_point_dt_sin = -omega ** 2 * np.sin(teta)
    return dTeta_point_dt_sin


# Méthode Euler d'ordre 1
def euler_method(teta, teta_sin, teta_point, teta_point_sin, Nt):
    for i in np.arange(Nt - 1):
        teta[i + 1] = teta[i] + dt * func_1er_ordre(t[i], teta_point[i])
        teta_sin[i + 1] = teta_sin[i] + dt * func_1er_ordre(t[i], teta_point_sin[i])
        teta_point[i + 1] = teta_point[i] + dt * func_2eme_ordre(t[i], omega, teta[i])
        teta_point_sin[i + 1] = teta_point_sin[i] + dt * func_sin(t[i], omega, teta_sin[i])
    return teta, teta_sin, teta_point, teta_point_sin


################################################ Conditions de l'experience ############################################

######################## Conditions initiales ########################
tmin = 0.0              # début de l'expérience  en s
tmax = 100.0            # fin de l'expérience    en s
dt = 0.001              # temps infinitésimal pour la précision
g = 9.8                 # pesanteur
l = 1.00                # longueur de la tige   en  mètre
omega = np.sqrt(g / l)  # pulsation             en  s^-1

# masse = 0.001           # masse                 en  kg
# d = 0.20                # diamètre de ma spĥère en  mètre
# mu = 1.8 * 10 ** (-5)   # viscosité du fluide   en  Pa.s


hauteur_du_laché_initial = np.pi / 2
vitesse_angulaire_initiale = 0

######################## Création de tableaux ########################

Nt = int((tmax - tmin) / dt) + 1
t = np.linspace(tmin, tmax, Nt)

teta = np.zeros(Nt)
teta_sin = np.zeros(Nt)
teta_point = np.zeros(Nt)
teta_point_sin = np.zeros(Nt)

teta[0] = hauteur_du_laché_initial
teta_sin[0] = hauteur_du_laché_initial
teta_point[0] = vitesse_angulaire_initiale
teta_point_sin[0] = vitesse_angulaire_initiale

################################################## Appel de la fonction#################################################

teta, teta_sin, teta_point, teta_point_sin = euler_method(teta, teta_sin, teta_point, teta_point_sin, Nt)

######################################################### PLOTS ########################################################

plt.figure(figsize=(12, 8))

# Premier sous-graphique : position
plt.subplot(2, 1, 1)  # Grille de 2 lignes, 1 colonne, sous-graphique 1
plt.plot(t, teta, color='b', label='Position sans sinus')
plt.plot(t, teta_sin, color='r', label='Position avec sinus', alpha=0.5)
plt.xlabel("Temps [s]", size=20)
plt.ylabel("Angle [rad]", size=20)
plt.title("Oscillateur Harmonique: position", size=30)
plt.legend(loc="upper right")

# Deuxième sous-graphique : vitesse angulaire
plt.subplot(2, 1, 2)  # Grille de 2 lignes, 1 colonne, sous-graphique 2
plt.plot(t, teta_point, color='b', label='Vit. Ang. sans sinus')
plt.plot(t, teta_point_sin, color='r', label='Vit. Ang. avec sinus', alpha=0.5)
plt.xlabel("Temps [s]", size=20)
plt.ylabel("Vit. ang. [rad/s]", size=20)
plt.title("Oscillateur Harmonique: vitesse angulaire", size=30)
plt.legend(loc="upper right")

plt.tight_layout()  # Ajuster automatiquement les espacements entre les sous-graphiques
plt.show()

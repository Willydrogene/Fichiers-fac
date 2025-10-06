import matplotlib.pyplot as plt
import numpy as np


# d²θ/dt = (-k/m)*θ_point - g*sin(θ) / l   avec k le coeff de frottements
def equation_pendule(t, g, l, mu, d, masse, theta_point_verlet, theta_half):
    dtheta_point_verlet_dt = ((-3 * np.pi * mu * d * theta_point_verlet) / masse) - (
                (g * np.sin(theta_half)) / l)  # d²θ/dt²
    return dtheta_point_verlet_dt


# Méthode Verlet d'ordre 2 (plus précise qu'Euler logiquement)
def verlet_method(theta_verlet, theta_point_verlet, dt, Nt, masse, g, l):
    for i in range(1, Nt):
        theta_half = theta_verlet[i - 1] + theta_point_verlet[
            i - 1] * dt / 2  # Il faut imaginer la méthode trapèzes des intégrales
        temp_theta_point_verlet = theta_point_verlet[i - 1] + equation_pendule(t[i], g, l, mu, d, masse, theta_point_verlet[i - 1], theta_half) * dt
        theta_verlet[i] = theta_half + temp_theta_point_verlet * dt / 2
        theta_point_verlet[i] = temp_theta_point_verlet
    return theta_verlet, theta_point_verlet


################################################ Conditions de l'expérience ############################################

######################## Conditions initiales ########################
tmin = 0.0              # début de l'expérience  en s
tmax = 120.0            # fin de l'expérience    en s
dt = 0.0001             # temps infinitésimal pour la précision
dt2 = 0.01
dt3 = 0.1
g = 9.8                 # pesanteur
l = 1.00                # longueur de la tige   en  mètre
masse = 0.001           # masse                 en  kg
d = 0.20                # diamètre de ma spĥère en  mètre
mu = 1.8 * 10 ** (-5)   # viscosité du fluide   en  Pa.s

hauteur_du_laché_initial = np.pi / 2
vitesse_angulaire_initiale = 0

######################## Création de tableaux ########################

Nt = int((tmax - tmin) / dt) + 1
Nt2 = int((tmax - tmin) / dt2) + 1
Nt3 = int((tmax - tmin) / dt3) + 1
t = np.linspace(tmin, tmax, Nt)
t2 = np.linspace(tmin, tmax, Nt2)
t3 = np.linspace(tmin, tmax, Nt3)

theta_verlet = np.zeros(Nt)             # Méthode Verlet
theta_point_verlet = np.zeros(Nt)       # Méthode Verlet
theta_verlet2 = np.zeros(Nt2)           # Méthode Verlet
theta_point_verlet2 = np.zeros(Nt2)     # Méthode Verlet
theta_verlet3 = np.zeros(Nt3)           # Méthode Verlet
theta_point_verlet3 = np.zeros(Nt3)     # Méthode Verlet

theta_verlet[0] = hauteur_du_laché_initial           # Méthode Verlet
theta_point_verlet[0] = vitesse_angulaire_initiale   # Méthode Verlet
theta_verlet2[0] = hauteur_du_laché_initial          # Méthode Verlet
theta_point_verlet2[0] = vitesse_angulaire_initiale  # Méthode Verlet
theta_verlet3[0] = hauteur_du_laché_initial          # Méthode Verlet
theta_point_verlet3[0] = vitesse_angulaire_initiale  # Méthode Verlet

################################################## Appel des fonctions #################################################

verlet_method(theta_verlet, theta_point_verlet, dt, Nt, masse, g, l)
verlet_method(theta_verlet2, theta_point_verlet2, dt2, Nt2, masse, g, l)
verlet_method(theta_verlet3, theta_point_verlet3, dt3, Nt3, masse, g, l)

######################################################### PLOTS ########################################################

plt.figure(figsize=(12, 8))

verlet1 = 'Position dt1: ' + str(dt)
verlet2 = 'Position dt2: ' + str(dt2)
verlet3 = 'Position dt3: ' + str(dt3)
verlet11 = 'Vit. Ang. dt1: ' + str(dt)
verlet22 = 'Vit. Ang. dt2: ' + str(dt2)
verlet33 = 'Vit. Ang. dt3: ' + str(dt3)

# Premier sous-graphique : Positions
plt.subplot(2, 1, 1)  # Grille de 2 lignes, 1 colonne, sous-graphique 1
plt.plot(t, theta_verlet, color='b', label=verlet1)
plt.plot(t2, theta_verlet2, color='r', label=verlet2, alpha=0.5)
plt.plot(t3, theta_verlet3, color='g', label=verlet3)
plt.xlabel("Temps [s]", size=20)
plt.ylabel("Angle [rad]", size=20)
plt.title("Oscillateur avec frot: position", size=30)
plt.legend(loc="upper right", ncol=3)

# Deuxième sous-graphique : Vitesses Angulaires
plt.subplot(2, 1, 2)  # Grille de 2 lignes, 1 colonne, sous-graphique 2
plt.plot(t, theta_point_verlet, color='b', label=verlet1)
plt.plot(t2, theta_point_verlet2, color='r', label=verlet2, alpha=0.5)
plt.plot(t3, theta_point_verlet3, color='g', label=verlet3)
plt.xlabel("Temps [s]", size=20)
plt.ylabel("Vit. ang. [rad/s]", size=20)
plt.title("Oscillateur avec frot: vitesse angulaire", size=30)
plt.legend(loc="upper right", ncol=3)

plt.tight_layout()  # Ajuster automatiquement les espacements entre les sous-graphiques
plt.show()

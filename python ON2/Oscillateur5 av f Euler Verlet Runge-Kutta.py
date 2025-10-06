import matplotlib.pyplot as plt
import numpy as np


# dθ/dt = θ_point
def func_1er_ordre(t, theta_point_euler):
    dTheta_dt = theta_point_euler
    return dTheta_dt


# d²θ/dt = (-k/m)*θ_point - g*sin(θ) / l   avec k le coeff de frottements
def func_2eme_ordre(t, g, l, mu, d, masse, theta_point_euler, theta_euler):
    dTheta_point_dt = ((-3 * np.pi * mu * d * theta_point_euler) / masse) - ((g / l) * np.sin(theta_euler))
    return dTheta_point_dt


# Méthode Euler d'ordre 1
def euler_method(theta_euler, theta_point_euler, dt, Nt):
    for i in np.arange(Nt - 1):
        theta_euler[i + 1] = theta_euler[i] + dt * func_1er_ordre(t[i], theta_point_euler[i])
        theta_point_euler[i + 1] = theta_point_euler[i] + dt * func_2eme_ordre(t[i], g, l, mu, d, masse, theta_point_euler[i], theta_euler[i])
    return theta_euler, theta_point_euler


# Méthode Verlet d'ordre 2 (plus précise qu'Euler logiquement)
def verlet_method(theta_verlet, theta_point_verlet, dt, Nt, masse, g, l):
    for i in range(1, Nt):
        theta_half = theta_verlet[i - 1] + theta_point_verlet[i - 1] * dt / 2  # Il faut imaginer la méthode trapèzes des intégrales
        temp_theta_point_verlet = theta_point_verlet[i - 1] + func_2eme_ordre(t[i], g, l, mu, d, masse, theta_point_verlet[i - 1], theta_half) * dt
        theta_verlet[i] = theta_half + temp_theta_point_verlet * dt / 2
        theta_point_verlet[i] = temp_theta_point_verlet

        # Calcul de l'énergie à chaque instant t
        energie_potentielle[i] = masse * g * l * (1 - np.cos(theta_verlet[i]))
        energie_cinetique[i] = 0.5 * masse * (l ** 2 * theta_point_verlet[i] ** 2)  # v² = (l*θ_point)²
        energie_mecanique[i] = energie_potentielle[i] + energie_cinetique[i]


    return theta_verlet, theta_point_verlet, energie_potentielle, energie_cinetique, energie_mecanique


# Méthode Runge-Kutta d'ordre 4
def runge_kutta_method(theta_rk, theta_point_rk, dt, Nt):
    for i in range(Nt - 1):
        t = i * dt
        k1_theta = dt * func_1er_ordre(t, theta_point_rk[i])
        k1_theta_point = dt * func_2eme_ordre(t, g, l, mu, d, masse, theta_point_rk[i], theta_rk[i])

        k2_theta = dt * func_1er_ordre(t + dt / 2, theta_point_rk[i] + k1_theta / 2)
        k2_theta_point = dt * func_2eme_ordre(t + dt / 2, g, l, mu, d, masse, theta_point_rk[i] + k1_theta / 2, theta_rk[i] + k1_theta / 2)

        k3_theta = dt * func_1er_ordre(t + dt / 2, theta_point_rk[i] + k2_theta / 2)
        k3_theta_point = dt * func_2eme_ordre(t + dt / 2, g, l, mu, d, masse, theta_point_rk[i] + k2_theta / 2, theta_rk[i] + k2_theta / 2)

        k4_theta = dt * func_1er_ordre(t + dt, theta_point_rk[i] + k3_theta)
        k4_theta_point = dt * func_2eme_ordre(t + dt, g, l, mu, d, masse, theta_point_rk[i] + k3_theta, theta_rk[i] + k3_theta)

        theta_rk[i + 1] = theta_rk[i] + (k1_theta + 2 * k2_theta + 2 * k3_theta + k4_theta) / 6
        theta_point_rk[i + 1] = theta_point_rk[i] + (k1_theta_point + 2 * k2_theta_point + 2 * k3_theta_point + k4_theta_point) / 6

    return theta_rk, theta_point_rk


# Pour avoir les données des graphes dans un fichier .txt
def sauvegarder_donnees(donnees, nom_fichier):
    with open(nom_fichier, 'w') as fichier:
        for ligne in donnees:
            fichier.write(str(ligne) + '\n')


# Pour comparer mes données dans le .txt (les données s'affichent côte à côte)
def comparer_listes(liste1, liste2, nom_fichier):
    with open(nom_fichier, 'w') as fichier:
        fichier.write('Comparaison\n')
        fichier.write('theta_euler\tx_verlet\n')
        for item1, item2 in zip(liste1, liste2):
            fichier.write(str(item1) + '\t' + str(item2) + '\n')


################################################ Conditions de l'expérience ############################################

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

theta_euler = np.zeros(Nt)          # Méthode Euler
theta_point_euler = np.zeros(Nt)    # Méthode Euler
theta_verlet = np.zeros(Nt)         # Méthode Verlet
theta_point_verlet = np.zeros(Nt)   # Méthode Verlet
theta_rk = np.zeros(Nt)             # Méthode Runge-Kutta
theta_point_rk = np.zeros(Nt)       # Méthode Runge-Kutta
energie_mecanique = np.zeros(Nt)
energie_potentielle = np.zeros(Nt)
energie_cinetique = np.zeros(Nt)

theta_euler[0] = hauteur_du_laché_initial
theta_point_euler[0] = vitesse_angulaire_initiale
theta_verlet[0] = hauteur_du_laché_initial          # Méthode Verlet
theta_point_verlet[0] = vitesse_angulaire_initiale  # Méthode Verlet
theta_rk[0] = hauteur_du_laché_initial              # Méthode Runge-Kutta
theta_point_rk[0] = vitesse_angulaire_initiale      # Méthode Runge-Kutta



################################################## Appel des fonctions #################################################

verlet_method(theta_verlet, theta_point_verlet, dt, Nt, masse, g, l)
euler_method(theta_euler, theta_point_euler, dt, Nt)
runge_kutta_method(theta_rk, theta_point_rk, dt, Nt)

nom_fichier = 'donnees.txt'
"""
sauvegarder_donnees(theta_euler, nom_fichier)
sauvegarder_donnees(x_verlet, nom_fichier)
comparer_listes(theta_euler, x_verlet, nom_fichier)
"""
######################################################### PLOTS ########################################################

plt.figure(figsize=(12, 8))

# Premier sous-graphique : Positions
plt.subplot(3, 1, 1)  # Grille de 3 lignes, 1 colonne, sous-graphique 1
plt.plot(t, theta_euler, color='b', label='Position Euler')
plt.plot(t, theta_verlet, color='r', label='Position Verlet', alpha=0.5)
plt.plot(t, theta_rk, color='g', label='Position Runge-Kutta')
plt.xlabel("Temps [s]", size=20)
plt.ylabel("Angle [rad]", size=20)
plt.title("Oscillateur avec frot: position", size=30)
plt.legend(loc="upper right", ncol=3)

# Deuxième sous-graphique : Vitesses Angulaires
plt.subplot(3, 1, 2)  # Grille de 3 lignes, 1 colonne, sous-graphique 2
plt.plot(t, theta_point_euler, color='b', label='v. ang. Euler')
plt.plot(t, theta_point_verlet, color='r', label='v. ang. Verlet', alpha=0.5)
plt.plot(t, theta_point_rk, color='g', label='v. ang. Runge-Kutta')
plt.xlabel("Temps [s]", size=20)
plt.ylabel("Vit. ang. [rad/s]", size=20)
plt.title("Oscillateur avec frot: vitesse angulaire", size=30)
plt.legend(loc="upper right", ncol=3)

# Troisième sous-graphique : Énergies
plt.subplot(3, 1, 3)  # Grille de 3 lignes, 1 colonne, sous-graphique 3
plt.plot(t, energie_potentielle, color='g', label='Énergie potentielle')
plt.plot(t, energie_cinetique, color='b', label='Énergie cinétique')
plt.plot(t, energie_mecanique, color='r', label='Énergie mécanique')
plt.xlabel("Temps [s]", size=20)
plt.ylabel("Énergie [J]", size=20)
plt.title("Énergies du pendule (Verlet)", size=30)
plt.legend(loc="upper right", ncol=3)

plt.tight_layout()  # Ajuster automatiquement les espacements entre les sous-graphiques
plt.show()

################### Je vous invite à mettre le plot en pleine page, et zommer vers les 100 secondes! ###################
################### Je vous invite également à augmenter le dt pour tester la précision des méthodes ###################
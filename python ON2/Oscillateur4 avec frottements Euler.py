import matplotlib.pyplot as plt
import numpy as np


# dθ/dt = θ_point
def func_1er_ordre(t, theta_point):
    dTheta_dt = theta_point
    return dTheta_dt


# d²θ/dt = - (g * θ) / l   sans frottement en prenant le sin(θ)
def func_2eme_ordre(t, g, l, theta):
    dTheta_point_dt = -(g / l) * np.sin(theta)
    return dTheta_point_dt


# d²θ/dt = - (g * θ) / l   avec frottement en prenant le sin(θ)
def func_frottements(t, g, l, mu, d, masse, theta_point_frott, theta_frott):
    dTheta_point_frott_dt = ((-3 * np.pi * mu * d * theta_point_frott) / masse) - ((g / l) * np.sin(theta_frott))
    return dTheta_point_frott_dt


# Méthode Euler d'ordre 1
def euler_method(theta, theta_frott, theta_point, theta_point_frott, Nt):
    for i in np.arange(Nt - 1):
        theta[i + 1] = theta[i] + dt * func_1er_ordre(t[i], theta_point[i])
        theta_frott[i + 1] = theta_frott[i] + dt * func_1er_ordre(t[i], theta_point_frott[i])
        theta_point[i + 1] = theta_point[i] + dt * func_2eme_ordre(t[i], g, l, theta[i])
        theta_point_frott[i + 1] = theta_point_frott[i] + dt * func_frottements(t[i], g, l, mu, d, masse, theta_point_frott[i], theta_frott[i])
    return theta, theta_frott, theta_point, theta_point_frott


# Pour avoir les données des graphes dans un fichier .txt
def sauvegarder_donnees(donnees, nom_fichier):
    with open(nom_fichier, 'w') as fichier:
        for ligne in donnees:
            fichier.write(str(ligne) + '\n')


# Pour comparer mes données dans le .txt (les données s'affichent côte à côte)
def comparer_listes(liste1, liste2, nom_fichier):
    with open(nom_fichier, 'w') as fichier:
        fichier.write('Comparaison\n')
        fichier.write('sans frott\tavec frott\n')
        for item1, item2 in zip(liste1, liste2):
            fichier.write(str(item1) + '\t' + str(item2) + '\n')


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

theta = np.zeros(Nt)
theta_frott = np.zeros(Nt)
theta_point = np.zeros(Nt)
theta_point_frott = np.zeros(Nt)

theta[0] = hauteur_du_laché_initial
theta_frott[0] = hauteur_du_laché_initial
theta_point[0] = vitesse_angulaire_initiale
theta_point_frott[0] = vitesse_angulaire_initiale


################################################## Appel des fonctions #################################################

theta, theta_frott, theta_point, theta_point_frott = euler_method(theta, theta_frott, theta_point, theta_point_frott, Nt)
nom_fichier = 'donnees.txt'
"""
sauvegarder_donnees(theta, nom_fichier)
sauvegarder_donnees(theta_frott, nom_fichier)
comparer_listes(theta, theta_frott, nom_fichier)
"""
######################################################### PLOTS ########################################################

plt.figure(figsize=(12, 8))

# Premier sous-graphique : position
plt.subplot(2, 1, 1)  # Grille de 2 lignes, 1 colonne, sous-graphique 1
plt.plot(t, theta, color='b', label='sans frottement')
plt.plot(t, theta_frott, color='r', label='avec frottements', alpha=0.5)
plt.xlabel("Temps [s]", size=20)
plt.ylabel("Angle [rad]", size=20)
plt.title("Oscillateur avec/sans frottements: position", size=30)
plt.legend(loc="upper right")

# Deuxième sous-graphique : vitesse angulaire
plt.subplot(2, 1, 2)  # Grille de 2 lignes, 1 colonne, sous-graphique 2
plt.plot(t, theta_point, color='b', label='v. ang. sans frott')
plt.plot(t, theta_point_frott, color='r', label='v. ang. avec frott', alpha=0.5)
plt.xlabel("Temps [s]", size=20)
plt.ylabel("Vit. Ang. [rad/s]", size=20)
plt.title("Oscillateur avec/sans frottements: vitesse angulaire", size=30)
plt.legend(loc="upper right")

plt.tight_layout()  # Ajuster automatiquement les espacements entre les sous-graphiques
plt.show()



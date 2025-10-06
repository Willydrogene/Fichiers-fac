import matplotlib
matplotlib.use('TkAgg')  #Qt5Agg
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import os

# d²θ/dt = (-k/m)*θ_point - g*sin(θ) / l   avec k le coeff de frottements
def equation_pendule(t, g, l, mu, d, masse, theta_point_verlet, theta_half):
    dtheta_point_verlet_dt = ((-3 * np.pi * mu * d * theta_point_verlet) / masse) - ((g * np.sin(theta_half)) / l)  # d²θ/dt²
    return dtheta_point_verlet_dt


# Méthode Verlet d'ordre 2 (plus précise qu'Euler logiquement)
def verlet_method(theta_verlet, theta_point_verlet, dt, Nt, masse, g, l):
    for i in range(1, Nt):
        theta_half = theta_verlet[i - 1] + theta_point_verlet[i - 1] * dt / 2  # Il faut imaginer la méthode trapèzes des intégrales
        temp_theta_point_verlet = theta_point_verlet[i - 1] + equation_pendule(t[i], g, l, mu, d, masse, theta_point_verlet[i - 1], theta_half) * dt
        theta_verlet[i] = theta_half + temp_theta_point_verlet * dt / 2
        theta_point_verlet[i] = temp_theta_point_verlet
    return theta_verlet, theta_point_verlet


################################################ Conditions de l'expérience ############################################

######################## Conditions initiales ########################
tmin = 0.0              # début de l'expérience  en s
tmax = 3.0              # fin de l'expérience    en s
dt = 0.1                # temps infinitésimal pour la précision
g = 9.8                 # pesanteur
l = 1.00                # longueur de la tige   en  mètre
masse = 0.001           # masse                 en  kg
d = 0.50                # diamètre de ma spĥère en  mètre
mu = 1.8 * 10 ** (-5)   # viscosité du fluide   en  Pa.s

hauteur_du_laché_initial = np.pi / 2
vitesse_angulaire_initiale = 0

######################## Création de tableaux ########################

Nt = int((tmax - tmin) / dt) + 1
#print(Nt)
t = np.linspace(tmin, tmax, Nt)

theta_verlet = np.zeros(Nt)             # Méthode Verlet
theta_point_verlet = np.zeros(Nt)       # Méthode Verlet

theta_verlet[0] = hauteur_du_laché_initial           # Méthode Verlet
theta_point_verlet[0] = vitesse_angulaire_initiale   # Méthode Verlet

################################################## Appel des fonctions #################################################

verlet_method(theta_verlet, theta_point_verlet, dt, Nt, masse, g, l)

######################################################### Animation ####################################################

def init():
    # Initialisation de l'animation
    pendule.set_data([], [])
    sphere.center = (0, -l)
    sphere.radius = d / 2

    # Initialisation du graphique de θ en fonction du temps
    line.set_data([], [])
    line_theta.set_data([], [])

    return pendule, sphere, line, line_theta

fig, ax = plt.subplots(1, 2, figsize=(13, 6))  # Créer une grille de sous-graphiques, 1 ligne, 2 colonnes

# Sous-graphique 1 : Animation
ax1 = ax[0]
ax1.set_xlim(-l - 0.2, l + 0.2)
ax1.set_ylim(-l - 0.2, l + 0.2)
ax1.set_title("Oscillateur avec frottement : position", size=20)
ax1.set_xlabel('x [m]', size=16)
ax1.set_ylabel('y [m]', size=16)
ax1.set_aspect('equal', adjustable='box')

pendule, = ax1.plot([], [], color='r', linestyle='-', linewidth=2)
sphere = plt.Circle((0, 0), d / 2, color='r')
ax1.add_artist(sphere)

# Sous-graphique 2 : Graphique de θ en fonction de t
ax2 = ax[1]
ax2.set_xlim(tmin, tmax)
ax2.set_ylim(-np.pi, np.pi)
ax2.set_xlabel('t [s]', size=16)
ax2.set_ylabel('θ [rad]', size=16)
ax2.set_title('Évolution de θ(t)', size=20)

line, = ax2.plot([], [], color='b', label='Position Verlet')
line_theta, = ax2.plot([], [], color='g', label='θ(t)')  # Définition de la ligne pour θ(t)


def update(frame):
    # Mise à jour de l'animation
    if frame < Nt:
        theta = theta_verlet[frame]
        x = l * np.sin(theta)
        y = -l * np.cos(theta)
        pendule.set_data([0, x], [0, y])
        sphere.center = (x, y)

    # Mise à jour du graphique de θ en fonction de t
    line_theta.set_data(t[:frame], theta_verlet[:frame])

    # Condition pour arrêter la mise à jour lorsque le temps t est terminé
    if frame == Nt - 1:
        ani.event_source.stop()

    return pendule, sphere, line, line_theta


def save_progress_callback(frame_number, total_frames):
    progress = (frame_number / total_frames) * 100
    print(f"Progress: {progress:.1f}%")

interval = (tmax*1000)/Nt
ani = FuncAnimation(fig, update, frames=Nt, init_func=init, blit=True, interval=interval)

# Obtenir le chemin absolu du fichier Python en cours d'exécution
current_dir = os.path.dirname(os.path.abspath(__file__))
gif_path = os.path.join(current_dir, 'animation.gif')

# Sauvegarde de l'animation en tant que vidéo
ani.save(gif_path, writer='pillow', progress_callback=save_progress_callback)
plt.tight_layout()
plt.show()

#%matplotlib qt sur spyder
#%matplotlib inline pour jupyter notebook
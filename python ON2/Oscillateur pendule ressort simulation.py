import matplotlib
matplotlib.use('Agg')  #Qt5Agg
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.ticker as ticker
import os

# J'ai une première equa diff 2eme ordre sur L suivant e.rho
def func_2eme_ordre_l(t, m, g, mu, d, k, l0, l, l_point, theta, theta_point):
    dl_point_dt = g*np.cos(theta) - (k*(l - l0))/m - (3*np.pi*mu*d*l_point)/m + l*(theta_point**2)
    return dl_point_dt


# J'ai une deuxieme equa diff 2eme ordre sur theta selon e.phi
def func_2eme_ordre(t, m, g, mu, d, k, l, l_point, theta, theta_point):
    dTheta_point_dt = -(g*np.sin(theta))/l - (3*np.pi*mu*d*theta_point)/m - (2*l_point*theta_point)/l
    return dTheta_point_dt


# J'utilise Verlet pour plus de précision avec un gros pas de temps dt
def verlet_method(t, m, g, mu, d, k, l0, l, l_point, theta, theta_point, dt, Nt):
    for i in range(1, Nt):
        theta_half = theta[i - 1] + theta_point[i - 1] * dt / 2
        temp_theta_point_verlet = theta_point[i - 1] + func_2eme_ordre(t[i], m, g, mu, d, k, l[i-1], l_point[i-1], theta_half, theta_point[i-1]) * dt
        theta[i] = theta_half + temp_theta_point_verlet * dt / 2
        theta_point[i] = temp_theta_point_verlet

        l_half = l[i - 1] + l_point[i - 1] * dt / 2
        temp_l_point_verlet = l_point[i - 1] + func_2eme_ordre_l(t[i], m, g, mu, d, k, l0, l_half, l_point[i - 1], theta[i-1], theta_point[i - 1]) * dt
        l[i] = l_half + temp_l_point_verlet * dt / 2
        l_point[i] = temp_l_point_verlet
    return theta, theta_point, l, l_point

################################################ Conditions de l'expérience ############################################

######################## Conditions initiales ########################
tmin = 0                                    # début de l'expérience  en s
tmax = 10                                   # fin de l'expérience    en s
dt = 0.01                                   # temps infinitésimal pour la précision
m = 0.2                                     # masse                  en  kg
g = 9.8                                     # pesanteur              en  m/s²
frottements_en_plus = 5000                  # les frottements des matériaux pour plus de réalisme (j'ai pris au pif)
mu = 1.8*10**(-5) * frottements_en_plus     # viscosité du fluide    en  Pa.s
d = 0.05                                    # diamètre de ma spĥère  en  mètre
l0 = 0.5                                    # longueur du ressort à l'équilibre
k = 40                                      # constante de raideur du ressort

angle_initial = 56*(np.pi)/57               # pour le mettre en l'air et voir ce qu'il se passe
longueur_initiale = 0.5                     # pour comprimer ou étirer le ressort dès le début
vitesse_angulaire_initiale = 0              # aug. et observez le ressort, mais il faut adapter k pour des valeurs limites
vitesse_long_pendule = 0                    # pas trop réalisable dans la vraie vie

######################## Création de tableaux ########################
Nt = int((tmax - tmin) / dt) + 1
t = np.linspace(tmin, tmax, Nt)

theta = np.zeros(Nt)
l = np.zeros(Nt)
theta_point = np.zeros(Nt)
l_point = np.zeros(Nt)
theta[0] = angle_initial
l[0] = longueur_initiale
theta_point[0] = vitesse_angulaire_initiale
l_point[0] = vitesse_long_pendule


################################################## Appel de la fonction ################################################

verlet_method(t, m, g, mu, d, k, l0, l, l_point, theta, theta_point, dt, Nt)

######################################################### Animation ####################################################
# Pour avoir un axe x avec des angles n*pi
def pi_formatter(x, pos):
    """Formateur d'étiquettes pour les valeurs des axes en multiples de pi"""
    N = int(np.round(x / (np.pi/2)))
    if N == 0:
        return "0"
    elif N == 1:
        return r"$\pi/2$"
    elif N == 2:
        return r"$\pi$"
    elif N % 2 > 0:
        return r"${0}\pi/2$".format(N)
    else:
        return r"${0}\pi$".format(N//2)

def init():
    # Initialisation de l'animation
    pendule.set_data([], [])
    pendule_trace.set_data([], [])
    sphere.center = (0, -l0)
    sphere.radius = d / 2

    # Initialisation du graphique de θ en fonction du temps
    line_theta.set_data([], [])

    return pendule, sphere, pendule_trace, line_theta

# Créer la figure et les sous-graphiques
fig, ax = plt.subplots(1, 2, figsize=(13, 6))
#plt.get_current_fig_manager().window.state('zoomed')

# Sous-graphique 1 : Animation
ax1 = ax[0]
ax1.set_xlim(-np.max(l) - 0.2, np.max(l) + 0.2)
ax1.set_ylim(-np.max(l) - 0.2, np.max(l) + 0.2)
ax1.set_title("Pendule/Ressort avec frottements : position", size=20)
ax1.set_xlabel('x [m]', size=16)
ax1.set_ylabel('y [m]', size=16)
ax1.set_aspect('equal', adjustable='box')


pendule, = ax1.plot([], [], color='r', linestyle='-', linewidth=2)

sphere = plt.Circle((0, 0), d / 2, color='g')
ax1.add_artist(sphere)

# Tracé de la traînée du pendule
pendule_trace, = ax1.plot([], [], color='b', linestyle='-', linewidth=0.5)


# Sous-graphique 2 : Graphique de θ en fonction de t
ax2 = ax[1]
ax2.set_xlim(np.min(theta) - 0.2, np.max(theta) + 0.2)
ax2.set_ylim(np.min(l) - 0.2, np.max(l) + 0.2)
ax2.xaxis.set_major_formatter(ticker.FuncFormatter(pi_formatter))
ax2.set_xlabel("Angle [rad]", size=15)
ax2.set_ylabel("Long pendule [m]", size=15)
ax2.set_title("Coordonnées cylindriques : position", size=20)
ax2.set_aspect('equal', adjustable='box')
ax2.invert_yaxis()  # Pour que ce soit en lien avec les coordonnées cartésiennes, meme si c'est cyl ici

line_theta, = ax2.plot([], [], color='g', linewidth=0.7, label='θ(t)')  # Définition de la ligne pour θ(t)


def update(frame):
    # Mise à jour de l'animation
    if frame < Nt:
        thetaa = theta[frame]
        ll = l[frame]
        x = ll * np.sin(thetaa)
        y = -ll * np.cos(thetaa)
        pendule.set_data([0, x], [0, y])
        sphere.center = (x, y)

        # Mettre à jour le tracé du ressort
        pendule_trace.set_data(l[:frame] * np.sin(theta[:frame]), -l[:frame] * np.cos(theta[:frame]))


    # Mise à jour du graphique de θ en fonction de t
    line_theta.set_data(theta[:frame], l[:frame])

    # Condition pour arrêter la mise à jour lorsque le temps t est terminé
    if frame == Nt - 1:
        ani.event_source.stop()

    return pendule, sphere, pendule_trace, line_theta

dpi = fig.get_dpi()

# Définir le DPI de la figure
fig.set_dpi(dpi)

interval = Nt/(tmax*1000)  # Si dt<0.01 ca ne marche pas je ne sais pas pourquoi
ani = FuncAnimation(fig, update, frames=Nt, init_func=init, blit=True, interval=interval)


def save_progress_callback(frame_number, total_frames):
    progress = (frame_number / total_frames) * 100
    print(f"Progress: {progress:.1f}%")


# Obtenir le chemin absolu du fichier Python en cours d'exécution
current_dir = os.path.dirname(os.path.abspath(__file__))
gif_path = os.path.join(current_dir, 'animation ressort.gif')
print(gif_path)
# Sauvegarde de l'animation en tant que vidéo
ani.save(gif_path, writer='pillow', fps=30, savefig_kwargs={'transparent': True}, progress_callback=save_progress_callback)  # à commenter pour aller plus vite
plt.tight_layout()
plt.show()
